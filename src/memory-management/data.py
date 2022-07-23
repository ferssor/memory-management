from pathlib import Path


def data():
    path = Path("../../data") / "memory.txt"
    raw = open(path, "r+")
    storage = []
    data = raw.read()
    values = data.split()
    for i in values:
        storage.append(i)

    return storage


print(data())
