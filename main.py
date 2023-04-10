def log(*args, **kwargs):
    import time
    """
    This function is used to print to the console.
    AND to write to the log file.
    """
    print(*args, **kwargs)
    with open("log.log", "a") as f:
        current_time = time.strftime('%H:%M:%S', time.localtime())
        print(str(current_time), file=f, end= '  ')
        print(*args, **kwargs, file=f)

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
    log("Creating the scheduling graph:")
    log(len(graph["graph"]), "vertices")
    log(len(graph["all_outgoing_edges"]), "edges")
    for vertices in graph["graph"]:
        for outgoing_edges in graph["graph"][vertices]["outgoing_edges"]:
            log(vertices, "->", outgoing_edges, "=", graph["graph"][vertices]["weight"])

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
    if not matrix:
        log("Empty matrix")
        return
    n = len(matrix[0])
    log("\n\t", "\t".join(str(i) for i in range(n)))
    for i in range(n):
        log(i, end="\t")
        for j in range(n):
            if matrix[i][j] == 0:
                log("", end="\t")
            else:
                log(matrix[i][j], end="\t")
        log()

def cycles(matrix, display_steps=False):
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
    if display_steps:
        log("\n", "-"*50, "\n")
        display_matrix(matrix)
    for j in range(len(matrix)):
        if not any(matrix[i][j] for i in range(len(matrix))):
            for i in range(len(matrix)):
                del matrix[i][j]
            del matrix[j]
            return cycles(matrix)
    return True

def negative_edges(graph):
    """
    Checks that the graph has no negative edges.
    """
    for vertices in graph["graph"]:
        if graph["graph"][vertices]["weight"] < 0:
            return True
    return False

def compute_ranks(matrix):
    """
    This function compute the ranks of the graph and returns a list of lists.
    The first rank have only one element, the entry point.
    Then while the matrix is not empty, it finds the empty columns and delete them.
    The deleted columns are the vertices of the next rank.
    """
    ranks = [[0]]
    for i in range(len(matrix)):
        del matrix[i][0]
    del matrix[0]
    index = 1
    while matrix:
        rank = []
        # Find empty columns
        for j in range(len(matrix)):
            if not any(matrix[i][j] for i in range(len(matrix))):
                rank.append(j + index)
        # Delete empty columns
        for j in range(len(rank)):
            for i in range(len(matrix)):
                del matrix[i][rank[j] - j - index]
            del matrix[rank[j] - j - index]
        index += len(rank)
        ranks.append(rank)
    return ranks

def display_ranks(ranks):
    log("\nRanks:")
    for i in range(len(ranks)):
        log("Rank", i, ":", ranks[i])

def earliest_date(graph):
    """
    Calculates the earliest date of a graph.
    It loop through the ranks and for each rank, it loops through the vertices.
    For each vertex, it loops through the outgoing edges and updates the earliest date of the outgoing edges.
    It appends the weight + the minimum of the earliest dates of the incoming edges.
    and returns the earliest date of the last vertex.
    """
    if negative_edges(graph):
        return "Error: negative edges"
    if cycles(graph_to_matrix(graph)):
        return "Error: cycles"

    time = [[0] for _ in range(len(graph_to_matrix(graph)))]
    for rank in compute_ranks(graph_to_matrix(graph)):
        for vertex in rank:
            for outgoing in graph["graph"][vertex]["outgoing_edges"]:
                if vertex == 0:
                    time[outgoing].append(graph["graph"][vertex]["weight"])
                else:
                    time[outgoing].append(max(time[vertex]) + graph["graph"][vertex]["weight"])
    output = [max(time[i]) for i in range(len(time))]
    return output, time[-1], time

def latest_date(graph):
    """
    Calculates the latest date of a graph
    """
    if negative_edges(graph):
        return "Error: negative edges"
    if cycles(graph_to_matrix(graph)):
        return "Error: cycles"
    earliest, _, earliest_larged= earliest_date(graph)
    time = [[0] for _ in range(len(graph_to_matrix(graph)))]
    time[-1] = [earliest[-1]]
    for rank in reversed(compute_ranks(graph_to_matrix(graph))):
        for vertex in rank:
            for outgoing in graph["graph"][vertex]["outgoing_edges"]:
                time[vertex].append(earliest_larged[outgoing][-1] - graph["graph"][vertex]["weight"])
                del earliest_larged[outgoing][-1]
    output = [time[i][-1] for i in range(len(time))]
    return output, time[0], time

def floats(earliest, latest):
    """
    Compute the floats of a graph. by subtracting the earliest date from the latest date.
    """
    floats = [latest[i] - earliest[i] for i in range(len(earliest))]
    return floats

def critical_path(floats):
    output = []
    for i in range(len(floats)):
        if floats[i] == 0:
            output.append(i)
    return output