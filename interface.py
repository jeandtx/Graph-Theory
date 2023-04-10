# importer toutes les fonctions depuis main.py
from main import *

def main():
    
    
    # get filename input from user
    filename = input("Enter filename: ")

    # load graph from file
    graph = import_graph(filename)

    while True:
        action = input("\nChoose an action to perform:\n1. Display the graph\n2. Compute the number of entry points\n3. Compute the number of exit points\n4. Convert the graph to a matrix\n5. Check if the graph has cycles\n6. Check if the graph has negative edges\n7. Compute ranks\n8. critical path\n9. Exit\n")

        if action == "1":
            display_graph(graph)
        elif action == "2":
            num_entry_points = entry_points(graph)
            log(f"The graph has {num_entry_points} entry point(s).")
        elif action == "3":
            num_exit_points = exit_points(graph)
            log(f"The graph has {num_exit_points} exit point(s).")
        elif action == "4":
            matrix = graph_to_matrix(graph)
            display_matrix(matrix)
        elif action == "5":
            if cycles(matrix):
                log("The graph has cycles.")
            else:
                log("The graph has no cycles.")
        elif action == "6":
            if negative_edges(graph):
                log ("The graph has negative edges.")
            else :
                log ("The graph has no negative edges.")
        elif action == "7":
            if cycles(graph_to_matrix(graph)):
                log("The graph has cycles. Cannot compute ranks.")
            else :
                display_ranks(compute_ranks(graph_to_matrix(graph)))

        elif action == "8":
            if cycles(graph_to_matrix(graph)):
                log("The graph has cycles. Cannot compute ranks.")
            else :
                log("floats", floats(earliest_date(graph)[0], latest_date(graph)[0]))
            
        elif action == "9":
            log("thanks for using our program :)")
            break
        else:
            log("Invalid input.")

        choice = input("\nDo you want to continue? (Y/N) ")
        if choice.lower() == "n":
            break
        else:
            log("Invalid choice. Try again.")

if __name__ == '__main__':
    main()