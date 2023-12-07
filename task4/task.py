import numpy as np


def solves():
    # создаем все варианты сумм и производных
    sums = set()
    mul = set()
    for l in range(1, 7):
        for r in range(1, 7):
            sums.add(l + r)
            mul.add(l * r)
    sums = sorted(sums)
    mul = sorted(mul)
    # sums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # cоздаем словари для определения индексов в таблице 
    sum_d = {num: sums.index(num) for num in sums}
    mul_d = {num: mul.index(num) for num in mul}
    #sum_d = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10}
    # матрица с количествами комбинаций
    сombinations = np.zeros((len(sums), len(mul)))
    for l in range(1, 7):
        for r in range(1, 7):
            сombinations[sum_d[l + r], mul_d[l * r]] += 1

    comb = сombinations / 36

    cp_A = np.sum(comb, axis=1)  # матрица вероятностей для события A
    cp_B = np.sum(comb, axis=0)  # матрица вероятностей для события B


    H_AB = -np.sum(comb * np.log2(comb, where=np.abs(comb) > 1e-4))
    H_A = -np.sum(cp_A * np.log2(cp_A, where=np.abs(cp_A) > 1e-4))
    H_B = -np.sum(cp_B * np.log2(cp_B, where=np.abs(cp_B) > 1e-4))
    Ha_B = H_AB - H_A
    I_AB = H_B - Ha_B
    return [round(num, 4) for num in [H_AB, H_A, H_B, Ha_B, I_AB]]

print(solves())

