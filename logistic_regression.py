from pandas import DataFrame
import random
from numpy import log
from math import e


def get_sigmoid_function(score: list, house: list, theta_0: float,
                         theta_1: float, learning_rate: float) -> tuple:
    """Take all values from x-axis and y-axis lists and calculate the
    mean square error for minimum square errors, update thetas"""

    mse = 0.0
    m = len(score)

    for score_unit, house_unit in zip(score, house):
        b, w, se = minimize_cost(m, theta_0, theta_1, score_unit,
                                 house_unit, learning_rate)
        theta_0 += b
        theta_1 += w

        mse += se
    ret_mse = mse * 1 / (2 * m)
    theta_0 /= len(score)
    theta_1 /= len(score)

    return theta_0, theta_1, ret_mse


def minimize_cost(m: int, theta_0: float, theta_1: float, real_score: float,
                  real_house: float, learning_rate: float) -> tuple:
    """Test with a slope value between -0.01 and 0.01, update y-interceipt
    value, take the smallest square error and return corresponding w and b"""
    limit = float("inf")
    w = 0.0
    b = 0.0

    minimum = int(- 1 / learning_rate)
    maximum = int(1 / learning_rate)

    for i in range(minimum, maximum, 1):
        theta_1 = float(i / ((2 * m) / learning_rate))
        # Below formula is that of the sigoid function
        # real_house = 1 / (1 + e ** -(theta_1 * real_score + theta_0))
        # 1 + (e ** -(theta_1 * real_score + theta_0)) * real_house = 1
        # 1 + (e ** -(theta_1 * real_score + theta_0)) = 1 / real_house
        # e ** -(theta_1 * real_score + theta_0) = 1 / real_house - 1
        # log(e ** -(theta_1 * real_score + theta_0))
        # = log(1 / real_house - 1)
        # -(theta_1 * real_score) - theta_0 = log(1 / real_house - 1)
        # - theta_0 = log(1 / real_house - 1) + (theta_1 * real_score)
        if (real_house):
            theta_0 = -(log(1 / real_house) + (theta_1 * real_score))
        else:
            theta_0 = -(log(1 / abs(real_house - 1)) + (theta_1 * real_score))

        # The natural logarithm (ln⁡) of e is 1, because the natural logarithm
        # is defined as the inverse of the exponential function:
        # ln(e) = 1
        # This is true because:
        # e**1 = e

        theta_0 = -theta_1 * real_score + real_house
        se = ((1 / 1 + e ** -(theta_1 * real_score + theta_0)) -
              real_house) ** 2
        if se < limit:

            limit = se
            b = theta_0
            w = theta_1

    return b, w, limit


def train_model(lhs: DataFrame, rhs: DataFrame,
                learning_rate: float) -> tuple:
    """Get thetas that minimizes the mean square error"""

    # Generate a random floating-point number between -0.01 and 0.01
    theta_0 = random.uniform(-0.01, 0.01)
    theta_1 = random.uniform(-0.01, 0.01)

    score = [sum(x) for x in lhs]
    house = [float(x) for x in rhs]

    theta_0, theta_1, mse = get_sigmoid_function(score, house,
                                                 theta_0, theta_1,
                                                 learning_rate)

    return theta_1, theta_0
