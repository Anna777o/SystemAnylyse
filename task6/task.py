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

def sz(data):
    res = 0
    for item in data:
        if isinstance(item, list):
            for l2 in item:
                res += 1
        else:
            res += 1
    return res

def cre_m(data)t:
    if (type(data) != list):
        data = json.loads(data)
    res = []
    for item in data:
        if isinstance(item, list):
            item_sum = 0
            for l2 in item:
                item_sum += int(l2)
            value = item_sum/len(item)
            for l2 in item:
                res.append(value)
        else:
            res.append(int(item))
    return res

def task(*rankings: str):
    m = len(rankings)
    rL = [json.loads(r) for r in rankings]
    # [[1, [2, 3], 4, [5, 6, 7], 8, 9, 10], [[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]]
    ni = [sz(r) for r in rL]
    n = ni[0]
    matrix = np.array([np.array(cre_m(r)) for r in rL]).T
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
