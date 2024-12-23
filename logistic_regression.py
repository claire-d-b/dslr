from pandas import DataFrame
import random
from math import e
from utils import switch_case


def get_sigmoid_function(scores: list, house: list, theta_0: float,
                         theta_1: float, learning_rate: float) -> tuple:
    """Take all values from x-axis and y-axis lists and calculate the
    mean square error for minimum square errors, update thetas"""

    mse = 0.0
    m = len(scores)
    weights = []

    for i, (score_row, house_unit) in enumerate(zip(scores, house)):
        weights.insert(i, [])
        for j, score_unit in enumerate(score_row):
            b, w, se = minimize_cost(m, theta_0, theta_1, score_unit,
                                     house_unit, learning_rate)
            theta_0 += b
            theta_1 += w
            weights[i].insert(j, theta_1 / len(score_row))

        mse += se
    ret_mse = mse * 1 / (2 * m)
    theta_0 /= len(scores) * len(score_row)
    bias = theta_0

    return bias, weights, ret_mse


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
        # real_price = theta_1 * real_mileage + theta_0
        # real_price - theta_0 = theta_1 * real_mileage
        # -theta_0 = theta_1 * real_mileage - real_price
        # theta_0 = -(theta_1 * real_mileage - real_price)
        theta_0 = -theta_1 * real_score + real_house
        z = theta_1 * real_score + theta_0

        # The natural logarithm (ln⁡) of e is 1, because the
        # natural logarithm is defined as the inverse of the
        # exponential function:
        # ln(e) = 1
        # This is true because:
        # e**1 = e

        # theta_0 = -theta_1 * real_score + real_house
        loss = ((1 / (1 + e ** -z)) - real_house)
        if loss < limit:

            limit = loss
            b = theta_0
            w = theta_1

    return b, w, limit


def train_model(lhs: DataFrame, rhs: DataFrame,
                learning_rate: float) -> tuple:
    """Get thetas that minimizes the mean square error"""

    # Generate a random floating-point number between -0.01 and 0.01
    theta_0 = random.uniform(-0.01, 0.01)
    theta_1 = random.uniform(-0.01, 0.01)

    scores = lhs
    house = [switch_case(x) for x in rhs]

    theta_0, theta_1, mse = get_sigmoid_function(scores, house,
                                                 theta_0, theta_1,
                                                 learning_rate)

    return theta_1, theta_0
