# Програма для скорочування строки
text = input("Введіть свою строку для скорочення: ")
# Змінна для запису результату
result = ""
# Змінна для пошуку пар дужок
delete = list()
# Цикл програми
for i in text:
    if i == "(":
        delete.append("(")
        result.replace("(", "")
    elif i == ")":
        if delete:
            delete.pop()
        else:
            result += i
    # Основна умова коли змінна Delete не є пустою вона не добавляє всі слідуючі символи,
    # Якщо наступний символ неє ")"
    elif not delete:
        result += i
# Виведення результату
print(result)