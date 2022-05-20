"""

"""
import os
from itertools import combinations

from src.jams.jams_parser import parse_jams, convert_jams
from src.jams.jams_utils import convert_key

DATASET = '/Users/andreapoltronieri/PycharmProjects/choco/partitions/biab-internet-corpus/choco/jams_converted'


def all_chords(dataset_file_path: str) -> list:
    """

    :param dataset_file_path:
    :return:
    """
    chords = []
    for filename in os.listdir(dataset_file_path):
        print(f'Converting track: {filename}')
        if filename.endswith(".jams"):
            keys, chords = parse_jams(os.path.join(dataset_file_path, filename))
            converted_chords = convert_jams(chords, keys[0])
            chords.extend(converted_chords)

    chords = set(tuple((x, tuple(y))) for x, y in chords)
    return list(chords)


def simplify_chord(chords_list: list) -> list:
    simplifications = []
    for combination in combinations(chords_list, 2):
        if combination[0][0] == combination[1][0]:
            if set(combination[0][1]).issubset(set(combination[1][1])) or set(combination[1][1]).issubset(
                    set(combination[0][1])):
                key, scale = convert_key('C:major')
                if set(combination[0][1]).issubset(set(scale)) and set(combination[1][1]).issubset(set(scale)) or \
                        not set(combination[0][1]).issubset(set(scale)) and set(combination[1][1]).issubset(set(scale)):
                    for s in simplifications:
                        if combination[0][1] and combination[1][1] in s:
                            break
                        elif combination[0][1] and not combination[1][1] in s:
                            s.append(combination[1][1])
                        elif combination[1][1] and not combination[0][1] in s:
                            s.append(combination[0][1])
                    else:
                        simplifications.append([combination[0][1], combination[1][1]])

    return simplifications


if __name__ == '__main__':
    chords_list = all_chords(DATASET)
    simplified_chord = simplify_chord(chords_list)
    print(simplified_chord)
    print(len(simplified_chord), len(chords_list))
