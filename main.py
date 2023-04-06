def import_graph(filename):
    """
    This function convert a .txt constraint table to a graph under a python dictionary.
    """
    graph = {"graph": {}, "all_outgoing_edges": []}
    with open('./data/' + filename + '.txt', "r") as file:
        data = file.readlines()
    oe = []
    for i in data:
        if len(i) < 6:
            oe.append(int(i[0]))
    graph["graph"][0] = {"weight": 0, "outgoing_edges": oe}#find_entry_points(graph)}
    for i in range(0, len(data)):
        # Clean the data from empty strings and convert to int
        data[i] = data[i].replace('\n', '')
        data[i] = data[i].split(' ')
        if '' in data[i]: data[i].remove('')
        data[i] = [int(x) for x in data[i]]

        graph["all_outgoing_edges"].extend(data[i][2:])

        graph["graph"][i+1] = {"weight": data[i][1], "outgoing_edges": []}
    for i in data:
        for j in i[2:]:
            graph["graph"][j]["outgoing_edges"].append(i[0])
    for vertices in graph["graph"]:
        if graph["graph"][vertices]["outgoing_edges"] == []:
            graph["graph"][vertices]["outgoing_edges"] = [len(data)+1]
    graph["graph"][len(data)+1] = {"weight": 0, "outgoing_edges": []}
    return graph

def display_graph(graph):
    """
    Displays the graph in triplet form.
    """
    print("Creating the scheduling graph:")
    print(len(graph["graph"]), "vertices")
    print(len(graph["all_outgoing_edges"]), "edges")
    for vertices in graph["graph"]:
        for outgoing_edges in graph["graph"][vertices]["outgoing_edges"]:
            print(vertices, "->", outgoing_edges, "=", graph["graph"][vertices]["weight"])

def entry_points(graph):
    """
    Checks the number of entry points.
    Entry point means a vertex with no incoming edges.
    """
    return graph["graph"][0]["outgoing_edges"]

def exit_points(graph):
    """
    Checks the number of exit points.
    Exit point means that a vertex has no outgoing edges.

    This function checks the outgoing edges of each vertex in the graph.
    If the list of outgoing edges is empty, then the vertex is an exit point.
    """
    ctr = []
    for vertices in graph["graph"]:
        if graph["graph"][vertices]["outgoing_edges"] == [len(graph["graph"]) - 1]:
            ctr.append(vertices)
    return ctr

def graph_to_matrix(graph):
    """
    Converts the graph to a matrix.

    The matrix is a 2D array where the rows are the vertices and the columns are the outgoing edges.
    1 if the vertex (row) has an outgoing edge to the vertex (column).
    """
    # create 2D empty array
    matrix = [[0 for _ in range(len(graph["graph"]))] for _ in range(len(graph["graph"]))]
    for vertices in graph["graph"]:
        for outgoing_edges in graph["graph"][vertices]["outgoing_edges"]:
            matrix[vertices][outgoing_edges] = graph["graph"][vertices]["weight"]
    return matrix

def display_matrix(matrix):
    """
    Displays the matrix in a nice format.
    """
    n = len(matrix[0])
    print("\n\t", "\t".join(str(i) for i in range(n)))
    for i in range(n):
        print(i, end="\t")
        for j in range(n):
            if matrix[i][j] == 0:
                print("", end="\t")
            else:
                print(matrix[i][j], end="\t")
        print()

def cycles(matrix):
    """
    Checks that the graph has no cycles.

	for each colunms:
        if column is empty:
            delete colunm and corresponding row
            return detect_cycle(matrix)
	if matrix is empty:
			return "no cycle"
    else 
        return "cycle detected"
    """
    if not matrix:
        return False
    for j in range(len(matrix)):
        if not any(matrix[i][j] for i in range(len(matrix))):
            for i in range(len(matrix)):
                del matrix[i][j]
            del matrix[j]
            return cycles(matrix)
    return True

    

if __name__ == "__main__":
    no_negative_edges(table)

    rank(vertices)

    earliest_date(table)
    latest_date(table)
    floats(table) # Floats are the tasks that can be delayed without delaying the project. (COPILOT)

    compute_critical_path(table)
    display_critical_path(table)


    # // TODO Create interface, see algorithm in subject
    # // TODO Create execution trace, see algorithm in subject