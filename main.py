def number_entry_point(graph):
    """
    Checks the number of entry points.
    Entry point means a vertex with no incoming edges.

    This function checks for all the vertices in the graph if they are in the list of all outgoing edges.
    If they are not, then they are entry points.
    """
    ctr = 0
    for entry_point in graph["graph"]:
        if entry_point not in graph["all_outgoing_edges"]:
            ctr += 1
    return ctr

def number_exit_point(graph):
    """
    Checks the number of exit points.
    Exit point means that a vertex has no outgoing edges.

    This function checks the outgoing edges of each vertex in the graph.
    If the list of outgoing edges is empty, then the vertex is an exit point.
    """
    ctr = 0
    for vertices in graph["graph"]:
        if graph["graph"][vertices]["outgoing_edges"] == []:
            ctr += 1
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
            matrix[vertices-1][outgoing_edges-1] = 1
    return matrix

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

    for i in matrix:
        ctr = 0
        for j in range(len(i)):
            if i[j] == 0:
                ctr += 1
        if ctr == len(i):
            matrix.remove(i)
            # this line deletes the corresponding row
            matrix = [row[:j] + row[j+1:] for row in matrix]
            # this line deletes the corresponding column
            return cycles(matrix)
    if not matrix:
        return False
    else:
        return True


    

if __name__ == "__main__":
    display_table(table) 

    build_graph(table)

    # Checking that this graph satisfies all the properties necessary for it to be a scheduling graph:
    no_cycles(table)
    same_weight_for_all_outgoing_edges_of_a_vertex(table)
    outgoing_edges_of_entry_point_have_weight_0(table)
    no_negative_edges(table)

    rank(vertices)

    earliest_date(table)
    latest_date(table)
    floats(table) # Floats are the tasks that can be delayed without delaying the project. (COPILOT)

    compute_critical_path(table)
    display_critical_path(table)


    # // TODO Create interface, see algorithm in subject
    # // TODO Create execution trace, see algorithm in subject