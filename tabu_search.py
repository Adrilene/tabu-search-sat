import copy
from configuration import nmax, delta_to_intensficate, repetitive_solution
from neighborhood import generate_neighborhood
from diversification import generate_diversed_neighbors
from intensification import generate_closer_neighbors
from utils import update_tabu, aspiration, assignment


def tabu_search(initial_solution, clauses, range_literal, optimal_value):
    current_solution = copy.deepcopy(initial_solution)
    current_value = assignment(current_solution[0], clauses)
    tabu_queue = []
    count = 1
    count_repetitive_solution = 0
    is_intesificated = False
    previous_value = 0
    qtd_strategy = {"Intesified": 0, "Diversed": 0}
    history = []

    while count < nmax:
        history.append(current_solution)
        if (
            len(clauses) - current_value <= delta_to_intensficate
            and not is_intesificated
        ):
            neighborhood = generate_closer_neighbors(current_solution[0])
            is_intesificated = True
            qtd_strategy["Intesified"] += 1

        else:
            if count_repetitive_solution < repetitive_solution:
                neighborhood = generate_neighborhood(current_solution, range_literal)
            else:
                neighborhood, history = generate_diversed_neighbors(
                    history, range_literal, current_value, clauses
                )
                qtd_strategy["Diversed"] += 1
                is_intesificated = False

        neighborhood_values = [
            assignment(neighborhood[i][0], clauses) for i in range(len(neighborhood))
        ]
        max_index = neighborhood_values.index(max(neighborhood_values))
        best_solution = neighborhood[max_index]

        # test if optimal value was reached
        if (max(neighborhood_values)) == optimal_value:
            current_solution = best_solution
            previous_value = current_value
            current_value = max(neighborhood_values)
            break

        while True:
            open("log.csv", "a").write(
                f"{count}; {list(map(int, current_solution[0]))}; {current_value}\n"
            )
            if sorted(best_solution[1]) in tabu_queue:
                if aspiration(max(neighborhood_values), current_value):
                    current_solution = best_solution
                    previous_value = current_value
                    current_value = max(neighborhood_values)
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
                break

        if current_value == previous_value:
            count_repetitive_solution += 1
        else:
            count_repetitive_solution = 0
        count += 1

    open("log.csv", "a").write(
        f"{count}; {list(map(int, current_solution[0]))}; {current_value}\n"
    )
    return current_solution[0], current_value, count, qtd_strategy

