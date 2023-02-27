# Python Project - Graph Theory Algorithms

This project aims to implement various graph theory algorithms using Python programming language. Graph Theory is the study of mathematical structures used to model pairwise relations between objects. It has many applications in computer science such as computer networks, social networks, transportation networks, etc.

## Algorithms Implemented

The following graph theory algorithms were implemented in this project:

-   Breadth First Search (BFS)
-   Depth First Search (DFS)
-   Dijkstra's Algorithm
-   Bellman-Ford Algorithm
-   Floyd-Warshall Algorithm
-   Kruskal's Algorithm
-   Prim's Algorithm

## Requirements

-   Python 3.x
-   NetworkX library

## Installation

1. Clone the repository: `git clone <https://github.com/username/repo.git`>
2. Install NetworkX library: `pip install networkx`

## Usage

1. Import the required algorithm from `graph_algorithms.py` module.
2. Create a graph using NetworkX library.
3. Call the algorithm function with the graph and required parameters as input.
4. The output will be the result of the algorithm.

## Examples

### Breadth First Search

```
from graph_algorithms import bfs

import networkx as nx

G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,4), (3,4), (3,5), (4,5)])

bfs(G, 1)

```

### Dijkstra's Algorithm

```
from graph_algorithms import dijkstra

import networkx as nx

G = nx.Graph()
G.add_weighted_edges_from([(1,2,5), (1,4,9), (1,5,2), (2,3,2), (3,4,3), (4,5,2)])

dijkstra(G, 1)

```

## Conclusion

This project provides a starting point for implementing various graph theory algorithms using Python programming language. The algorithms implemented in this project can be used as a reference for implementing other algorithms.
