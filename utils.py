from configuration import tabu_size, delta_aspiration, delta_to_intensficate
from math import factorial
import random


def update_tabu(queue, value):
    if len(queue) >= tabu_size:
        queue.pop(0)
    queue.append(sorted(value))
    return queue


def change_positions_tabu(queue, value):
    queue.pop(queue.index(value))
    queue.append(value)
    return queue


def aspiration_by_objective(best_value, current_value):
    if best_value > current_value:
        return True
    return False


def aspiration_by_influence(best_value, current_value, optimal_value):
    if abs(best_value - current_value) >= delta_aspiration:
        return True
    if (
        optimal_value - best_value <= delta_to_intensficate
        and best_value > current_value
    ):
        return True
    return False


def assignment(literals, clauses):
    true_clauses = 0
    for clause in clauses:
        literals_result = [
            literals[abs(clause_value) - 1]
            if clause_value > 0
            else not literals[abs(clause_value) - 1]
            for clause_value in clause
        ]
        if True in literals_result:
            true_clauses += 1
    return true_clauses


def calculate_len_of_neighbors(n):
    nv = factorial(n) / (factorial(2) * factorial(n - 2))
    if nv > 1000:
        return 1000
    return nv


def get_random_solution(one, two, three, four, five):
    return random.choices([one, two, three, four, five], [0.5, 0.5, 0.5, 0.5, 0.5], k=1)[0]
