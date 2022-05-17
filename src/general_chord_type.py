"""
Re-implementation of the General Chord Type in an Object-Oriented fashion.
"""
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
    minimum = 999
    paths = []

    for grade in chord_grades:
        combination = namedtuple('combination', 'root grade min')
        weights = calculate_weights(grade, chord_grades, consonance_vector)
        print(grade, chord_grades, weights)
        combination_minimum, min_indexes = get_minimum(weights)
        if combination_minimum <= minimum:
            minimum = combination_minimum
            paths.extend([combination(grade, chord_grades[x], minimum) for x in min_indexes])
    print(paths)


if __name__ == "__main__":
    get_minimum_weight([0, 3, 5, 9], CV)
