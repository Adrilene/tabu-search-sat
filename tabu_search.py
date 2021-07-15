import copy
from configuration import nmax, delta_to_intensficate
from neighborhood import generate_neighborhood
from diversification import generate_diversed_neighbors
from intensification import generate_closer_neighbors
from utils import update_tabu, aspiration, assignment


def tabu_search(initial_solution, clauses, range_literal):
    current_solution = copy.deepcopy(initial_solution)
    current_value = assignment(current_solution[0], clauses)
    tabu_queue = []
    count = 1
    count_repetitive_solution = 0
    is_intesificated = False
    previous_value = 0
    M = 1

    while count < nmax:
        # while 100:

        if (
            len(clauses) - current_value <= delta_to_intensficate
            and not is_intesificated
        ):
            neighborhood = generate_closer_neighbors(current_solution[0])
            is_intesificated = True
            open("log.txt", "a").write("Intesified\n")

        else:
            if count_repetitive_solution < 50:
                neighborhood = generate_neighborhood(current_solution, range_literal)
            else:
                neighborhood = generate_diversed_neighbors(
                    current_solution, range_literal
                )
                open("log.txt", "a").write("Diversed\n")
                is_intesificated = False

        neighborhood_values = [
            assignment(neighborhood[i][0], clauses) for i in range(len(neighborhood))
        ]
        max_index = neighborhood_values.index(
            max(neighborhood_values)
        )  # Index do melhor vizinho
        best_solution = neighborhood[max_index]
        if (max(neighborhood_values)) == len(clauses):
            current_solution = best_solution
            previous_value = current_value
            current_value = max(neighborhood_values)
            break

        while True:
            # check if all elements have been visited
            open("log.txt", "a").write(
                f"count: {count} | max_neighborhood_values: {max(neighborhood_values)} \n"
            )
            if sorted(best_solution[1]) in tabu_queue:
                ## TODO: change logic for accept
                if aspiration(max(neighborhood_values), current_value):
                    current_solution = best_solution
                    previous_value = current_value
                    current_value = max(neighborhood_values)
                    M = count
                    break
                else:
                    neighborhood_values[max_index] = 0
                    max_index = neighborhood_values.index(max(neighborhood_values))
                    best_solution = neighborhood[max_index]
            else:
                current_solution = best_solution
                previous_value = current_value
                current_value = max(neighborhood_values)
                tabu_queue = update_tabu(tabu_queue, best_solution[1])
                M = count
                break

        if current_value == previous_value:
            count_repetitive_solution += 1
        else:
            count_repetitive_solution = 0
        count += 1

    return current_solution[0], current_value
