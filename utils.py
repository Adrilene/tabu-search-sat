from configuration import tabu_size
from math import factorial
import random


def update_tabu(queue, value):
    global tabu_size
    if len(queue) >= tabu_size:
        queue.pop(0)
    queue.append(sorted(value))
    return queue


def aspiration(best_value, current_value):
    if best_value > current_value:
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

def get_random_solution(one, two):
    return random.choices([one, two], [0.5, 0.5], k=1)[0]