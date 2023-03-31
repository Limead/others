import random

def baseball_play():
    check_list = random.sample(range(0,10),3)
    n = 0
    check = str(check_list[0])+str(check_list[1])+str(check_list[2])
    while True:
        n += 1
        S = 0
        B = 0

        input_value = input('value : ')
        
        if input_value == check:
            print(f'clear : {n}')
            break
        
        if (input_value[0] == check[0]):
            S += 1
        if (input_value[1] == check[1]):
            S += 1
        if (input_value[2] == check[2]):
            S += 1
        
        if (input_value[0] != check[0]) & (input_value[0] == check[1]):
            B += 1
        if (input_value[0] != check[0]) & (input_value[0] == check[2]):
            B += 1
        if (input_value[1] != check[1]) & (input_value[1] == check[0]):
            B += 1
        if (input_value[1] != check[1]) & (input_value[1] == check[2]):
            B += 1
        if (input_value[2] != check[2]) & (input_value[2] == check[0]):
            B += 1
        if (input_value[2] != check[2]) & (input_value[2] == check[1]):
            B += 1
            
        print(f'S : {S} / B : {B}')
        
if __name__ == '__main__':
    baseball_play()
