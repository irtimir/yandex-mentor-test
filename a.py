"""
Временная сложность:
O(n_seq2) - создаём set из seq2
O(seq1) - проверяем каждый элемент из seq1, содержится ли он в seq2
Итоговая сложность: O(N)

Пространственная сложность:
O(seq2) - дополнительно храним уникальный набор элементов из seq2
Итоговая сложность: O(N)
"""


def get_diff(seq1, seq2):
    res = set()
    seq2_set = set(seq2)

    for element in seq1:
        if element not in seq2_set:
            res.add(element)

    return res
