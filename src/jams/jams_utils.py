"""

"""
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)
harte_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'harte'))
sys.path.append(harte_path)

from harte_utils import harte_to_pitch
from general_chord_type import harte_to_gct


def convert_key(jams_key: str):
    """

    :param jams_key:
    :return:
    """
    assert ':' in jams_key, 'The given key is not a valid JAMS key.'
    key_root, scale = jams_key.split(':')
    assert scale in ['major', 'minor'], 'The key scale is not supported.'
    if scale == 'major':
        scale = f'{key_root}:(1,2,3,4,5,6,7)'
    elif scale == 'minor':
        scale = f'{key_root}:(1,2,b3,4,5,b6,b7)'
    key_pc_set = harte_to_pitch(scale)
    root = key_pc_set[0]
    pc_set_grades = [g - root for g in key_pc_set]
    return [root, pc_set_grades]


if __name__ == '__main__':
    print(convert_key('Cb:minor'))
