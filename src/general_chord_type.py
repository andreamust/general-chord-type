"""
Re-implementation of the General Chord Type in an Object-Oriented fashion.
"""

CV = [0, 7, 5, 1, 1, 2, 3, 1, 2, 2, 4, 6]


def calculate_weights(root: int, grades: list, consonance_vector: list):
    return [consonance_vector[(x - root if x >= root else 12 + x - root)] for x in grades]


def get_minimum_weight(chord_grades: list, consonance_vector: list):
    minimum = None

    for grade in chord_grades:
        abc = calculate_weights(grade, chord_grades, consonance_vector)
        print(abc)


get_minimum_weight([0, 3, 5, 7], CV)
