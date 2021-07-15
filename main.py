import time
from configuration import sat_file
from tabu_search import tabu_search
from random import choice


def main():
    open("log.txt", "w").write("")
    ini = time.time()
    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace("\n", "").strip().split(" "))))

    initial_solution = ([choice([True, False]) for _ in range(range_literal)], -1, -1)
    result, best_value, count = tabu_search(initial_solution, clauses, range_literal)
    end = time.time()
    result = list(map(int, result))
    qtd_intensified = len([True for line in open('log.txt','r').readlines() if 'Intesified' in line])
    qtd_diversed = len([True for line in open('log.txt','r').readlines() if 'Diversed' in line])

    print(f'Resultado: {result}')
    print(f'Valor ótimo: {best_value}')
    print(f'Tempo de execução: {end - ini}')
    print(f'Número de iterações: {count}')
    print(f'Quantidade de Intensificações: {qtd_intensified}')
    print(f'Quantidade de Diversificações: {qtd_diversed}')

if __name__ == "__main__":
    main()
