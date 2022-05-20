"""

"""
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
jams_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'jams'))
sys.path.append(jams_path)

from jams_utils import convert_key


def transposer(harte_key: str, note_root: int, target_root: int = 0):
    """

    :param harte_key:
    :param note_root:
    :param target_root:
    :return:
    """
    key_root, scale = convert_key(harte_key)
    note_root = note_root if note_root >= key_root else note_root + 12
    difference = (note_root - key_root) + target_root
    assert difference >= 0, 'Negative differences not allowed.'
    return difference


if __name__ == '__main__':
    print(transposer('A:major', 9))
