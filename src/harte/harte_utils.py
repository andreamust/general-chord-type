"""
Utility functions for managing and transforming Harte chords.
"""

from music21 import note, interval

from harte_map import HARTE_SHORTHAND_MAP


def extend_harte(harte_grades: str) -> list:
    """

    :param harte_grades: a chord's grades annotated according to the Harte
    Notation
    :return: str: a chord annotated according to the Harte Notation without
    any shortcut
    """
    split_grades = harte_grades.split('(')
    assert split_grades[0] in HARTE_SHORTHAND_MAP.keys(), 'The Harte shorthand is not mapped.'
    extended_shorthand = list(HARTE_SHORTHAND_MAP[split_grades[0]])
    # if there is only a shorthand
    if len(split_grades) == 1:
        return extended_shorthand
    # if shorthand and grades
    cleaned_grades = split_grades[1].split(',')
    return sorted(set(extended_shorthand + cleaned_grades), key=lambda x: x[-1])


def convert_interval(chord_interval: str) -> str:
    """
    Utility function that converts intervals from the Harte notation
    (e.g. b3, #5, etc.) to the music21.interval.DiatonicInterval.simpleName
    :param chord_interval: an interval name expressed in the Harte syntax
    :return: str: an interval expressed as the music21.interval.DiatonicInterval.simpleName
    """
    base_grade = int(''.join([g for g in chord_interval if g.isdigit()]))
    base_grade = base_grade if base_grade < 8 else base_grade - 7
    if base_grade in [1, 4, 5]:
        if 'b' in chord_interval or '#' in chord_interval:
            return chord_interval.replace('b', 'd').replace('#', 'A')
        return f'P{chord_interval}'
    if 'b' in chord_interval or '#' in chord_interval:
        return chord_interval.replace('b', 'm').replace('#', 'A')
    return f'M{chord_interval}'


def harte_to_pitch(harte_chord: str) -> tuple:
    """

    :param harte_chord: a chord annotated according to the Harte Notation
    :return: list: a list of pitches that compose the chord
    """
    harte_split = harte_chord.split(':')
    assert len(harte_split) == 2, 'The given chord is not a valid Harte chord.'
    harte_root, harte_grades = harte_split
    # get the root pitch
    root_object = note.Note(harte_root)
    root_pitch = root_object.pitch.pitchClass
    # check the first character of harte_grades
    # if grades contains shorthands extend the chord
    harte_grades = harte_grades.lstrip('(').rstrip(')')
    if harte_grades[0] != '(':
        harte_grades = extend_harte(harte_grades)
    else:
        harte_grades = harte_grades.split(',')
    harte_grades = [interval.Interval(convert_interval(x)).chromatic.mod12 for x in harte_grades]
    if '*1' not in harte_chord:
        harte_grades.append(0)
    return root_pitch, sorted(harte_grades)


if __name__ == '__main__':
    # test Harte utils
    print(harte_to_pitch('Fb:maj(6,7)'))
    print(harte_to_pitch('C#:maj(3,5,b7)'))
