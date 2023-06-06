def remove_text(string):
    while True:
        # Находим 1 скобку
        open_index = string.find(open_bracket)
        if open_index == -1:
            break

        # Находим 2 скобку
        close_index = string.find(close_bracket, open_index)
        if close_index == -1:
            break

        # Удаляем все лишнее :)
        string = string[:open_index] + string[close_index + 1:]
    return string


if __name__ == "__main__":
    # Получаем строку
    user_string = input("Введите строку: ")

    # Устанавливаем значения
    open_bracket = '('
    close_bracket = ')'

    # Вызываем ф и удаляем скобки и значения между ними
    user_string = remove_text(user_string)

    # Результат
    print(f'Строка без символов между скобками: {user_string}')