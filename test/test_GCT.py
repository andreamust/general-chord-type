"""
Test file for the General Chord Type (GCT) re-implementation.
"""

import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)
harte_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'harte'))
sys.path.append(harte_path)

from general_chord_type import harte_to_gct
from utils import open_stats_file

TEST_DATA = os.path.join(os.path.dirname(os.getcwd()), 'test', 'test_data')


def test_chords_stats(file_path: str):
    """

    :param file_path:
    :return:
    """
    chord_data = open_stats_file(file_path)

    classes = []
    for data in chord_data:
        if 'chord' in data[3]:
            print(data[1])
            gct_chord = harte_to_gct(data[1])
            classes.append(gct_chord)
            print(f'{data[0]} ---> {gct_chord}')
    print(f'\nOriginal classes: {len(chord_data)}')
    print(f'\nTotal classes: {len(set([tuple((e, tuple(l))) for e, l in classes]))}')


if __name__ == '__main__':
    test_chords_stats(os.path.join(TEST_DATA, 'biab_chords.csv'))
