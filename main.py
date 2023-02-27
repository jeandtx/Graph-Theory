
# Data structure for the graph:
graph = {
    "entry_point": {
        "weight": 0,
        "outgoing_edges": ["A", "B"]
    },
    "A": {
        "weight": 5,
        "outgoing_edges": ["C"]
    },
}

if __name__ == "__main__":
    print("Hello World")

    table = read_table("table.txt")
    display_table(table) 

    build_graph(table)

    # Checking that this graph satisfies all the properties necessary for it to be a scheduling graph:
    single_entry_point(table)
    single_exit_point(table)
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