'''1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
 в формат Unicode и также проверить тип и содержимое переменных.
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
 а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя
  методы encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
 в байтовое и выполнить обратное преобразование (используя методы encode и decode).
5. Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com и преобразовывает результат
из байтовового типа данных в строковый без ошибок для любой кодировки операционной системы.
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
 «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
  что перед нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того,
   в какой кодировке он был создан.'''


'''1 задание'''

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(type(word_1) == str)
print(type(word_2) == str)
print(type(word_3) == str)

converted_word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
converted_word_2 = '\u0441\u043e\u043a\u0435\u0442'
converted_word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(converted_word_1) == str)
print(type(converted_word_2) == str)
print(type(converted_word_3) == str)

'''2 задание'''

word_1 = 'class'
word_2 = 'function'
word_3 = 'method'

print(type(eval(f'b"{word_1}"')))
print(len(eval(f'b"{word_1}"')))

print(type(eval(f'b"{word_2}"')))
print(len(eval(f'b"{word_2}"')))

print(type(eval(f'b"{word_3}"')))
print(len(eval(f'b"{word_3}"')))


'''3 задание'''

def byte_type(word: str):
    try:
        return type(eval(f'b"{word}"')) == 'bites'
    except Exception as e:
        return e

print(byte_type('type'))
print(byte_type('attribute'))
print(byte_type('класс'))
print(byte_type('функция'))

'''4 задание'''

w_1 = 'разработка'
encode_w_1 = w_1.encode('utf-8')
decode_w_1 = encode_w_1.decode('utf-8')
w_2 = 'администрирование'
encode_w_2 = w_2.encode('utf-8')
decode_w_2 = encode_w_2.decode('utf-8')
w_3 = 'protocol'
encode_w_3 = w_3.encode('utf-8')
decode_w_3 = encode_w_3.decode('utf-8')
w_4 = 'standard'
encode_w_4 = w_4.encode('utf-8')
decode_w_4 = encode_w_4.decode('utf-8')

print(encode_w_1)
print(decode_w_1)
print(encode_w_2)
print(decode_w_2)
print(encode_w_3)
print(decode_w_3)
print(encode_w_4)
print(decode_w_4)

'''5 задание'''

import chardet
import subprocess
import platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

args_2 = ['ping', param, '2', 'youtube.com']
process = subprocess.Popen(args_2, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


'''6 задание'''

with open('../lesson_2/test.txt', 'w', encoding='utf-8') as f:
    f.write('сетевое программирование \n')
    f.write('сокет \n')
    f.write('декоратор')

import chardet
encoding = chardet.detect(open('../lesson_2/test.txt', 'rb').read())['encoding']

with open('../lesson_2/test.txt', 'r', encoding=encoding) as f:
    print(f.read())