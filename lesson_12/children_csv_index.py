import csv
from read_csv import open_csv_file_dict

# from uuid import uuid4
# uuid4() альтернативный вариант создания уникальных айдишников для индексов


def create_index(all_data: list, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список записей из all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


def create_position_id_index(all_data: list, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем, не дублируя записи
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список порядкового номера записей в all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


def print_position_id_index(all_data: list, position_index: dict):
    """
    В удобном формате выводит на экран содержимое переданного индекса по данным
    :param all_data: данные, по которым построен индекс
    :param position_index: индекс, где значения - списки порядковых номеров
    :return: ничего, функция только выводит на экран
    """
    for index_key, position_values in position_index.items():
        print(f'Записи со значением {index_key}')
        for i in position_values:
            print('  ', all_data[i])


if __name__ == '__main__':
    # открываем csv файл и считываем данные из него
    children_data = open_csv_file_dict('children.csv', to_print=False)

    # unique id (в качестве ссылок на данные, чтобы их не дублировать
    # дублирование чревато дополнительным занимаемым местом,
    # а так же неконсистентность редактирования данных
    # (редактировании одной копии не редактирует остальные)
    # консистентность в этом примере работает, однако при разделении
    # на разные файлы может не работать
    print(children_data[4])

    # создаём индекс по колонке age
    age_index = create_index(children_data, 'age')
    # выводим на экран содержимое индекса
    print(type(age_index), age_index)

    print('Строится индекс по возрастам...')
    age_position_id_index = create_position_id_index(children_data, 'age')
    input('Нажмите Enter чтобы увидеть индекс по возрастам...')
    print_position_id_index(children_data, age_position_id_index)

    print('Меняем фамилию Liam...')
    children_data[0]['lastName'] = 'McGreg'
    input('Нажмите Enter чтобы увидеть индекс по возрастам с изменённой фамилией...')
    print_position_id_index(children_data, age_position_id_index)

    # выводим на экран содержимое индекса
    print(type(age_index), age_index)

    # создаём индекс по колонке group
    group_index = create_index(children_data, 'group')
    # выводим на экран содержимое индекса
    print(type(group_index), group_index)
