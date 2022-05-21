"""

"""
import os

import joblib

from src.jams import jams_parser
from src.simplify_chord import simplify_chord, DATASET

import pandas as pd


def compute_dataset(dataset_path: str):
    """

    :param dataset_path:
    :return:
    """
    converted_simplified = dict()
    for filename in os.listdir(dataset_path):
        print(f'Converting track: {filename}')
        track_chords = []
        if filename.endswith(".jams"):
            keys, chords = jams_parser.parse_jams(os.path.join(dataset_path, filename))
            converted_chords = jams_parser.convert_jams(chords, keys[0])
            for chord in converted_chords:
                track_chords.append(simplify_chord(chord))
        converted_simplified[filename] = track_chords

    joblib.dump(converted_simplified, 'data/converted_simplified.joblib')
    return converted_simplified


def save_file_metadata(dataset_path: str):
    """

    :param dataset_path:
    :return:
    """
    metadata = []
    for filename in os.listdir(dataset_path):
        if filename.endswith(".jams"):
            file_title = jams_parser.get_jams_meta(os.path.join(dataset_path, filename))
            metadata.append([filename, file_title])
    meta_df = pd.DataFrame(metadata, columns=['filename', 'title'])
    meta_df.sort_values(by=['filename'], inplace=True, ascending=False)
    meta_df.to_csv('biab_metadata.csv', index=False)


if __name__ == '__main__':
    # print(compute_dataset(DATASET))
    save_file_metadata(DATASET)
