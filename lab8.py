import random # Подключение модуля для работы со случайной генерацией
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('sample.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('Запуск программы')

while True: # Цикл обработки ввода целого числа
    try:
        n = int(input('Введите целое число - количество генерируемых чисел: '))
        break
    except ValueError:
        print('Ошибка ввода. Попробуйте еще раз')

numbers = [i+1 for i in range(n)] # Генерация списка натуральных чисел заданного кол-ва
rand_nums = [] # Пустой список для сгенерированных чисел

print('Нажимайте Enter для генерации каждого нового числа ')

for j in range(n):
    input() # Требование пустого ввода
    new_num = random.choice(numbers) # Генерация случайного числа из ранее заданного списка
    rand_nums.append(new_num) # Добавление в список сгенерированного числа
    print(f'Сгенерированное число: {new_num}', end = '')
    numbers.remove(new_num) # Удаление из списка оставшихся возможных чисел

print(f'\nСписок сгенерированных чисел: {rand_nums}')

try:
    input('\nРабота программы завершена. Для выхода из консоли нажмите Enter ')
    logging.info('Программа сработала успешно')
except RuntimeError:
    logging.error('Ошибка')
