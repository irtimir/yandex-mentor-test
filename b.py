"""
Временная сложность:
O(nlog(n)) - сортировка list
O(n) - проверка нулей
Итоговая сложность: O(nlog(n)) + O(n) = O(nlog(n))

Пространственная сложность:
O(1) - проверяем только один элемент за итерацию
Итоговая сложность: O(1)
"""


def remove_zeros(seq):
    seq.sort(key=lambda x: not x)

    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == 0:
            seq.pop()
        else:
            break
