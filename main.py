# Задание: Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой).
#
# Реализацию пользовательского интерфейса студент может делать как ему удобнее,
# можно делать как параметры запуска программы (команда, данные),
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

import json
import time

time_tuple = time.localtime()
time_ = time.strftime("%d.%m.%Y, %H:%M:%S", time_tuple)

file_name = 'notes.json'
data = {}


def new_json():  # Создаем нвую заметку
    header = input('Название заметки:\n')

    body = input("заметка:\n")

    new_note = {header: [time_, body]}  # меняю формат записки в словарь

    data = load_json()  # подгружаю БД
    data.update(new_note)  # обновляю БД
    save_json(data)  # сохраняю БД


def save_json(data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # ensure_ascii=False Убрал кодировку русского языка



def load_json():
    with open(file_name, 'r', encoding='utf-8') as file:
        data.update(json.load(file))
    return data


def del_json():
    data = load_json()
    print(load_json().keys())  # Вывод ключей заметок
    data.pop(input('Какую заметку удалить?\nВведите название: '))
    # del data[input('Какую заметку удалить?\nВведите название: ')] # 2 вариант
    save_json(data)


def choice_key():
    data = load_json()

    data_list = [i for i in data]

    id = 1
    id_name = []
    for i in data:
        id_name.append(f'{id} - {i}')
        id += 1
    print(*id_name, sep='\n')

    id_or_name = input('Укажите id или название заметки: ')

    if str(id_or_name) in data.keys():  # поверка на начичие ключа
        key = id_or_name
        print(f'key = [{key}]')

    elif id_or_name.isdigit():  # проверка на число
        id = int(id_or_name)

        if id in range(1, len(data_list) + 1):  # проверка числа в диапозоне id
            key = data_list[id - 1]
            print(f'key = [{key}]')

        else:
            print('Неверный номер, попробуйте еще раз или введите название\n')
            edit_json()

    else:
        print('Неверный номер или название, попробуйте еще раз\n')
        edit_json()

    return key


def edit_json():
    data = load_json()
    key = choice_key()

    choise = int(input('Что будем менять?\n(1) Название;\n (2) Текст;\n  (3) Название и Текст;\n   (0) Отмена\n:'))
    if choise == 1:
        print("код 1")
        new_key = input("Введите новое название: ")
        data[new_key] = data.pop(key)


    elif choise == 2:
        print("код 2")
        data[key][0] = time_
        print(f'Текущие данные: {data[key]}')
        new_text = input("Введите новый текст.  Если передумали - оставьте поле пустым.\n: ")
        if new_text == "":
            new_text = data[key][1]
        else:
            data[key][1] = new_text
        print(f'Новые данные: {data[key]}')

    elif choise == 3:
        print("код 3")
        new_key = input("Введите новое название: ")
        data[new_key] = data.pop(key)

        data[new_key][0] = time_
        print(f'Текущие данные: {data[new_key]}')
        new_text = input("Введите новый текст.  Если передумали - оставьте поле пустым.\n: ")
        if new_text == "":
            new_text = data[new_key][1]
        else:
            data[new_key][1] = new_text
        print(f'Новые данные: {data[new_key]}')


    elif choise == 0:
        print("код 0")
        print("Выход из редактирования...")
        pass

    else:
        print("Неверный ввод, повторите попытку")
        edit_json()

    save_json(data)
    # return data


def navigation():
    indent = '\n' * 10  # Отстум для читаемости
    print(indent)

    time.sleep(0.5)

    try:
        code = int(input("Выберете пункт:\n"
                         "1 - Показать все заметки\n"
                         "2 - Создать новую\n"
                         "3 - Редактировать\n"
                         "4 - Удалить\n"
                         "0 - Exit\n"))
        if code not in range(5):
            raise ValueError

    except ValueError:
        print("Введите число 0-4! ")
        navigation()
    else:
        print(f"Выбран код {code}")

    match code:
        case 1:
            data = load_json()
            print(json.dumps(data, ensure_ascii=False, indent=4))
            print(input("Enter - продолжить"))
            navigation()

        case 2:
            new_json()
            navigation()

        case 3:
            edit_json()
            navigation()

        case 4:
            del_json()
            navigation()

        case 0:
            print('Exit')
            time.sleep(3)
            pass


navigation()
