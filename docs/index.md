# Protocol Activity Modeling Language

PAML (Protocol Activity Modeling Language) uses the UML Activity Model to represent protocols.

UML defines concepts Behavior, Event and Trigger that are used in modeling behavior.
A Behavior models dynamic change, and UML has three forms of behavioral model, one of which is the activity model.
Basic concepts of behavioral modeling are described in section 13 of the UML specification.

An activity model describes the data and control flow among executable atomic behaviors called actions.
The model is a graph with nodes for actions, objects (e.g., data) and control, and edges representing flow of objects and control. Control nodes determine when actions are performed.
In the UML specification, Activities are defined in section 15, and actions in section 16.

> This document uses [mermaid-js](https://mermaid-js.github.io/mermaid/#/) notation for class diagrams,
> You may need to enable mermaid in your viewer to see them properly.

## Protocols

A protocol is an activity with a list of materials, and input/output parameters determined by the activity.

```mermaid
classDiagram
    Protocol "1" --> "*" EntitySpecification : materials
    Protocol "1" --> "*" Activity
```

For the protocol to be well-formed, the materials must each have a corresponding `ProvisionAction` within the activity.

## Activities

We adopt the UML activity model as a whole with specified exclusions and extensions.

This model is defined in Sections 15 and 16 of the UML specification along with concepts defined in other sections.
This portion of the UML specification should be treated as the primary definition of the activity model.

### Behaviors

A Behavior is an abstract activity with inputs and outputs and pre- and post-conditions. Inputs and Outputs are either Object nodes in the activity graph, or the input/output pins of an action.

```mermaid
classDiagram
    Behavior <|-- Activity
    Behavior "1" --> "*" Parameter : inputs
    Behavior "1" --> "*" Parameter : outputs
    Parameter : +String default
    Parameter : +ParameterDirectionKind direction
    Behavior --> Constraint : precondition
    Behavior --> Constraint : postcondition
```

### Graph

An Activity consists of the activity graph nodes and edges.
Each edge may have a guard, which is a BLAH, and a weight, which is a BLAH.

```mermaid
classDiagram
    Activity "1" --> "*" ActivityNode
    Activity "1" --> "*" ActivityEdge
    ActivityEdge --> ActivityNode : source
    ActivityNode --> ActivityEdge : incoming
    ActivityEdge --> ActivityNode : target
    ActivityNode --> ActivityEdge : outgoing
```

```mermaid
classDiagram
    ActivityNode <|-- ControlNode
    ActivityNode <|-- ObjectNode
    ObjectNode <|-- ActivityParameterNode
    ActivityParameterNode --> Parameter
```

```mermaid
classDiagram
    ActivityEdge <|-- ControlFlow
    ActivityEdge <|-- ObjectFlow
```

### Control

```mermaid
classDiagram
    ControlNode <|-- Initial
    ControlNode <|-- Final
    Final <|-- FlowFinal
    Final <|-- ActivityFinal
    ControlNode <|-- Fork
    ControlNode <|-- Join
    ControlNode <|-- Merge
    ControlNode <|-- Decision
```

### Action

```mermaid
classDiagram
    ActivityNode <|-- ExecutableNode
    ExecutableNode --> ExceptionHandler : handler
    Element <|-- ExceptionHandler
    ExceptionHandler --> ObjectNode : exception_input
    ExceptionHandler --> Classifier : exception_type
```

```mermaid
classDiagram
    ExecutableNode <|-- Action
    Action --> InputPin : inputs
    Action --> OutputPin : outputs
    Action --> Constraint : precondition
    Action --> Constraint : postcondition
```

```mermaid
classDiagram
    ObjectNode <|-- Pin
    Pin <|-- InputPin
    Pin <|-- OutputPin
    InputPin <|-- ValuePin
    ValuePin --> ValueSpecification
```

### Invocation

```mermaid
classDiagram
    Action <|-- InvocationAction
```

### Object

```mermaid
classDiagram
    Type <|-- ContainerType
    Type <|-- ItemType
    ItemType --> ContainerType
    ItemType <|-- CollectionType
    CollectionType "1" --> "n" SingleItemTypes : part_types
    ItemType <|-- SingleItemType
    SingleItemType --> SampleType
    Type <|-- PhysicalStateType
    Type <|-- SampleType
    SampleType <|-- CompositeSampleType
    CompositeSampleType "1" --> "n" SampleType : component_types
```

```mermaid
classDiagram
    Object --> Type
    Object <|-- Entity
    Object <|-- Container
    Object <|-- Value
    Entity <|-- Collection
    Entity --> Container
    Collection --> SingleEntity : parts
    Entity <|-- SingleEntity
    SingleEntity --> Sample
    SingleEntity --> PhysicalState
    Sample <|-- CompositeSample
    CompositeSample "1" --> "n" Sample : components
```
