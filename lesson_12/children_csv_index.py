import csv
from read_csv import open_csv_file_dict


def create_index(all_data: list, column_name: str):
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


if __name__ == '__main__':
    children_data = open_csv_file_dict('children.csv', to_print=False)
    age_index = create_index(children_data, 'age')
    print(type(age_index), age_index)

    group_index = create_index(children_data, 'group')
    print(type(group_index), group_index)
