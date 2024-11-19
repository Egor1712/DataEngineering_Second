import numpy as np
import os

matrix = np.load('./58/second_task.npy')

x = []
y =[]
z =[]

variant = 58

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        item = matrix[i][j]
        if item > 500 + variant:
            x.append(i)
            y.append(j)
            z.append(item)


np.savez('./results/second_task.npz', x,y,z)
np.savez_compressed('./results/second_task_compressed.npz', x,y,z)

file_size = os.path.getsize('./results/second_task.npz')
compressed_file_size = os.path.getsize('./results/second_task_compressed.npz')

print(f'File size difference is [{abs(file_size - compressed_file_size)}] bytes')