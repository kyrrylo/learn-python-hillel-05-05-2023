# from datetime import datetime, date, time, timedelta  # с таким импортом пишется меньше кода

import datetime

if __name__ == '__main__':
    date = datetime.date(2023, 8, 5)
    time = datetime.time(9, 0, 0)
    print(type(date), date)
    print(type(time), time)
    print(datetime.datetime.now())
    print(datetime.datetime.today().date())

    x = datetime.datetime.now()
    print(type(x), x)

    # метод combine позволяет объединить дату и время в одном объекте
    x = datetime.datetime.combine(date, time)
    print(type(x), x)

    # обратно из типа данных datetime можно достать дату с помощью метода date()
    x_date = x.date()
    print(type(x_date), x_date)

    # обратно из типа данных datetime можно достать время с помощью метода time()
    x_time = x.time()
    print(type(x_time), x_time)

    print(type(x_time.hour), x_time.hour)
    print(type(x_time.minute), x_time.minute)

    # Типы данных библиотеки datetime
    # datetime (сообразно названию библиотеки, тут можно запутаться)
    # date
    # time
    # timezone (редко используется)
    # timedelta

    # date можно сравнивать с date
    # datetime можно сравнивать с datetime
    # time можно сравнивать с time

    expiration_date = datetime.date(year=2023, month=7, day=11)
    today = datetime.datetime.today()
    if expiration_date > today.date():
        print('Expiration date еще не наступил')
    else:
        print('Expiration date еще уже прошёл')

    if datetime.datetime.combine(expiration_date, datetime.time(0, 0, 0)) > today:
        print('Expiration date еще не наступил')
    else:
        print('Expiration date еще уже прошёл')


    datetime_str = '2023-08-05'

    # strptime конвертирует строку со временем в объект datetime
    x = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    print(type(x), x)

    datetime_str = '2023-08-05 09:15:00'
    x = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    print(type(x), x)

    x_date = x.date()
    x_time = x.time()
    print(type(x_date), x_date)
    print(type(x_time), x_time)

    # из str -> datetime с помощью метода strptime()
    # из datetime -> date с помощью метода date()
    # из datetime -> time с помощью метода time()
    # из date и/или time -> datetime с помощью метода combine()
    # из datetime/date/time -> str с помощью метода strftime()

    print(x_date.strftime('%d %B %y'))
    print(x_time.strftime('%H hours %M minutes %S seconds'))
    print(x.strftime('%H hours %M minutes %S seconds %d %B %y'))

    # timedelta
    result = today + datetime.timedelta(days=30.5) - datetime.timedelta(hours=2)
    print(type(result), result, result.weekday())
    # weekday
    # 0 - Monday, 1 - Tuesday... 4 - Friday
    friend_birthday = x + datetime.timedelta(days=365)
    how_much_time_until_friend_birthday = friend_birthday - today
    print(type(how_much_time_until_friend_birthday), how_much_time_until_friend_birthday)
