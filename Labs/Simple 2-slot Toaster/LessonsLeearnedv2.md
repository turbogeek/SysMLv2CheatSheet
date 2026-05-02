# SysML v2 AI Agent Skill / Comprehensive Reference

**Generated on:** 2026-04-26 15:55:49

---

# SysML v2.0 Language Reference
... (the rest of the original skill.md remains unchanged up to the Best Practices section) ...

---

## 8. BEST PRACTICES (Expanded)

1. **Use Definitions as Templates**: Create reusable definitions, specialize in usages.
2. **Leverage Standard Libraries**: Import and use standard types and units.
3. **Document Requirements**: Use doc comments for requirement text.
4. **Use Short Names for IDs**: Provide requirement IDs with short names.
5. **Organize with Packages**: Structure models into logical packages.
6. **Type Everything**: Explicitly type features for clarity.
7. **Use Ports for Interactions**: Model interactions through ports and interfaces.
8. **Separate Structure and Behavior**: Parts for structure, actions/states for behavior.
9. **Frame Concerns**: Use concerns to capture stakeholder needs.
10. **Verify Requirements**: Create verification cases for requirements.

---

## Additional Modeling Rules from Iterative Corrections (Toaster Example)

*These rules were derived from errors encountered and corrected during the development of a complete toaster model. They supplement the existing best practices and must be followed to avoid similar issues.*

- **System Subject for Use Cases**  
  The subject of a use case (and often the top‑level system) must be a `part def` (e.g., `part def ToasterSystemRoot`). Never use an undefined name.

- **Quoting of Special Characters in Units**  
  When a unit symbol contains characters that are not alphanumeric or underscore, enclose it in single‑quoted square brackets: `['°C']`. Unquoted versions like `[°C]` may be misinterpreted.

- **Prefer Standard ISQ Quantities**  
  Avoid inventing custom attribute definitions for physical quantities when a suitable ISQ quantity exists. For example, use `ISQElectromagnetism::electricPower` rather than `attribute def ElectricPower :> ISQ::power`. This ensures interoperability and reduces redundant definitions.

- **Conjugation is a Usage Modifier, not a Definition**  
  Never import a conjugated port definition (e.g., `private import LogicalDesign::~UserSettings`). Conjugation (`~`) is applied to a usage of a port, not to the definition. Always import the base port definition and write `~PortDef` where needed in usage contexts.

- **Complete Definition of Referenced Elements**  
  Every port, part, attribute, or action that is referenced must have a corresponding definition. For example, `wallPlug` must be declared as a port of the enclosing part, and every action in a state machine effect (like `StopHeatingAction`) must be defined (as `action def`).

- **Exhibit State Bindings**  
  Inside an `exhibit state` clause, use `bind attribute = externalAttribute;` to connect the state machine’s attributes to the owning part’s attributes. Do **not** use attribute redefinition (`:>>`) for this purpose.

- **Avoid Reserved Words in Port Names**  
  Port names such as `in`, `out`, `port`, `event`, etc., clash with keywords. Use longer descriptive names like `inPower`, `outPower`, `powerIn`, `powerOut`. This applies even to simple physical ports.

- **Multiple Connection Targets**  
  The `connect` statement accepts exactly one source and one target. To connect a single source to multiple destinations, use separate `connect` statements. For example:
  ```sysml
  connect timer.outputContacts to innerElements.powerIn;
  connect timer.outputContacts to outerElements.powerIn;