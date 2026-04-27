# SysMLv2 Validation and Error Correction Skill

This skill equips AI Agents (like Claude, Gemini, ChatGPT, DeepSeek) with the specific knowledge required to act as a **SysMLv2 Linter and Validator**. Because Large Language Models can occasionally hallucinate syntax or misapply SysMLv2 concepts, this skill provides a strict checklist to verify any generated SysMLv2 code *before* presenting it to the user.

## Agent Instructions: How to use this skill

When you are asked to review, validate, or fix SysMLv2 code (or immediately after you have generated SysMLv2 code yourself), you must execute the following checks line-by-line. Do not assume the code is correct just because it looks structurally sound. 

If any of the following rules are violated, you must rewrite the code to correct them.

### 1. Usage vs. Definition Verification
- **Check:** Are there explicit definitions (e.g., `part def`, `port def`, `action def`) for every type used in the model?
- **Correction:** If a usage is declared (e.g., `subject toaster : ToasterSystem;`), ensure that `part def ToasterSystem;` exists in a reachable scope. Do not invent usages without defining their types.

### 2. Requirement Syntax and Traceability
- **Check:** Does the model use `satisfy requirement Requirements::'Some Requirement'`?
- **Correction:** **Remove** the `requirement` keyword in `satisfy` statements. It must be `satisfy Requirements::'Some Requirement';`.
- **Check:** Are system requirements defined as definitions (`requirement def`) instead of usages?
- **Correction:** Actual project requirements must be usages: `requirement <'ID'> 'Name' : RequirementType { ... }`.

### 3. Framing Concerns
- **Check:** Does the code use `frame concern StakeholderConcerns::'Safety' ;`?
- **Correction:** **Remove** the `concern` keyword. It must be `frame StakeholderConcerns::'Safety';`.

### 4. Special Characters in Unit Symbols
- **Check:** Are unit symbols containing special characters left unquoted? (e.g., `[°C]`, `[Ω]`).
- **Correction:** You **must** wrap non-alphanumeric unit symbols in single quotes within the brackets: `['°C']`.

### 5. ISQ Quantities vs Custom Attributes
- **Check:** Did the code invent a custom attribute for a standard physical quantity? (e.g., `attribute def ElectricPower :> ISQ::power;`).
- **Correction:** Use standard ISQ quantities directly from the library (e.g., `ISQElectromagnetism::electricPower`) to avoid redundant abstractions and compilation errors.

### 6. Invalid Conjugation Imports
- **Check:** Are there imports of conjugated ports? (e.g., `import LogicalDesign::~UserSettings;`).
- **Correction:** Conjugation `~` is a modifier applied to a **usage**. You can never import or define a conjugated definition. Import the base port (`import LogicalDesign::UserSettings;`) and apply the tilde at usage: `port in : ~UserSettings;`.

### 7. Reserved Word Violations
- **Check:** Are any element names (parts, ports, blocks, connections) using reserved SysMLv2 keywords like `in`, `out`, `port`, `event`, `all`, `comment`, `state`, etc.?
- **Correction:** Rename them to be descriptive (e.g., change `port in` to `port powerIn`).

### 8. Multiple Connection Targets
- **Check:** Does a single `connect` statement have multiple targets? (e.g., `connect A to B, C;`).
- **Correction:** Split into distinct statements:
  ```sysml
  connect A to B;
  connect A to C;
  ```

### 9. Exhibit State Bindings
- **Check:** Is `:>>` being used to bind attributes inside an `exhibit state` block?
- **Correction:** Use the `bind` keyword: `bind attribute = externalAttribute;`.

### 10. Comment Blocks
- **Check:** Are `//` comments used anywhere?
- **Correction:** SysMLv2 documentation and requirements must use block comments: `doc /* ... */`. Standard inline comments must use `/* ... */`. Never use `//`.

### 15. CollectionFunctions prefix usage
- **Check:** Is `KerML::CollectionFunctions::size(...)` used?  
- **Correction:** Remove `KerML::` prefix. Use `CollectionFunctions::size(...)` (or import the package and call `size(...)`).

### 16. Ordered/nonunique modifier placement
- **Check:** Are braces `{}` used around `ordered nonunique`?  
- **Correction:** Remove the braces. Write `[*] ordered nonunique` directly after the multiplicity.

### 17. Missing ScalarValues import for primitive types
- **Check:** Is `Boolean`, `Real`, `Integer`, or `String` used without a `ScalarValues::*` import in the enclosing package?  
- **Correction:** Add `private import ScalarValues::*;` at the top of the package.

## Final Output Protocol

When validation is complete, output the corrected SysMLv2 code. Explicitly list out which of the above rules were violated (if any) and explain how you fixed them to ensure the user understands the corrections made.
