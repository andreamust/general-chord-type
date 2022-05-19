"""
Re-implementation of the General Chord Type in an Object-Oriented fashion.
"""
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
harte_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'harte'))
sys.path.append(harte_path)

from utils import get_minimum
from harte.harte_utils import harte_to_pitch

TONAL_VECTOR = [0, 7, 5, 1, 1, 2, 3, 1, 2, 2, 4, 6]
ATONAL_VECTOR = [0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]


def calculate_weights(root: int, grades: list, consonance_vector=None) -> list:
    """
    Utility function that calculates the weights of a given sequence of chord
    grades and a root note, calculates the weights between the root and each
    grade, based on a consonance-dissonance vector
    :param root: the grade from which to calculate the weights
    :param grades: the grades on which to calculate the weights
    :param consonance_vector: a 12-valued vector that defines the consonance/
    dissonance of the different grades. In this vector, the higher the value,
    the lower the consonance.
    Two default vectors are presented with the script:
        - TONAL_VECTOR
        - ATONAL_VECTOR
    :return: list: a list of weights, having the same shape as the input grades
    list
    """
    if consonance_vector is None:
        consonance_vector = TONAL_VECTOR
    grades = [g if g <= 11 else g - 12 for g in grades]
    return [consonance_vector[(x - root if x >= root else 12 + x - root)] for x in grades]


def get_minimum_path(chord_grades: list, consonance_vector: list) -> list[list]:
    """
    Main function for calculating the shortest path (weight wise) of a given sequence
    of chord tones, expressed in pitch sets
    :param chord_grades: the pitch sets that make up a chord
    :param consonance_vector: a 12-valued vector that defines the consonance/
    dissonance of the different grades. In this vector, the higher the value,
    the lower the consonance.
    :return: list[list]: a list of lists, where each list is the optimal path
    for the input chord grades, calculated on the given consonance vector
    """
    # initialises the paths as a list of lists
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
            # gets the minimum of the combination and their indexes
            combination_minimum, min_indexes = get_minimum(weights)
            if combination_minimum <= minimum:
                # if the minimum is lower than the achieved clean the list
                if combination_minimum < minimum:
                    paths.clear()
                    minimum = combination_minimum
                # store the minimum value path
                for idx in min_indexes:
                    paths.append(step + [reference_grades[idx]])

    return paths


def reorganise_path(gct_path: list) -> list:
    """
    Utility function that reorganises a path chord wise (considering the
    chord notes) and according to the GCT rules.
    The organisation of the path is [root, [grades]]
    :param gct_path: the optimal path as returned by the get_minimum_path
    function
    :return: list: the input path organised according to the GCT principles,
    i.e. [root, [grades]]
    """
    root = gct_path[0]
    reorganised_grades = sorted((x - root if x - root >= 0 else 12 + x - root) for x in gct_path)

    return [root + reorganised_grades[0], reorganised_grades]


def choose_path_alternatives(path_alternatives: list[list], original_chord: list) -> list:
    """

    :param path_alternatives:
    :param original_chord:
    :return:
    """
    assert len(path_alternatives) > 0, 'GCT produced no results.'
    print(len(path_alternatives))
    if len(path_alternatives) == 1:
        return path_alternatives[0]
    best_alternative = [x for x in path_alternatives if path_alternatives[0] == original_chord[0]]
    return best_alternative[0] if len(best_alternative) > 0 else path_alternatives[0]


def harte_to_gct(harte_chord: str) -> list:
    """
    Main function that converts a Harte chord into a pitch-class set, and
    performs the New-GCT algorithm on it
    :return:
    """
    chord = harte_to_pitch(harte_chord)
    minimum_path = get_minimum_path(chord, TONAL_VECTOR)
    minimum_path = choose_path_alternatives(minimum_path, chord)

    return reorganise_path(minimum_path)


if __name__ == "__main__":
    # ex = get_minimum_path([4, 7, 11], TONAL_VECTOR)
    # print(ex)
    # print(reorganise_path(ex[0]))
    test = harte_to_gct('C:sus4')
    print(test)
