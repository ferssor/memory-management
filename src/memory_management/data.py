from pathlib import Path


def data():
    path = Path("../../data") / "memory.txt"
    raw = open(path, "r")
    storage = []
    data = raw.read()
    values = data.split()
    for i in values:
        storage.append(int(i))

    return storage


def entry():
    list = []
    n = int(input("Enter number of elements : "))

    for i in range(0, n):
        element = int(input("element {}: ".format(i + 1)))
        list.append(element)

    return list
