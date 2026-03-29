# Long Lost Friends

An AI pathfinding project that uses search algorithms to navigate a maze and find multiple agents (A, B, C, D) scattered across a grid map.

## Problem Description

The map consists of a grid where:
- `w` — walkable cell (open path)
- `b` — blocked cell (wall/obstacle)
- `A` — starting agent (robot)
- `B`, `C`, `D` — target agents to find

The goal is for agent `A` to find and reach the other lost friends (B, C, D) navigating through the maze while avoiding blocked cells.

## Map Format

The map is defined in `sources.txt` as a comma-separated grid. Example:

```
b,b,B,w,w,w,w
w,w,w,w,w,b,b
w,b,w,w,w,C,w
w,w,w,b,w,b,w
w,w,w,b,w,b,w
b,w,b,w,w,b,w
b,w,b,w,b,b,w
w,A,w,w,w,D,w
```

## Project Structure

```
Long-Lost-Friends/
├── main.py          # Core logic: map parsing, movement, and search algorithm
├── sources.txt      # Grid map definition
└── AI_Assignment1.pdf  # Assignment specification
```

## How It Works

1. **Map Parsing** — `get_map()` reads `sources.txt` and loads the grid
2. **Map Construction** — `construct_map()` converts the raw grid into a structured maze representation
3. **Movement Functions** — `move_upwards()`, `move_downwards()`, `move_leftwards()`, `move_rightwards()` generate next states from a given path
4. **Path Extension** — `extend_path()` expands a path in all four directions
5. **Search** — `A_search()` implements a BFS-based search to locate agents B, C, D starting from A
6. **Heuristic** — `get_estimated_remaining_distance()` computes Manhattan distance to a target for informed search

## Requirements

- Python 3.x
- `numpy`

Install dependencies:

```bash
pip install numpy
```

## Running

```bash
python main.py
```

## Algorithm

The search uses a queue-based (BFS) traversal. Each path is represented as a list of nodes:

```
path = [[x1, y1, cost], [x2, y2, cost], ...]
```

The heuristic uses **Manhattan distance** to estimate the remaining distance to a target agent, supporting an A\*-style informed search.

## Status

Work in progress — `construct_map` and `A_search` are partially implemented.
