def get_nodes(graph):
    all_keys = []
    for key in graph:
        if key not in all_keys:
            all_keys.append(key)
        for elem in graph[key]:
            if elem not in all_keys:
                all_keys.append(elem)

    return all_keys, len(all_keys)


def create_matrix(graph, len):
    matrix = [[0 for _ in range(len)] for _ in range(len)]

    for i in graph:
        for j in graph[i]:
            matrix[int(i) - 1][int(j) - 1] = 1
            matrix[int(j) - 1][int(i) - 1] = -1

    return matrix

def task():
    graph = {'1':'2','2':['3','4'],'3':['5','6']}
    _, l = get_nodes(graph)
    matrix = create_matrix(graph, l)
    result = [[0 for _ in range(5)] for _ in range(l)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result[i][0] += 1
                for index, value in enumerate(matrix[j]):
                    if value == 1:
                        result[i][2] += 1
            if matrix[i][j] == -1:
                result[i][1] += 1
                for index, value in enumerate(matrix[j]):
                    if value == -1:
                        result[i][3] += 1
                    if value == 1 and index != i:
                        result[i][4] += 1
    print(result)

task()
