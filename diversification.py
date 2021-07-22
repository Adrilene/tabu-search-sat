from utils import calculate_len_of_neighbors, assignment, get_random_solution
import copy
import random
from configuration import random_repetitive
import time


def disturb_solution_diversed(solution):
    solution_copy = copy.deepcopy(solution)
    random.seed(time.time())
    indexes = sorted(random.sample(range(0, len(solution)), k=int(len(solution) / 4)))

    for i in indexes:
        solution_copy[i] = not solution_copy[i]

    return solution_copy, indexes


def generate_diversed_neighbors(history, clauses, current_value, range_literal):
    print("Make Diversification")
    random.seed(time.time())
    solutions, values = [], []
    while True:
        for _ in range(random_repetitive):
            history_sample = random.sample(history, 5)
            choice = []
            for one, two, three, four, five in zip(history_sample[0], history_sample[1], history_sample[2], history_sample[3], history_sample[4]):
                choice.append(get_random_solution(one, two, three, four, five))
            solutions.append(choice)

        for solution in solutions:
            values.append((assignment(solution, clauses)))
        max_index = 0
        solution = solutions[0]
        for i, value in enumerate(values):
            if abs(current_value - value) > abs(current_value - values[max_index]):
                solution, max_index = solutions[i], i
        if solution not in history:
            history.append(solution)
            break
        # else:
        #     solution = [
        #         random.choices([True, False], [0.5, 0.5], k=1)[0]
        #         for _ in range(range_literal)
        #     ]
        #     break

    nv = calculate_len_of_neighbors(range_literal)
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, indexes = disturb_solution_diversed(solution)
        complete_solution = (troubled_solution, indexes)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

    return neighborhood, history

