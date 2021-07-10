import copy


def generate_closer_neighbors(solution):
    neighborhood = []

    for i in range(len(solution)):
        neighbor = copy.deepcopy(solution)
        neighbor[i] = not neighbor[i]
        neighborhood.append((neighbor, [i, i]))

    return neighborhood

