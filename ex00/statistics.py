def nearest(quartile: float, lst: list) -> float:
    distance = 0
    mindistance = float('inf')
    index = 0
    for i in range(len(lst)):
        distance = abs(lst[i] - quartile)
        if distance < mindistance:
            mindistance = distance
            index = i
    return lst[index]


def ft_statistics(*args: any, **kwargs: any) -> None:
    lst = ['mean', 'median', 'var', 'std', 'quartile']
    idx = 0
    ret = 0
    i = 0

    largs = list(args)

    for key in kwargs:
        for i in range(len(lst)):
            if kwargs[key] == lst[i]:
                idx = i

                if idx == 0:
                    try:
                        len(largs)
                        for arg in largs:
                            ret += arg
                        ret = ret / len(largs)
                        print(ret)
                    except Exception:
                        print("ERROR")

                elif idx == 1:
                    # The median is a measure of central tendency that
                    # represents the middle value of a dataset when it is
                    # ordered from smallest to largest.
                    # If the dataset contains an odd number of observations,
                    # the median is the middle value. If the dataset contains
                    # an even number of observations, the median is the average
                    # of the two middle values.
                    try:
                        len(largs)
                        largs.sort(key=None, reverse=False)

                        if len(largs) % 2:
                            index = len(largs) / 2
                            ret = largs[int(index)]
                            print(ret)
                        else:
                            index = len(largs) / 2
                            ret = (largs[int(index - 1) +
                                   largs[int(index)]]) / 2
                            print(ret)
                    except Exception:
                        print("ERROR")

                elif idx == 2 or idx == 3:
                    # The standard deviation is a measure of
                    # the amount of variation or dispersion in a set
                    # of values. It quantifies how much the values
                    # in a dataset deviate from the mean (average)
                    # of the dataset.
                    # Variance is a measure of the dispersion or
                    # spread of a set of data points.
                    # It quantifies how much the values in a dataset
                    # differ from the mean of the dataset. """
                    try:
                        len(largs)
                        # Calculate the Mean:
                        mean = 0
                        for arg in largs:
                            mean += arg
                        mean = mean / len(largs)
                        # Calculate Each Deviation from the Mean and
                        # Square it:
                        deviation_lst = []
                        for arg in largs:
                            deviation_lst.append((arg - mean) ** 2)
                        # Calculate the Mean of These Squared Deviations:
                        sd_mean = 0

                        for item in deviation_lst:
                            sd_mean += item
                        sd_mean = sd_mean / len(deviation_lst)

                        if idx == 3:
                            # Take the Square Root:
                            print(sd_mean ** 0.5)
                        else:
                            print(sd_mean)
                    except Exception:
                        print("ERROR")

                elif idx == 4:
                    # Calculating quartiles is a common task
                    # in statistics, often used to divide a dataset
                    # into four equal parts.
                    # Quartiles provide information about the spread
                    # and distribution of data.
                    # There are three main quartiles:
                    # First Quartile (Q1): Also known as the
                    # lower quartile, it divides the lowest 25% of
                    # the data from the rest.
                    # Second Quartile (Q2): This is the median of
                    # the dataset, dividing it into two halves.
                    # Third Quartile (Q3): Also known as the upper
                    # quartile, it divides the highest 25% of the
                    # data from the rest.
                    # Steps:

                    # Sort the data: First, sort the data in ascending order.
                    # Find the median: The second quartile (Q2) is the median
                    # of the dataset.
                    # Find Q1 and Q3: Q1 is the median of the lower half of the
                    # data (below the median), and Q3 is the median of the
                    # upper half (above the median).

                    # How to use interpolation to find percentiles?
                    # The linear interpolation formula for percentiles is:
                    # linear: i + (j - i) * fraction, where fraction is the
                    # fractional part of the index surrounded by i and j.
                    try:
                        len(largs)
                        largs.sort(key=None, reverse=False)

                        # identify quartile position
                        q1 = float((len(largs) + 1) / 4)

                        q3 = float((3 * (len(largs) + 1)) / 4)
                        # Q1: Interpolate between values:
                        if not isinstance(q1, int):
                            pos1, pos2 = largs[int(q1)], largs[int(q1) - 1]
                            q1 = float(pos2 + (pos1 - pos2) * 0.75)

                        else:
                            q1 = largs[q1]
                        # Q3: Interpolate between values:s
                        if not isinstance(q3, int):
                            pos1, pos2 = largs[int(q3)], largs[int(q3) - 1]
                            q3 = float(pos2 + (pos1 - pos2) * 0.25)

                        else:
                            q3 = largs[q3]

                        if len(largs) % 2:
                            largs = [float(nearest(q1, largs)),
                                     float(nearest(q3, largs))]
                        else:
                            largs = [float(q1), float(q3)]
                        print(largs)

                    except Exception:
                        print("ERROR")
