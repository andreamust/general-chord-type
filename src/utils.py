"""

"""

import numpy as np


def get_minimum(values_list: list) -> tuple:
    """

    :param values_list:
    :return:
    """
    minimum = min(x for x in values_list if x > 0)
    values_array = np.array(values_list)
    return minimum, list(np.where(values_array == minimum)[0])
