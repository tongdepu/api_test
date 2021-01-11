import json

data = {
    'name': 'wangwu',
    'liebiao': [1, 2, 3, 4],
    'yuanzu': (1, 2, 3)
}
with open('json_test.txt', 'w+') as f:
    json.dump(data,f)

with open('json_test.txt') as f:
    print(json.load(f))


