import numpy as np


def from_str(str_json):
    s_json = str(str_json[1:-1])
    splitt = s_json.split(",")
    clusters = []
    cluster_read = False
    for s in splitt:
        current_cluster = cluster_read
        if '[' in s:
            s = s[1:]
            cluster_read = True
        if ']' in s:
            s = s[:-1]
            cluster_read = False

        if not current_cluster:
            clusters.append([int(s)])
        else:
            clusters[-1].append(int(s))
    return clusters


def create_matrix(str_json: str):
    matrix = []
    n = 0

    clusters = from_str(str_json)
    for cluster in clusters:
        n += len(cluster)
    for i in range(n):
        matrix.append([1] * n)

    bad_case = []
    for cluster in clusters:
        for bad_elem in bad_case:
            for elem in cluster:
                matrix[elem - 1][bad_elem - 1] = 0
        for elem in cluster:
            bad_case.append(int(elem))

    return np.array(matrix)


def andmatrix(matrix1, matrix2):
    n, m = matrix1.shape
    matrix = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            matrix[i][j] = matrix1[i][j] * matrix2[i][j]

    return matrix


def ormatrix(matrix1, matrix2):
    n, m = matrix1.shape
    matrix = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            matrix[i][j] = max(matrix1[i][j], matrix2[i][j])

    return matrix


def ans(matrix, est1, est2):
    strin = {}

    rows, cols = matrix.shape
    exclude = []
    for i in range(rows):
        if i + 1 in exclude:
            continue
        strin[i + 1] = [i + 1]
        for j in range(i + 1, cols):
            if matrix[i][j] == 0:
                strin[i + 1].append(j + 1)
                exclude.append(j + 1)

    res = []
    for k in strin:
        if not res:
            res.append(strin[k])
            continue
        for i, elem in enumerate(res):
            if np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1]) and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1]):
                for c in strin[k]:
                    res[i].append(c)
                    break
            if np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1]) or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1]):
                res = res[:i] + strin[k] + res[i:]
                break
        res.append(strin[k])

    fin = []
    for r in res:
        if len(r) == 1:
            fin.append(r[0])
        else:
            fin.append(r)
    return str(fin)


def solve(string1, string2):
    m1 = create_matrix(string1)
    m2 = create_matrix(string2)

    mand = andmatrix(m1, m2)
    mandt = andmatrix(np.transpose(m1), np.transpose(m2))
    mor = ormatrix(mand, mandt)
    cl = ans(mor, m1, m2)
    return cl


if __name__ == "__main__":
    string1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    string2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    results = solve(string1, string2)
    print(results)

