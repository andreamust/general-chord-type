"""
Re-implementation of the General Chord Type in an Object-Oriented fashion.
"""
import sys
from collections import namedtuple

from utils import get_minimum

CV = [0, 7, 5, 1, 1, 2, 3, 1, 2, 2, 4, 6]


def calculate_weights(root: int, grades: list, consonance_vector: list):
    """

    :param root:
    :param grades:
    :param consonance_vector:
    :return:
    """
    return [consonance_vector[(x - root if x >= root else 12 + x - root)] for x in grades]


def get_minimum_weight(chord_grades: list, consonance_vector: list):
    """

    :param chord_grades:
    :param consonance_vector:
    :return:
    """

    fixed_grades = [0, 3, 5, 9]

    minimum = sys.maxsize

    paths = []
    level = []
    # while len(paths[0]) == len(chord_grades):

    for grade in chord_grades:
        combination = namedtuple('combination', 'root grade min')
        # get the total weight by iterating over all the chain
        total_weight = []
        for chain_el in grade:
            weights = calculate_weights(chain_el, [x for x in fixed_grades if x not in grade], consonance_vector)
            total_weight.append(weights)
        weights = [sum(j) for j in zip(*total_weight)]
        print(grade, chord_grades, weights)
        combination_minimum, min_indexes = get_minimum(weights)
        print('combination_minimum', combination_minimum, min_indexes)
        if combination_minimum <= minimum:
            if combination_minimum < minimum:
                level.clear()
            minimum = combination_minimum
            reference_grades = [x[-1] for x in chord_grades if x[-1] not in grade]
            print('rg', reference_grades)
            paths.extend(grade)

            level.extend([combination(grade[-1], reference_grades[x], minimum) for x in min_indexes])
            print(level)
    paths.extend([(combination.root, combination.grade) for combination in level])


    print(paths)


def get_weight(chord_grades: list, consonance_vector: list):
    for grade in chord_grades:
        pass


if __name__ == "__main__":
    get_minimum_weight([[5, 0], [0, 3], [5, 9], [9, 0]], CV)
