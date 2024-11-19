import json

import numpy
import numpy as np

matrix = np.load('./58/first_task.npy')

sum = np.int64(0)
sum_md = np.int64(0)
sum_sd = np.int64(0)
min = matrix[0][0]
max = matrix[0][0]

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        item = matrix[i][j]
        sum += item
        if i == j:
          sum_md += item
        if matrix.shape[1] - i - 1 == j:
            sum_sd += item
        if item < min:
            min = item
        if item > max:
            max = item


data = {
    'sum': float(sum),
    'avr': float(sum / matrix.size),
    'sumMD': float(sum_md),
    'avrMD': float(sum_md / matrix.shape[0]),
    'sumSD': float(sum_sd),
    'avrSD': float(sum_sd / matrix.shape[0]),
    'max': float(max),
    'min': float(min)
}
with open('./results/first_task.json', 'w+') as file:
    json.dump(data, file)

norm = matrix / sum
np.save('./results/first_task.npy', norm)
