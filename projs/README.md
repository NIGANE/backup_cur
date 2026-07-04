*This project has been created as part of the 42 curriculum by amerkht.*

# Autonomous Drone Navigation Simulator

## Description

The Autonomous Drone Navigation Simulator is a Python application that models the movement of drones through a network of interconnected hubs. The simulation environment is defined by a configuration file describing the number of drones, the available hubs, the connections between them, and optional constraints such as hub capacities, restricted zones, priority zones, and connection bandwidth.

The project validates the input configuration, constructs an internal graph representation of the environment, computes one or more suitable routes from the starting hub to the destination hub, distributes drones across these routes, and simulates their movement while respecting all imposed constraints.

The objective is to efficiently deliver every drone to its destination while minimizing congestion and ensuring that all routing rules are respected.

---

## Features

- Configuration file parsing and validation
- Graph construction from configuration data
- Shortest-path computation
- Alternative path discovery
- Drone distribution across multiple paths
- Hub capacity management
- Connection bandwidth limitations
- Restricted and priority zone handling
- Turn-based simulation
- Colored terminal output
- Detailed error reporting

---

## Instructions

### Requirements

- Python 3.12 or later
- uv
- make

### Installation

Install dependencies:

```bash
uv sync
```
or
```bash
make install
```

### Execution

Run the simulator with:

```bash
uv run python -m main <configuration_file>
```

Example:

```bash
uv run python -m main examples/example.txt
```

---

## Configuration Format

Example configuration:

```txt
nb_drones: 5

start_hub: A 0 0
hub: B 1 0 [zone=restricted]
hub: C 2 0 [max_drones=2]
end_hub: D 3 0

connection: A-B
connection: B-C [max_link_capacity=2]
connection: C-D
```

---

## Algorithm Choices and Implementation Strategy

### Configuration Validation

The configuration file is processed sequentially. Each line is validated using regular expressions before being converted into domain objects.

Validation includes:

- malformed directives
- duplicate hubs
- duplicate connections
- duplicate start or destination hubs
- invalid coordinates
- invalid capacities
- invalid colors
- invalid zone types
- missing required directives
- unknown hub references

Any validation failure immediately stops execution with a descriptive error message.

---

### Graph Representation

The simulation environment is represented as a graph.

Each hub corresponds to a vertex while every connection represents an edge.

Each hub stores:

- neighboring hubs
- traversal cost
- occupancy
- capacity
- zone type
- visitation state
- relaxation value

This representation allows efficient path-finding while remaining easy to extend.

---

### Path Finding

The routing algorithm is based on graph relaxation.

Beginning at the starting hub, traversal costs are propagated through neighboring hubs until the minimum cost for every reachable hub has been computed.

Traversal costs depend on the zone type:

- Normal zones have the default cost.
- Restricted zones receive a higher traversal cost.
- Priority zones receive a highly favorable relaxation value, encouraging the algorithm to select routes passing through them.

Once the shortest path has been reconstructed using predecessor links, additional candidate paths are discovered by temporarily increasing the cost of previously selected paths. This encourages the algorithm to explore alternative routes.

The discovered paths are then filtered according to:

- total traversal cost
- path length

This produces several efficient routes suitable for distributing drones across the network.

---

### Drone Distribution

Instead of assigning every drone to the same route, drones are distributed across the available paths using a round-robin strategy.

This simple scheduling policy reduces congestion while improving overall throughput.

---

### Simulation

The simulator executes in discrete turns.

For every drone during each turn:

1. verify that the destination hub has available capacity;
2. verify that the connection has remaining bandwidth;
3. reserve restricted hubs when required;
4. move the drone to the next hub;
5. record the movement for display.

Connection bandwidth counters are reset after every turn.

The simulation terminates once every drone reaches the destination.

---

## Visual Representation

The simulator provides a textual visualization of the simulation in real time.

Each simulation turn prints the drones that moved during that turn together with their next position. Colored hub names improve readability by making different hub categories easier to identify.
`

Visual features include:

- colored hub names;
- movement tracking;
- restricted-zone indication;
- turn-by-turn simulation output;
- total simulation turns upon completion.

These features help users understand routing decisions, monitor congestion, and follow the progression of every drone throughout the simulation.

---


---

## Resources

### Documentation

- Python Documentation — https://docs.python.org/3/
- PEP 8 — https://peps.python.org/pep-0008/
- PEP 257 — https://peps.python.org/pep-0257/
- Python `re` module documentation
- Colorama documentation

### Graph Algorithms

- Dijkstra's Algorithm
- Graph Relaxation
- Breadth-First Search (BFS)

### AI Usage

Artificial intelligence (ChatGPT) was used as a development assistant during this project. It was primarily used for:

- explaining Python language features;
- reviewing implementation ideas;
- improving code readability;
- generating Google-style docstrings;
- reviewing documentation;
- discussing algorithmic approaches;
- identifying edge cases;
- suggesting naming improvements.

All architectural decisions, implementation, debugging, testing, and validation of the final solution were performed by the project author(s).

---

## Authors

- amerkht