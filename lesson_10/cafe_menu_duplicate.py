# этот код выполняется как когда файл импортируется (становится модулем),
# так и когда запускается как главный (__main__)
MENU = [
    1, 2, 3, 4, 5
]


# этот код не будет выполнен пока не вызовется функция
def my_function():
    print(10)
    return 100


# этот код не будет выполнен когда файл импортируется,
# но будет выполнен, когда файл запускается как главный
if __name__ == '__main__':
    print(__name__)
