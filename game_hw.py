""""Guess The Number!
    A game where the computer independently picks and guesses a number"""

import numpy as np

def random_predict(number: int = 1) -> int:  
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict = np.random.randint(1,101) # устанавливаем предпологаемое число
    
    while number != predict: # запускаем цикл для определения загаданного числа
        
        count += 1
        
        if number > predict:
            predict += 5
            
        else:
            predict -= 4
            
    return count

def average_number(random_predict) -> int: 
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания 

    Returns:
        int: среднее количество попыток
    """
    # 
    count_ls = [] 
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел
    
    for number in random_array: # 
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # вычисляем среднее значение
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    
    return score

if __name__ == '__main__':
    average_number(random_predict) # запускаем
                