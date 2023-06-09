# cafe_menu - модуль, раз мы его импортируем
import cafe_menu
# импортировать всё
# from cafe_menu_duplicate import *

from math import sqrt

# импортировать с переименованием во избежание конфликта имён
from cafe_menu_duplicate import MENU as DUPLICATE_MENU
from cafe_menu import MENU as REAL_MENU


if __name__ == '__main__':
    print(__name__)
    print(DUPLICATE_MENU)
    print(REAL_MENU)
