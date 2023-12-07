import numpy as np
import json


def count_hk(data):
    res = []
    for item in data:
        if isinstance(item, list):
            res.append(len(item))
    return res


def count_Ts(data):
    res = 0
    for item in data:
        res += item ** 3 - item
    return res


def task(*rankings: str):
    m = len(rankings)
    rL = [json.loads(r) for r in rankings]
    # [[1, [2, 3], 4, [5, 6, 7], 8, 9, 10], [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]]
    n = 10
    matrix = [[1, 1.5], [2.5, 1.5], [2.5, 4], [4, 4.], [6, 4], [6, 6], [6, 7], [8, 9], [9, 9], [10, 9]]

    xi = np.sum(matrix, axis=1)
    xavg = xi.mean()
    sums = np.sum(np.square(xi - xavg))

    D = sums / (n - 1)
    hk = [count_hk(r) for r in rL]
    Ts = [count_Ts(h) for h in hk]
    Dmax = (m ** 2 * (n ** 3 - n) - m * np.sum(Ts)) / (12 * (n - 1))
    W = D / Dmax

    return round(W, 2)


str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
str2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
print(task(str1, str2))

