'''1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
    данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
    соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
    os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
     поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
      «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
      (также для каждого файла);

    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
     данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
    Проверить работу программы через вызов функции write_to_csv().

2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
 Написать скрипт, автоматизирующий его заполнение данными. Для этого:

    Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
     цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
      в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
    Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата. Для этого:

    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму
    — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
    отсутствующим в кодировке ASCII (например, €);
    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
    файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом:
     allow_unicode = True;'''
import json
import datetime

import yaml

'''1 задание'''

import re
import chardet
import csv
import os

patterns = ['Название ОС', 'Код продукта', 'Изготовитель системы', 'Тип системы']


def get_data(patterns: list):
    file_names = os.listdir('documents/')
    main_data = [patterns]
    for file in file_names:
        encoding = chardet.detect(open(f'lesson_2/documents/{file}', 'rb').read())['encoding']
        with open(f'lesson_2/documents/{file}', 'r', encoding=encoding) as f:
            line = []
            for i in f.read().splitlines():
                for pattern in patterns:
                    if re.search(pattern, i):
                        line.append(i.replace(f'{pattern}:', '').strip())
            main_data.append(line)
    return main_data


def write_to_csv(data):
    with open('result.csv', 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)
    with open('result.csv', encoding='utf-8') as f_n:
        return f_n.read()


print(write_to_csv(get_data(patterns)))

'''2 задание'''


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(obj=dict_to_json, indent=4))

    with open('orders.json', encoding='utf-8') as f:
        f_content = f.read()
        return json.loads(f_content)


print(write_order_to_json('headphones', 5, 45, 'user', '20.05.2000'))

'''3 задание'''

data_to_yaml = {
    '1': [1, 2, 3],
    '2': 2,
    '3': {'123': '123€',
          '456': '456€'},
}

with open('data_yaml.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data_to_yaml, f, default_flow_style=None, allow_unicode=True)

with open('data_yaml.yaml', encoding='utf-8') as f:
    print(f.read())