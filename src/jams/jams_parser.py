"""

"""

import jams

from src.general_chord_type import harte_to_gct
from src.transposer import transposer


def parse_jams(jams_path: str) -> tuple:
    """

    :param jams_path:
    :return:
    """
    jams_file = jams.load(jams_path, validate=False, strict=False)

    annotations = [annotation for annotation in jams_file.annotations]
    observations = annotations[0].data
    key = annotations[1].data
    return [observation.value for observation in key], [observation.value for observation in observations]


def convert_jams(jams_chords: list, jams_key: str) -> list:
    """

    :param jams_chords:
    :param jams_key:
    :return:
    """
    converted_chords = [harte_to_gct(chord) for chord in jams_chords]
    return [[transposer(jams_key, root, target_root=0), grades] for root, grades in converted_chords]


if __name__ == '__main__':
    keys, chords = parse_jams('../../test/test_data/biab-internet-corpus_12.jams')
    print(keys)
    print(chords)
    print(convert_jams(chords, keys[0]))
