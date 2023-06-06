print("Привіт, я програма-скорочувач, можеш вставити якийсь текст, а я спробую скоротити його.")

# Ввод від користувача
user_input = input("Вставляй текст: ")

while user_input.lower() != "кінець":
    # Перетворюємо введений текст в список символів
    input_list = list(user_input)

    # Удаляємо символи в лапках
    for i in input_list:
        if "(" in input_list and ")" in input_list:
            del input_list[input_list.index("(") - 1:input_list.index(")") + 1]

    # Обʼєднуємо назад в строку і видяляємо лишні пробіли
    result_string = "".join(input_list).strip()

    # Результат
    print("Результат:", result_string)

    # Новий ввод від користувача
    user_input = input("Вставляй далі текст або надрукуй 'кінець', для виходу: ")

print("До зустрічі")