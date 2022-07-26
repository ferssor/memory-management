from tabulate import tabulate
from data import data


def worst_fit(blockSize: int, blockLength: int, processSize: int, processLength: int):
    allocation = [-1] * processLength

    for i in range(processLength):
        worstId = -1
        for j in range(blockLength):
            if blockSize[j] >= processSize[i]:
                if worstId == -1:
                    worstId = j
                elif blockSize[worstId] < blockSize[j]:
                    worstId = j

        if worstId != -1:
            allocation[i] = worstId
            blockSize[worstId] -= processSize[i]

    print("Worst-fit")
    final_allocation(processLength, processSize, allocation)
    memory(blockSize)


def first_fit(blockSize: int, blockLength: int, processSize: int, processLength: int):
    allocation = [-1] * processLength

    for i in range(processLength):
        for j in range(blockLength):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]

                break

    print("First-fit")
    final_allocation(processLength, processSize, allocation)
    memory(blockSize)


def best_fit(blockSize: int, blockLength: int, processSize: int, processLength: int):
    allocation = [-1] * processLength

    for i in range(processLength):

        bestId = -1
        for j in range(blockLength):
            if blockSize[j] >= processSize[i]:
                if bestId == -1:
                    bestId = j
                elif blockSize[bestId] > blockSize[j]:
                    bestId = j

        if bestId != -1:
            allocation[i] = bestId
            blockSize[bestId] -= processSize[i]

    print("Best-fit")
    final_allocation(processLength, processSize, allocation)
    memory(blockSize)


def next_fit(blockSize: int, blockLength, processSize, processLength):
    allocation = [-1] * processLength
    j = 0
    t = blockLength - 1
    for i in range(processLength):
        while j < blockLength:
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]

                t = (j - 1) % blockLength
                break
            if t == j:
                t = (j - 1) % blockLength
                break

            j = (j + 1) % blockLength

    print("Next-fit")
    final_allocation(processLength, processSize, allocation)
    memory(blockSize)


def final_allocation(processLength: int, processSize: int, allocation: int):
    result = []
    index = []
    process = []
    value = []

    for i in range(processLength):
        if allocation[i] != -1:
            value = allocation[i] + 1
            result.append(value)
        else:
            result.append("Not Allocated")

        index.append(i + 1)
        process.append(processSize[i])

        table = {"Process no.": index, "Process Size": process, "Block no.": result}

    return print(
        tabulate(
            table, headers="keys", tablefmt="grid", stralign="center", numalign="center"
        )
    )


def memory(block):
    sub = []
    for i in range(len(data())):
        sub.append(data()[i] - block[i])
    table = {
        "Initial memory": data(),
        "Current memory": block,
        "Diff": sub,
    }

    return print(
        tabulate(
            table, headers="keys", tablefmt="grid", stralign="center", numalign="center"
        )
    )
