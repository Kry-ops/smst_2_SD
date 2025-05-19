import random
import os
import re
import sys

def check_play_status():
  valid_responses = ['ya', 'tidak']
  while True:
    try:
      response = input('mau bermain lagi? (ya atau tidak): ')
      if response.lower() not in valid_responses:
        raise ValueError('hanya boleh menjawab ya atau tidak' )
      
      if response.lower()=='ya':
        return True
      else:
        os.system('cls' if os.name == 'nt' else 'clear' )
        print('Trimakasih telah bermain!')
        sys.exit() 
        
    except ValueError as err:
      print(err)

def play_rps():
  play = True
  while play:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    print('semut, gajah, manusia, harimau, burung - shoot!')

    user_choice = input('pilih senjatamu'' [S]emut, [G]ajah, [M]anusia, [H]arimau, atau [B]urung: ')

    if not re.match("[SsGgMmHhBb]", user_choice):
      print('mohon memilih: ')
      print('[S]emut, [G]ajah, [M]anusia, [H]arimau, atau [B]urung')
      continue
      
    print(f'kemu memilih: {user_choice}')

    choices = ['S','G','M','H','B']
    opp_choice = random.choice(choices)

    print(f'Aku memilih: {opp_choice}')

    if opp_choice == user_choice.upper():
        print('Seri')
        play = check_play_status()
    elif opp_choice == 'M' and user_choice.upper()=="S":
        print('Manusia mengalahkan Semut, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'M' and user_choice.upper()=="B":
        print('Manusia mengalahkan Burung, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'G' and user_choice.upper()=="M":
        print('Gajah mengalahkan Manusia, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'G' and user_choice.upper()=="H":
        print('Gajah mengalahkan Harimau, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'S' and user_choice.upper()=="G":
        print('Semut mengalahkan Gajah, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'S' and user_choice.upper()=="H":
        print('Semut mengalahkan Harimau, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'H' and user_choice.upper()=="M":
        print('Harimau mengalahkan Manusia, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'B' and user_choice.upper()=="G":
        print('Burung mengalahkan Gajah, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'B' and user_choice.upper()=="S":
        print('Burung mengalahkan Semut, aku menang!!!')
        play = check_play_status()
    elif opp_choice == 'B' and user_choice.upper()=="H":
        print('Burung mengalahkan Semut, aku menang!!!')
        play = check_play_status()
    else:
        print('Selamat kamu menang\n')
        play = check_play_status()

if __name__ == '__main__':
  play_rps()

        
