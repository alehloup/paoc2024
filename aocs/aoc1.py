from collections import Counter


def read_lists() -> (list, list):
    with open("./inputs/aoc1_easy.txt") as f:
        lines = f.readlines()

    list1, list2 = [], []
    for line in lines:
        el1, el2 = line.split()
        list1.append(int(el1))
        list2.append(int(el2))

    list1.sort()
    list2.sort()

    return list1, list2


def aoc1_easy():
    list1, list2 = read_lists()
    print(
        sum(abs(list1[i] - list2[i]) for i in range(len(list1)))
    )


def aoc1_hard():
    list1, list2 = read_lists()
    counts = Counter(list2)
    print(
        sum(el * counts[el] for el in list1)
    )
