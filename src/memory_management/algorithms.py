from tabulate import tabulate


def worst_fit(blockSize: int, blockLenth: int, processSize: int, processLength: int):
    print(blockSize)
    allocation = [-1] * processLength

    for i in range(processLength):
        worstId = -1
        for j in range(blockLenth):
            if blockSize[j] >= processSize[i]:
                if worstId == -1:
                    worstId = j
                elif blockSize[worstId] < blockSize[j]:
                    worstId = j

        if worstId != -1:
            allocation[i] = worstId
            blockSize[worstId] -= processSize[i]

    print("Worst-fit")
    print(blockSize)
    final_allocation(processLength, processSize, allocation)


def first_fit(blockSize: int, blockLength: int, processSize: int, processLength: int):
    print(blockSize)
    allocation = [-1] * processLength

    for i in range(processLength):
        for j in range(blockLength):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]

                break

    print("First-fit")
    print(blockSize)
    final_allocation(processLength, processSize, allocation)


def best_fit(blockSize: int, blockLength: int, processSize: int, processLength: int):
    print(blockSize)
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
    print(blockSize)
    final_allocation(processLength, processSize, allocation)


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

    headers = ["Process no.", "Process Size", "Block no."]
    return print(tabulate(table, headers=headers, tablefmt="grid", stralign="center"))
