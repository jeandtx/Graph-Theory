
def has_predecessors(etat, contraintes):
    for c in contraintes:
        if etat in c[2:]:
            return True
    return False


def a_pred(constraint, constraints):
    for c in constraints:
        if constraint[0] in c[2:]:
            return True
    return False


def est_contrainte_binaire(constraint):

    return len(constraint) == 2

def add_zero_to_constraints(constraints):
    new_constraints = []
    for constraint in constraints:
        if len(constraint) == 2:
            new_constraint = [constraint[0], constraint[1], 0]
        else:
            new_constraint = constraint
        new_constraints.append(new_constraint)
    return new_constraints

def ajouter_contrainte_zero(contraintes):
    contraintes.insert(0, [0, 0, 0])
    return contraintes

def add_final_constraint(constraints):
    predecessors = set()
    for constraint in constraints:
        for pred in constraint[2:]:
            predecessors.add(pred)
    if predecessors:
        final_constraint = [len(constraints), 0] + list(set(range(len(constraints))) - predecessors)
    else:
        final_constraint = [len(constraints), 0] + list(range(len(constraints)-1))
    constraints.append(final_constraint)
    return constraints


def count_constraints(constraints):
    return len(constraints)


def count_predecessors(constraints):
    num_predecessors = 0
    for constraint in constraints[1:]:
        num_predecessors += len(constraint[2:])
    return num_predecessors



def jeu_de_triplets(constraints):

    print(count_constraints(constraints)," sommets")
    print(count_predecessors(constraints)," arcs")
    n = len(constraints)

    # On commence par créer un dictionnaire pour stocker les durées de chaque contrainte
    durations = {}
    for constraint in constraints:
        durations[constraint[0]] = constraint[1]

    # On crée une liste pour stocker toutes les contraintes sauf la première
    all_constraints = []

    # Ensuite, on parcourt les contraintes une à une et on les ajoute à la liste
    for i in range(1, n):
        for j in constraints[i][2:]:
            if j != i:
                all_constraints.append((j, i, durations[j]))
        if i in constraints[i][2:]:
            all_constraints.append((i, i, durations[i]))

    # On trie la liste en fonction des durées des contraintes
    sorted_constraints = sorted(all_constraints, key=lambda x: x[2])

    # On affiche les contraintes dans l'ordre trié
    for constraint in sorted_constraints:
        print(f"{constraint[0]} -> {constraint[1]} = {constraint[2]}")


def generate_values_matrix(constraints):
    n = len(constraints)

    # On commence par créer un dictionnaire pour stocker les durées de chaque contrainte
    durations = {}
    for constraint in constraints:
        durations[constraint[0]] = constraint[1]

    # On crée une matrice d'adjacence pour stocker les contraintes
    matrix = [[None] * n for _ in range(n)]

    # Ensuite, on parcourt les contraintes une à une et on les ajoute à la matrice d'adjacence
    for i in range(1, n):
        for j in constraints[i][2:]:
            if j != i:
                matrix[j][i] = durations[j]
        if i in constraints[i][2:]:
            matrix[i][i] = durations[i]

    return matrix

def print_values_matrix(matrix, constraints):
    print("\n\n")
    n = len(constraints)
    # On affiche la matrice d'adjacence sous forme de tableau
    print("  ", "   ".join(str(i) for i in range(n)))
    for i in range(n):
        print(i, end="  ")
        for j in range(n):

            if matrix[i][j] is None:
                print("*", end="   ")
            else:
                print(matrix[i][j], end="   ")
        print()


def check_first_diagonal(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] is not None:
            return True
    return False


def single_entry(constraints):
    entry_count = 0
    entry_constraint = None
    for constraint in constraints:
        if 0 in constraint[2:]:
            entry_count += 1
            entry_constraint = constraint[0]
    if entry_count == 1:
        return entry_constraint
    else:
        return None

def single_exit(constraints):
    exit_count = 0
    exit_constraint = None
    for constraint in constraints:
        if len(constraint[2:]) == 0:
            exit_count += 1
            exit_constraint = constraint[0]
    if exit_count == 1:
        return exit_constraint
    else:
        return None


def constraint_exists(constraints, constraint_num):
    for constraint in constraints:
        if constraint[0] == constraint_num:
            return True
    return False

def find_input_output(constraints):

    last_constraint = count_constraints(new_constraints) - 1
    if (constraint_exists(constraints, 0) == True) :
        print("There is only one entry point", 0)
    if (constraint_exists(constraints, last_constraint) == True) :
        print("There is only one exit point", last_constraint)



"""------------------------------------------------------------------"""



constraintes = [[1, 1, 3], [2, 2], [3, 3, 1], [4, 4, 1, 2], [5, 5, 2, 4]]
new_constraints = add_zero_to_constraints(constraintes)
new_constraints = ajouter_contrainte_zero(new_constraints)
new_constraints = add_final_constraint(new_constraints)

print("\n\n",new_constraints,"\n\n")

jeu_de_triplets(new_constraints)

matrix = generate_values_matrix(new_constraints)

print_values_matrix(matrix, new_constraints)

print("\n",check_first_diagonal(matrix))

print(matrix)

find_input_output(new_constraints)