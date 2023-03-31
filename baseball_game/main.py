import random
import re


def baseball_play():
  print('''
  안녕하세요! 
  
  해당 게임은 숫자야구 게임입니다.
  
  룰은 간단하게 랜덤한 3자리의 숨겨진 숫자가 존재하며 (ex. 941)
  
  매 입력을 통해서 숨겨진 숫자를 찾아내면 되는 게임입니다.
  
  매 입력 결과 S(스트라이크), B(볼) 카운트를 표시해주는데, 
  
  S는 정답과 입력의 자리와 숫자가 모두 같은 개수,
  
  B는 정답과 입력의 자리는 다르고 숫자는 같은 개수입니다.
  
  각 숫자는 0~9 이며 서로 중복되지 않습니다.
  ''')
  check_list = random.sample(range(0, 10), 3)
  n = 0
  check = str(check_list[0]) + str(check_list[1]) + str(check_list[2])
  check = re.sub('[^0-9]', '', check)
  while True:
    n += 1
    S = 0
    B = 0

    input_value = input('입력값 : ')
    try:
      if input_value == check:
        print(f'clear : {n}번만에 정답을 맞추셨습니다!')
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
    except:
      print('입력값이 잘못되었습니다.')
      print('3자리 숫자로 입력해주세요.')


if __name__ == '__main__':
  baseball_play()
