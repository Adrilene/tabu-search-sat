import time
from configuration import sat_file
from tabu_search import tabu_search
from random import choice
import sys

def main():
    open("log.csv", "w").write("iteracao; current solution; current value\n")
    ini = time.time()
    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace("\n", "").strip().split(" "))))

    initial_solution = ([choice([True, False]) for _ in range(range_literal)], -1, -1)
    optimal_value = sys.argv[0] if sys.argv else range_clause
    result, best_value, count, qtd_strategy = tabu_search(initial_solution, clauses, range_literal, optimal_value)
    end = time.time()
    result = list(map(int, result))

    print(f'Resultado: {result}')
    print(f'Valor ótimo: {best_value}')
    print(f'Tempo de execução: {end - ini}')
    print(f'Número de iterações: {count}')
    print(f'Quantidade de Intensificações: {qtd_strategy["Intesified"]}')
    print(f'Quantidade de Diversificações: {qtd_strategy["Diversed"]}')

if __name__ == "__main__":
    main()
