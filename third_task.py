import json
import os

import msgpack
import pandas as pd


data = pd.read_json('58/third_task.json')
data = data.groupby('name').price.agg(['min','max','mean'])

datas = []
for key, row in data.iterrows():
    datas.append({
        'name': key,
        'min': row['min'],
        'max': row['max'],
        'avg': row['mean']
    })

with open('./results/third.task.json', 'w+', encoding='utf-8') as file:
    json.dump(datas, file, ensure_ascii=False)


with open('./results/third.task.msgpack', 'wb') as f:
    msgpack.dump(datas, f)

file_size = os.path.getsize('./results/third.task.json')
msgpack_file_size = os.path.getsize('./results/third.task.msgpack')

print(f'File size difference is [{abs(file_size - msgpack_file_size)}] bytes')