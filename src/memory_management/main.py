from algorithms import best_fit, worst_fit, first_fit
from data import data, entry


block = data()
process = entry()
blockLength = len(block)
processLength = len(process)
best_fit(block, blockLength, process, processLength)
worst_fit(block, blockLength, process, processLength)
first_fit(block, blockLength, process, processLength)
