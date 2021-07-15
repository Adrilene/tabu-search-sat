from utils import calculate_len_of_neighbors
import copy
import random
from random import choice
import time


def disturb_solution_diversed(solution):
    solution_copy = copy.deepcopy(solution)
    random.seed(time.time())
    indexes = sorted(
        random.sample(range(0, len(solution)), k=int(len(solution) / 4))
    )

    for i in indexes:
        solution_copy[i] = not solution_copy[i]

    return solution_copy, indexes


def generate_diversed_neighbors(history, range_literal):
    while True:
        solution = [choice([True, False]) for _ in range(range_literal)]
        if solution not in history:
            break
    nv = calculate_len_of_neighbors(range_literal)
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, indexes = disturb_solution_diversed(solution)
        complete_solution = (troubled_solution, indexes)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

    return neighborhood

