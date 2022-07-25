from algorithms import best_fit, worst_fit, first_fit, next_fit
from data import data, entry


process = entry()
processLength = len(process)
best_fit(data(), len(data()), process, processLength)
worst_fit(data(), len(data()), process, processLength)
first_fit(data(), len(data()), process, processLength)
next_fit(data(), len(data()), process, processLength)
