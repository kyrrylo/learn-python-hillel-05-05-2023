import csv
import random


ALHABET = 'qwertyuiopasdfghjklzxcvbnm'

# csv = comma separated values
# значения, разделённые запятой

# pandas - основная библиотека для работы с csv файлами
# csv библиотека - базовая, со своими "моментами"

def open_csv_file_dict(filename, to_print=True):
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        if to_print:
            print(type(reader), reader)
            for row in rows:
                print(type(row), row)
        return rows

def open_csv_file(filename):
    # newline='' потому что так "любит" библиотека csv
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file)
        print(type(reader), reader)
        for row in reader:
            print(type(row), row)
            if row[0] == '6 Feb':
                print(row[2])

def generate_csv_rows() -> tuple:
    rows = list()
    header = ['letter', 'float', 'integer']
    for i in range(100):
        random_letter = random.choice(ALHABET)
        random_float = round(random.random() * 100, 2)
        random_integer = random.randint(0, 100)
        rows.append([random_letter, random_float, random_integer])
    # return (rows, header) равноценная запись
    return rows, header


def write_csv_rows(filename: str, rows: list, header: list):
    with open(filename, newline='', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        print(type(writer), writer)
        writer.writerow(header)
        writer.writerows(rows)


def generate_csv_dict_rows() -> list:
    rows = list()
    for i in range(100):
        random_letter = random.choice(ALHABET)
        random_float = round(random.random() * 100, 2)
        random_integer = random.randint(0, 100)
        rows.append({'letter': random_letter, 'float': random_float, 'integer': random_integer})
    return rows

def write_csv_dict_rows(filename: str, rows: list):
    with open(filename, newline='', mode='w') as csv_file:
        if rows:
            header = list(rows[0].keys())
        writer = csv.DictWriter(csv_file, header)
        print(type(writer), writer)
        writer.writeheader()
        writer.writerows(rows)


def optimal_write_dict_rows(filename: str):
    with open(filename, newline='', mode='w') as csv_file:
        header = ['letter', 'float', 'integer']
        writer = csv.DictWriter(csv_file, header)
        writer.writeheader()
        for i in range(100):
            random_letter = random.choice(ALHABET)
            random_float = round(random.random() * 100, 2)
            random_integer = random.randint(0, 100)
            row = {'letter': random_letter, 'float': random_float, 'integer': random_integer}
            writer.writerow(row)


if __name__ == '__main__':
    open_csv_file('simple_csv_file.csv')
    open_csv_file_dict('simple_csv_file.csv')

    generated_rows, generated_header = generate_csv_rows()
    write_csv_rows('random_csv_file_no_headers.csv', generated_rows, generated_header)

    generated_dict_rows = generate_csv_dict_rows()
    write_csv_dict_rows('random_csv_file_with_headers.csv', generated_dict_rows)

    optimal_write_dict_rows('optimal_dict_rows.csv')