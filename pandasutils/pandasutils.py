import pandas as pd


def frequency(dataframe, column):
    """
    Creates a dataframe that gives the total and frequencies per item.
    Dataframe output example:

        total  freq
    18     22  0.44
    17      9  0.18
    19      7  0.14
    20      4  0.08
    21      3  0.06
    25      2  0.04
    23      2  0.04
    24      1  0.02

    :param dataframe:
    :param column:
    :return: dataframe
    """
    s_ini = dataframe[column]
    s_sum = s_ini.value_counts()
    total = sum(s_sum)
    freq = [x / total for x in s_sum]

    df = pd.DataFrame({
        'total': s_sum,
        'freq': freq,
    })

    return df


def frequency_by_natural_order(dataframe, column):
    """
    Create a dataframe that gives the total by natural order, frequencies,
    accumulated total and frequency per item.
    Dataframe output example:

        tot  freq  tot_ac  freq_ac
    17    9  0.18       9     0.18
    18   22  0.44      31     0.62
    19    7  0.14      38     0.76
    20    4  0.08      42     0.84
    21    3  0.06      45     0.90
    23    2  0.04      47     0.94
    24    1  0.02      48     0.96
    25    2  0.04      50     1.00

    :param dataframe:
    :param column:
    :return: dataframe
    """
    s_ini = dataframe[column]
    s_sum = s_ini.value_counts()
    s_sort = s_sum.sort_index()
    s_tot = s_sort.sum()

    t = 0
    ft = 0
    tot_ac = []
    freq = []
    freq_ac = []
    for x in s_sort:
        f = x / s_tot
        freq.append(f)

        ft += f
        freq_ac.append(ft)

        t += x
        tot_ac.append(t)

    df = pd.DataFrame({
        'tot': s_sort,
        'freq': freq,
        'tot_ac': tot_ac,
        'freq_ac': freq_ac,
    })

    return df


def frequency_by_buckets(dataframe, column, r, ini, end):
    """
    Creates a dataframe with cumulative values within a range, which are called
    buckets.
    Dataframe output example:

               tot  freq  tot_ac  freq_ac
    [40, 50)     8  0.16       8     0.16
    [50, 60)    22  0.44      30     0.60
    [60, 70)     8  0.16      38     0.76
    [70, 80)     6  0.12      44     0.88
    [80, 90)     5  0.10      49     0.98
    [90, 100)    1  0.02      50     1.00

    :param dataframe:
    :param column:
    :param r: the range between values
    :param ini: where the interval begin
    :param end: where the interval end
    :return: dataframe
    """

    s_ini = dataframe[column]

    buckets = [x for x in range(ini, end+r, r)]
    s_buckets = pd.cut(s_ini, buckets, right=False)

    s_buckets = s_buckets.value_counts()
    s_buckets = s_buckets.sort_index()
    s_tot = sum(s_buckets)

    t = 0
    ft = 0
    tot_ac = []
    freq = []
    freq_ac = []
    for x in s_buckets:
        f = x / s_tot
        freq.append(f)

        ft += f
        freq_ac.append(ft)

        t += x
        tot_ac.append(t)

    df = pd.DataFrame({
        column: s_buckets,
        'freq': freq,
        'tot_ac': tot_ac,
        'freq_ac': freq_ac,
    })

    return df
