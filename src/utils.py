"""

"""

import csv

import numpy as np


def get_minimum(values_list: list) -> tuple:
    """

    :param values_list:
    :return:
    """
    minimum = min(x for x in values_list if x > 0)
    values_array = np.array(values_list)
    return minimum, list(np.where(values_array == minimum)[0])


def open_stats_file(stats_file_path: str):
    """
    Opens the stats_file, which contains all chord annotations for each dataset.

    Parameters
    -----------
    stats_file_path : str
        The path of the stats_file
    Returns
    -------
    chord_list : List
        A list of all chord occurrences contained in the dataset.
    """
    with open(stats_file_path) as csv_file:
        stats = csv.reader(csv_file, delimiter=',')
        # skip header
        next(stats)
        return [x for x in stats]


def normalise_grade(grade: int) -> int:
    while grade > 12:
        grade -= 12
    return grade
