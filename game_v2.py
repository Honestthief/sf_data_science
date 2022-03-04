"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np 

def random_predict(number:int=1) -> int: 
    """ Randomly guess a number
    
    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attampts 
    """
    count = 0 
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # Estimated number
        if number == predict_number:
            break # exit from the loop if quessed right
    return(count)

def score_game(random_predict) -> int:
    """How many quesses on average

    Args:
        random_predict (_type_): quess function

    Returns:
        int: average number of attampts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for namber in random_array:
        count_ls.append(random_predict(namber))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает ваше число в среднем за: {score} попыток')
    return(score)

if __name__ == "_main_":
    #Run
    score_game(random_predict)