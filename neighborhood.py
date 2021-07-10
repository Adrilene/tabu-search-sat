import copy
import random
import time
from utils import calculate_len_of_neighbors


def disturb_solution(solution):  # REFATOR
    solution_copy = copy.deepcopy(solution[0])
    random.seed(time.time())
    indexes = sorted(random.sample(range(0, len(solution[0])), k=2))  # FIX
    for i in indexes:
        solution_copy[i] = not solution_copy[i]
    return solution_copy, indexes


def generate_neighborhood(solution, range_literal):
    nv = calculate_len_of_neighbors(range_literal)
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, indexes = disturb_solution(solution)
        complete_solution = (troubled_solution, indexes)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

    return neighborhood

