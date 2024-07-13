def ft_statistics(*args: any, **kwargs: any) -> None:
#your code here
    lst = ['mean', 'median', 'variance', 'std', 'quartile']
    fct = 0
    idx = 0
    ret = 0
    i = 0
    ret_lst = []

    args = list(args)
    for key in kwargs:
        for i in range(len(lst)):
            if kwargs[key] == lst[i]:
                idx = i
                if idx == 0:
                    for arg in args:
                        ret += arg
                    if len(args):
                        ret = ret / len(args)
                        print(ret)
                    else:
                        print('ERROR')

                elif idx == 1:
                    """The median is a measure of central tendency that represents the middle value of a dataset when it is ordered
                    from smallest to largest. If the dataset contains an odd number of observations, the median is the middle value.
                    If the dataset contains an even number of observations, the median is the average of the two middle values."""
                    nlist = sorted(args)
                    if len(nlist) % 2:
                        index = len(nlist) / 2
                        ret = nlist[int(index)]
                        print(ret)
                    else:
                        index = len(nlist) / 2
                        if index:
                            ret = (nlist[int(index - 1) + nlist[int(index)]]) / 2
                            print(ret)
                        else:
                            print("ERROR")
                
                elif idx == 2 or idx == 3:
                    """The standard deviation is a measure of the amount of variation or dispersion in a set of values.
                    It quantifies how much the values in a dataset deviate from the mean (average) of the dataset.
                    Variance is a measure of the dispersion or spread of a set of data points.
                    It quantifies how much the values in a dataset differ from the mean of the dataset."""

                    """Calculate the Mean:"""
                    mean = 0
                    for arg in args:
                        mean += arg
                    mean = mean / len(args)
                    """Calculate Each Deviation from the Mean and Square It:"""
                    for arg in args:
                        ret_lst.append((arg - mean) ** 2)
                    """Calculate the Mean of These Squared Deviations:"""
                    nmean = 0

                    for item in ret_lst:
                        nmean += item
                    nmean = nmean / len(ret_lst)
                    if idx == 3:
                        """Take the Square Root:"""
                        ret = nmean ** 0.5
                        print(ret)
                    print(nmean)

                elif idx == 4:
                    """Calculating quartiles is a common task in statistics, often used to divide a dataset into four equal parts.
                    Quartiles provide information about the spread and distribution of data. There are three main quartiles:
                    First Quartile (Q1): Also known as the lower quartile, it divides the lowest 25% of the data from the rest.
                    Second Quartile (Q2): This is the median of the dataset, dividing it into two halves.
                    Third Quartile (Q3): Also known as the upper quartile, it divides the highest 25% of the data from the rest."""
                    nlist = sorted(args)

                    if len(nlist):
                        """identify quartile position"""
                        q1 = (25 / 100) * (len(nlist) + 1)
                        q2 = (50 / 100) * (len(nlist) + 1)
                        q3 = (25 / 100) * (len(nlist) + 1)
                        """Q1: Interpolate between values:"""
                        x, y = int(q1), int(q1)+1
                        ret_lst.append(int(nlist[x] + (0.75 * (nlist[y] - nlist[x]))))
                        """Q2: Simply the median value:"""
                        if len(nlist) % 2:
                            index = int(len(nlist) / 2)
                            ret_lst.append(nlist[index])
                        else:
                            index = int(len(nlist) / 2)
                            ret_lst.append(int(nlist[index] + nlist[index] + 1) / 2)
                        """Q3: Interpolate between values:"""
                        i, j = int(q3), int(q3)+1
                        ret_lst.append(int(nlist[i] + (0.25 * (nlist[j] - nlist[i]))))

                        for item in ret_lst:
                            if item in nlist:
                                nlist.remove(item)
                        if len(nlist):
                            nlist.remove(nlist[0])
                            nlist.remove(nlist[len(nlist)-1])
                            nlist = [float(item) for item in nlist]
                            print(nlist)
                        else:
                            print("ERROR")
                    else:
                        print("ERROR")
                        

    