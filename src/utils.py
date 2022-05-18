"""

"""

import numpy as np

from collections import namedtuple


def get_minimum(values_list: list) -> tuple:
    """

    :param values_list:
    :return:
    """
    minimum = min(x for x in values_list if x > 0)
    values_array = np.array(values_list)
    return minimum, list(np.where(values_array == minimum)[0])


def reformat_combinations(combinations_list: list[namedtuple], new_minimum: int) -> list:
    """

    :param new_minimum:
    :param combinations_list:
    :return:
    """
    for el in combinations_list:
        if el.min > new_minimum:
            combinations_list.remove(el)
    return combinations_list
