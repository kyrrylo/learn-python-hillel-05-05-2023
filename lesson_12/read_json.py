import json

# json библиотека совершает парсинг джсон файлов за нас
# Parsing | Парсинг - это процесс доставания важной информации из текстового файла


def read_text_file(filename):
    with open(filename, mode='r') as text_file:
        lines = text_file.readlines()
        line = int(lines[0])
        print(type(line), line)

        line = float(lines[1])
        print(type(line), line)

        line = list(lines[2])  # строка в список конвертируется неверно
        print(type(line), line)

        # line = dict(lines[3])  # строка в словарь не конвертируется
        # print(type(line), line)
        return lines


if __name__ == '__main__':
    text_file_lines = read_text_file('text.txt')
    # fp = file pointer, то что возвращает open()
    print('JSON')
    children_json_object = json.load(open('children.json'))
    print(type(children_json_object), children_json_object)
    print(type(children_json_object['boolean_value']), children_json_object['boolean_value'])

    json_object = json.load(open('this_is_definitely_not_json.exe'))
    print(type(json_object), json_object)

    json_object = json.loads(text_file_lines[2])
    print(type(json_object), json_object)

    json_object = json.loads(text_file_lines[3])
    print(type(json_object), json_object)

    json_object = json.loads("""
    {
    "json_key": 5,
    "json_key2": 10
}""")
    print(type(json_object), json_object)

    # load парсит текстовый файл в dict/ list
    # loads парсит строку в dict/list
    # dump из dict/list в текстовый файл
    # dumps из dict/list в str

    json.dump({"sun": "солнце", "moon": "луна"}, open('dictionary.json', mode='w'), indent=4)

    json.dump(children_json_object, open('new_children.json', mode='w'), indent=2, sort_keys=True)

    dumped_str = json.dumps({"sun": "солнце", "moon": "луна"})
    print(type(dumped_str), dumped_str)

    json_object = json.load(open('dictionary.json'))
    print(type(json_object), json_object)

    json.dump(["sun", "солнце", "moon", "луна"], open('list.json', mode='w'))

    dumped_str = json.dumps(["sun", "солнце", "moon", "луна"])
    print(type(dumped_str), dumped_str)
