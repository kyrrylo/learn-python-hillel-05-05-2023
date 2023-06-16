import json
import os


if __name__ == '__main__':
    if not os.path.isfile('children.json'):
        print('Программа не запустится без файла children.json!')
        exit(-1)

    children_data = json.load(open('children.json'))['children']
    print(children_data)

    age_index = dict()
    for data in children_data:
        if data['age'] not in age_index:
            age_index[data['age']] = list()
        age_index[data['age']].append(data)

    print(age_index)