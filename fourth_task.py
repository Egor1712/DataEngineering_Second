import pickle
import json

with open('./58/fourth_task_products.json', 'rb') as file:
    products = pickle.load(file)

with open('./58/fourth_task_updates.json', 'r', encoding='utf-8') as file:
    updates = json.load(file)

products_map = dict(map(lambda p: (p['name'], p), products))

for update in updates:
    product = products_map[update['name']]
    method = update['method']
    param = update['param']
    if method == 'add':
        product['price'] += param
    if method == 'sub':
        product['price'] -= param
    if method == 'percent+':
        product['price'] = product['price'] * (1 + param)
    if method == 'percent-':
        product['price'] = product['price'] * (1 - param)

with open('./results/fourth_task.pkl', "wb") as file:
    pickle.dump(products, file)

