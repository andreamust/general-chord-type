"""

"""
import os
import sys
from itertools import combinations

import joblib

from src.jams.jams_parser import parse_jams, convert_jams
from src.jams.jams_utils import convert_key

DATASET = '/Users/andreapoltronieri/PycharmProjects/choco/partitions/biab-internet-corpus/choco/jams_converted'

SIMPLIFICATIONS = 'data/chord_simplifications.joblib'


def all_chords(dataset_file_path: str) -> list:
    """

    :param dataset_file_path:
    :return:
    """
    all_chords = []
    for filename in os.listdir(dataset_file_path):
        print(f'Converting track: {filename}')
        if filename.endswith(".jams"):
            keys, chords = parse_jams(os.path.join(dataset_file_path, filename))
            converted_chords = convert_jams(chords, keys[0])
            all_chords.extend(converted_chords)

    chords = set(tuple((x, tuple(y))) for x, y in all_chords)
    return list(chords)


def test_chord_similarity(chord1: tuple, chord2: tuple) -> bool:
    """

    :param chord1:
    :param chord2:
    :return:
    """
    if chord1[0] == chord2[0]:
        if set(chord1[1]).issubset(set(chord2[1])) or set(chord2[1]).issubset(set(chord1[1])):
            key, scale = convert_key('C:major')
            if (set([x if x <= 12 else x - 12 for x in chord1[1]]).issubset(set(scale)) and set(
                    [x if x <= 12 else x - 12 for x in chord2[1]]).issubset(set(scale))) or \
                    (not set([x if x <= 12 else x - 12 for x in chord1[1]]).issubset(
                        set(scale)) and not set(
                        [x if x <= 12 else x - 12 for x in chord2[1]]).issubset(set(scale))):
                return True
    return False


def store_simplifications(chords_list: list) -> list:
    simplifications = []
    for combination in combinations(chords_list, 2):
        if test_chord_similarity(combination[0], combination[1]):
            for s in simplifications:
                if combination[0] and combination[1] in s:
                    break
                if combination[0] in s and combination[1] not in s and False not in [
                                test_chord_similarity(x, combination[1]) for x in s]:
                    s.append(combination[1])
                    break
                if combination[1] in s and combination[0] not in s and False not in [
                                test_chord_similarity(x, combination[0]) for x in s]:
                    s.append(combination[0])
                    break
            else:
                if test_chord_similarity(combination[0], combination[1]):
                    simplifications.append([combination[0], combination[1]])
    joblib.dump(simplifications, SIMPLIFICATIONS)
    return simplifications


def simplify_chord(gct_chord: tuple, chord_simplifications: str = SIMPLIFICATIONS) -> tuple:
    simplified = joblib.load(chord_simplifications)
    for simplified_class in simplified:
        if gct_chord in simplified_class:
            minimum = sys.maxsize
            minimum_value = None
            for el in simplified_class:
                if len(el[1]) < minimum:
                    minimum = len(el[1])
                    minimum_value = el
            return minimum_value
    return gct_chord


if __name__ == '__main__':
    # chords_list = all_chords(DATASET)
    # simplified_chord = store_simplifications(chords_list)
    print(simplify_chord((10, (0, 4, 7, 11, 15))))
