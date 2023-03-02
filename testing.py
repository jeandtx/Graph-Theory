from main import *

# Data structure for the graph:
graph = {
    "graph": {
        1: {
            "weight": 0,
            "outgoing_edges": [2, 3]
        },
        2: {
            "weight": 0,
            "outgoing_edges": [3, 2]
        },
        3: {
            "weight": 5,
            "outgoing_edges": [3, 4]
        }, 
        4: {
            "weight": 0,
            "outgoing_edges": []
        }
    },
    "all_outgoing_edges": [2, 3, 3, 2, 3, 4]
}


print("Graph presentation:")
for i in graph["graph"]:
    print(i, graph["graph"][i]["outgoing_edges"])
# print("Matrix presentation:")
# matrix = graph_to_matrix(graph)
# for i in matrix:
#     print(i)

matrix = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
print('cycles:', cycles(matrix))