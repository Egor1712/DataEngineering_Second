import csv
import json
import os.path
import pickle
import sys

import msgpack
import pandas as pd

data = pd.read_csv('./58/all_youtube_analytics.csv', sep=',')

columns = ['views', 'comments', 'likes', 'dislikes', 'shares', 'subscribersGained', 'subscribersLost',
           'averageViewPercentage']

def convert_to_object(series):
    result = {}
    for col in columns:
        result[col] = series[1][col]
    return result

data = data.loc[:, data.columns.intersection(columns)]

characteristics = []
for column in columns:
    characteristics.append({
        'name': column,
        'max': data[column].max(),
        'min': data[column].min(),
        'average': data[column].mean(),
        'sum': data[column].sum(),
        'std': data[column].std()
    })

items = list(map(convert_to_object, data.iterrows()))

with open('./results/fifth_task.json', 'w+') as file:
    json.dump(characteristics, file)

with open('./results/fifth_task_dataset.json', 'w+') as file:
    json.dump(items, file)

with open('./results/fifth_task_dataset.pkl', 'wb') as file:
    pickle.dump(items, file)

with open('./results/fifth_task_dataset.msgpack', 'wb') as file:
    msgpack.dump(items, file)

with open('./results/fifth_task_dataset.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for item in items:
        writer.writerow(list(map(lambda col: item[col], columns)))

extensions = ['json', 'pkl', 'csv', 'msgpack']

min = sys.maxsize
max = 0
for ext in extensions:
    filename = f'./results/fifth_task_dataset.{ext}'
    size = os.path.getsize(filename) / 1024 / 1024
    print(f'Size of file {filename} is {size:.2f} MB')
    if size > max:
        max = size
    if size < min:
        min = size

print(fr'Max size is [{max:.2f}] MB')
print(fr'Min size is [{min:.2f}] MB')
