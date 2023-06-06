a = input("Please, input your string\n-> ")
c = list(a)
# условие while находит в тексте скобки и слова и удаляет их
while "(" in c:
    s1 = c.index("(")
    while c[s1] != ")":
        c.pop(s1)
    c.remove(")")
    if c[s1 - 1] == " ":  # "s1-1" чтобы удалить пробел
        c.pop(s1 - 1)
print(''.join(c))