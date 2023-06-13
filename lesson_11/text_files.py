import os

# Файлы бывают двух типов
# Текстовые
# Бинарные (.exe, .png, .jpg, .dll, .zip, .rar, .7z, .bin, .mp4, .mov)

def file_read_method(f_wrapper, chars=None):
    print('I demonstrate read() function effect on file')
    s = f_wrapper.read(chars)
    print(type(s), s)


def file_readlines_method(f_wrapper):
    print('I demonstrate readlines() function effect on file')
    x = f_wrapper.readlines()
    print(type(x), x)
    for line in x:
        print(line.strip().lower())


def file_readline_method(f_wrapper):
    """
    Метод readline за один вызов читает одну строку
    :param f_wrapper:
    :return:
    """
    print('I demonstrate readline() function effect on file')
    x = f_wrapper.readline()
    while x:
        print(type(x), x.strip())
        x = f_wrapper.readline()


def file_write_method(f_wrapper):
    f_wrapper.write('This is a new string\n')
    f_wrapper.write('This is another new string\n')

    source_file = open('my_text_file.png', mode='r', encoding='utf-8')
    f_wrapper.write(source_file.read())

    f_wrapper.seek(20)
    # seek работает только на чтение, чтобы записать в середину, нужно прочитать содержимое файла,
    # поменять строчку внутри Python программы, после чего записать файл заново (перезаписать)
    f_wrapper.write('I am appended in the end')


if __name__ == '__main__':
    # r - read чтение
    # w - write запись
    # a - append добавление

    # для кириллицы пользоваться encoding='utf-8'
    f = open('my_text_file.png', mode='r', encoding='utf-8')

    # три метода чтения
    # f.read()
    # f.readlines()
    # f.readline()
    print(f)
    print(type(f))  # Text текстовый IO input/output Wrapper обёртка (объект для управления файлом)

    print('Is file readable?', f.readable())
    print('Is file writable?', f.writable())

    file_read_method(f_wrapper=f, chars=10)
    # Чтобы читать файл с начало, нужно перезагрузить сохранённый прогресс прочтённого
    # как закладка в книге
    # f = open('my_text_file.png', mode='r', encoding='utf-8')
    # если не переоткрывать файл, то можно воспользоваться функцией seek - "перемещает закладку книги на указанную позицию"
    f.seek(0)
    file_readlines_method(f_wrapper=f)

    # urllib, requests для открытия web-страниц
    # html/xml. библиотеки: xml.tree | Beautiful Soup (web-scraping)
    f.seek(0)
    file_readline_method(f_wrapper=f)

    print('Запись в файл', '=' * 10)
    # в режиме mode=r мы не можем открывать несуществующие файлы
    filename = 'new_text_file.jpg'
    if os.path.isfile(filename):
        print(f'Чтение файла {filename}...')
        f = open(filename, mode='r', encoding='utf-8')
    else:
        # режим a(ppend) и w(rite) создают файлы, если таких нет
        print(f'Такого файла нет: {filename}, создаём файл...')
        f = open(filename, mode='a', encoding='utf-8')

    print(f'Открытие файла {filename}...')
    # открытие файлов в режиме a(ppend) не меняет их содержимого
    # открытие файлов в режиме w(rite) полностью очищает содержимое файла


    # вместо конструкции f = open()... нужно всегда (с файлами) пользоваться with-as
    # with <объявление значения контроллируемой переменной> as <имя переменной, куда это значение записывается>
    with open(filename, mode='w', encoding='utf-8') as f:
        with open('my_text_file.png', mode='r', encoding='utf-8') as another_f:
            print('Is file readable?', f.readable())
            print('Is file writable?', f.writable())

            file_write_method(f)

            f.writelines(['a', 'b', 'c'])  # крайне редко используется, не ставит переноса на новую строку чем неудобен
            f.write('\n' + '\n'.join(['a', 'b', 'c']))
