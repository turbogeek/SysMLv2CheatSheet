# Graphical Cheat Sheet

*Standard Graphical Notation*

## 1. Nodes

## Part Definition

![Part Definition](assets/symbols/light/PartDefinition.svg)

**Notation**: Rectangle: 'part def'

**Syntax**: `part def Name;`

**Example**: `part def Vehicle;`

## Part Usage

![Part Usage](assets/symbols/light/PartUsage.svg)

**Notation**: Rounded Rect: 'part'

**Syntax**: `part name : Type;`

**Example**: `part engine : Engine;`

## Action Definition

![Action Definition](assets/symbols/light/ActionDefinition.svg)

**Notation**: Rectangle: 'action def'

**Syntax**: `action def Name;`

**Example**: `action def Drive;`

## Action Usage

![Action Usage](assets/symbols/light/ActionUsage.svg)

**Notation**: Rounded Rect: 'action'

**Syntax**: `action name : Type;`

**Example**: `action drive : Drive;`

## Requirement Def

![Requirement Def](assets/symbols/light/RequirementDef.svg)

**Notation**: Rectangle: 'requirement def'

**Syntax**: `requirement def Name;`

**Example**: `requirement def Perf;`

## Requirement Usage

![Requirement Usage](assets/symbols/light/RequirementUsage.svg)

**Notation**: Rounded Rect: 'requirement'

**Syntax**: `requirement name : Type;`

**Example**: `requirement req1 : Perf;`

## State Definition

![State Definition](assets/symbols/light/StateDefinition.svg)

**Notation**: Rectangle: 'state def'

**Syntax**: `state def Name;`

**Example**: `state def Idle;`

## State Usage

![State Usage](assets/symbols/light/StateUsage.svg)

**Notation**: Rounded Rect: 'state'

**Syntax**: `state name;`

**Example**: `state off;`

## 2. Relationships

## Specialization

![Specialization](assets/symbols/light/Specialization.svg)

**Notation**: Solid line, hollow triangle

**Syntax**: `def A :> B;`

**Example**: `part def Car :> Vehicle;`

## Composition

![Composition](assets/symbols/light/Composition.svg)

**Notation**: Solid line, filled diamond

**Syntax**: `part name : Type;`

**Example**: `part wheel : Wheel;`

## Reference

![Reference](assets/symbols/light/Reference.svg)

**Notation**: Solid line, hollow diamond

**Syntax**: `ref part name : Type;`

**Example**: `ref part driver : Person;`

## Import

![Import](assets/symbols/light/Import.svg)

**Notation**: Dashed line, open arrow

**Syntax**: `import Package::*;`

**Example**: `import SI::*;`

## Binding

![Binding](assets/symbols/light/Binding.svg)

**Notation**: Solid line, «bind»

**Syntax**: `bind a = b;`

**Example**: `bind p1 = p2;`

## Succession

![Succession](assets/symbols/light/Succession.svg)

**Notation**: Dashed line, open arrow

**Syntax**: `first a then b;`

**Example**: `first start then stop;`

