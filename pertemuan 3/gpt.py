import random
import os
import re

def check_play_status():
  valid_responses = ['ya', 'tidak']
  while True:
    try:
      response = input('mau bermain lagi? (ya atau tidak): ')
      if response.lower() not in valid_responses:
        raise ValueError('hanya boleh menjawab ya atau tidak')
      
      if response.lower()=='ya':
        return True
      else:
        os.system('cls' if os.name == 'nt' else 'clear' )
        print('Trimakasih telah bermain!')
        exit()
    except ValueError as err:
      print(err)

def play_rps():
  play = True
  while play:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    print('semut, manusia, gajah, harimau, burung - shoot!')

    user_choice = input('pilih senjatamu'' [S]emut, [G]ajah, [M]anusia, [H]arimau, atau [B]urung: ')

    if not re.match("[SsGgMmHhBb]", user_choice):
      print('mohon memilih: ')
      print('[S]emut, [G]ajah, [M]anusia, [H]arimau, atau [B]urung')
      continue
      
    print(f'kamu memilih: {user_choice}')

    choices = ['S','G','M','H','B']
    opp_choice = random.choice(choices)

    print(f'Aku memilih: {opp_choice}')

    if opp_choice == user_choice:
        print('Seri')
        play = check_play_status()
    elif opp_choice == 'S' and user_choice=='G':
        print('semut mengalahkan gajah, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'G' and user_choice=='M':
        print('gajah mengalahkan manusia, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'M' and user_choice=='S':
        print('manusia mengalahkan semut, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'H' and user_choice=='M':
        print('harimau mengalahkan manusia, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'B' and user_choice=='H':
        print('burung mengalahkan harimau, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'B' and user_choice=='S':
        print('burung mengalahkan semut, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'H' and user_choice=='G':
        print('harimau mengalahkan gajah, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'G' and user_choice=='B':
        print('gajah mengalahkan burung, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'M' and user_choice=='B':
        print('manusia mengalahkan burung, aku menang!!!')
        play = check_play_status()
    else:
        print('Kamu menang\n')
        play = check_play_status()

if __name__ == '__main__':
  play_rps()
