"""
Re-implementation of the General Chord Type in an Object-Oriented fashion.
"""
import sys

from utils import get_minimum

TONAL_VECTOR = [0, 7, 5, 1, 1, 2, 3, 1, 2, 2, 4, 6]


def calculate_weights(root: int, grades: list, consonance_vector: list):
    """
    Utility function that calculates the weights of a given sequence of
    grades
    :param root:
    :param grades:
    :param consonance_vector:
    :return:
    """
    return [consonance_vector[(x - root if x >= root else 12 + x - root)] for x in grades]


def get_minimum_path(chord_grades: list, consonance_vector: list):
    """

    :param chord_grades:
    :param consonance_vector:
    :return:
    """

    paths = [[g] for g in chord_grades]
    # loop until the output has the same shape as the input
    while len(paths[0]) != len(chord_grades):
        # initialise the minimum at the max possible value (theoretically)
        minimum = sys.maxsize
        step_path = paths[:]
        for step in step_path:
            # calculate the grades to which the min_indexes refer
            reference_grades = [x for x in chord_grades if x not in step]
            # get the total weight by iterating over all the chain
            total_weight = []
            for chain_el in step:
                weights = calculate_weights(chain_el, reference_grades, consonance_vector)
                total_weight.append(weights)
            weights = [sum(j) for j in zip(*total_weight)]
            combination_minimum, min_indexes = get_minimum(weights)
            if combination_minimum <= minimum:
                # if the minimum is lower than the achieved clean the list
                if combination_minimum < minimum:
                    paths.clear()
                    minimum = combination_minimum
                # store the minimum value path
                for idx in min_indexes:
                    paths.append(step + [reference_grades[idx]])

    print(paths)


if __name__ == "__main__":
    get_minimum_path([0, 4, 7, 9], TONAL_VECTOR)
