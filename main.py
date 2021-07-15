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
    print(tabu_search(initial_solution, clauses, range_literal))
    end = time.time()
    print(f"time: {end - ini}")
    open("log.txt", "a").write(f"time: {time}")


if __name__ == "__main__":
    main()
