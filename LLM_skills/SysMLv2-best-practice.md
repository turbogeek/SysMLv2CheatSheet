# SysML v2 Best Practices (repository conventions)

Practical rules for authoring SysML v2 textual models in this toolchain (standalone
validator + live CATIA Magic / Cameo). These complement the syntax rules in `skill.md`.

## Structure

1. **One root package per file.** Keep exactly one package at the root of the file's
   namespace; nest helper packages (math extensions, libraries) inside it. CATIA Magic
   names the imported namespace after the FIRST root element in the containment tree, so a
   single named root package gives a clean, predictable name. Avoid sibling root packages
   or a leading bare comment as the first element. Put the file overview in the root
   package's `doc`.
2. **`private import` only and placed inside the package.** Plain `import` and `public import`
   are forbidden (except to break circular dependencies). All imports (such as `ScalarValues::*`, 
   `ISQ::*`, `SI::*`) must be `private import` and must be placed *inside* each package/subpackage 
   definition (i.e., inside the folder/package scope) to prevent namespace leaks.
3. **Definition/usage discipline.** `def` classifies; usages apply. Don't use reserved
   words (`type`, `standard`, `interface`, `in`, `out`, …) as names.

## Documentation

4. **Element and package docs go INSIDE the element/package as `doc`.**
   - For elements: `attribute m : MassValue { doc /* … */ }`.
   - For packages/folders: The overview comment must be placed *inside* the package definition block and be preceded by the `doc` keyword (e.g., `package MyPackage { doc /* description */ ... }`). Plain comments outside or before the package definition block do not associate with the package in the model AST and are discouraged.
5. **One comment, not a stack.** A multi-line comment is a single `/* … */` block, never a
   column of one-line block comments. **Block comments do not nest** — never put a `*/`
   inside another `/* … */`.
6. **A group comment** (about several following lines, e.g. a section banner) is a single
   block comment placed above them.

## Calculations & missing math

7. **Calcs carry the math**, not a TODO comment — implement the expression in the body.
8. **`ln`, `exp`, and anything missing from the standard Kernel Function Library** are
   declared in a nested `MathExtensions` package as a `calc def` with a Groovy textual
   representation: `calc def ln { in x : Real[1]; return result : Real[1]; rep lnGroovy
   language "Groovy" /* result = Math.log(x) */ }`. (`sqrt`, `**`, `^` ARE available.) To
   invert the Breguet range equation for fuel sizing you need `exp`.

## Validation & the Cameo workflow

9. **Validate in BOTH** the standalone validator AND the live Cameo/Dassault plugin — the
   plugin is stricter (e.g. `satisfy` needs a requirement USAGE, not a `requirement def`).
   Treat a clean production-tool load as authoritative.
10. **Undo, don't pollute.** Each successful textual import commits into the open Cameo
    project. Before re-loading an edited version, UNDO the previous load (Cameo has full
    undo) or remove the previously-loaded packages; otherwise duplicate root packages
    accumulate and `import Foo::*` can resolve to a STALE earlier copy missing your new
    members. Prefer undo/cleanup over renaming packages to dodge the clash.

## Diagrams

11. **Provide proper diagrams, not just `view` elements.** A model with `view`/`viewpoint`
    elements isn't "diagrammed" until they're realized as actual diagrams in the tool.
    For a deliverable, generate the containment/package overview, a BDD-style definition
    view of the parts, an IBD-style internal view with ports & connections, requirement
    tables, and any state-machine/action diagrams.
12. **Filter library elements out of every `expose` view.** `expose` pulls in the imported
    standard-library / scope elements too, which render as clutter worthless to the reader.
    Add `filter not KerML::Root::Element::isLibraryElement;` inside every view that uses
    `expose` so the diagram shows only the model's own elements. (Other useful filters:
    `filter @RequirementUsage;` to keep one kind, `filter not (istype ViewUsage);` to drop
    the views themselves.)
