import random
import os
import re

def check_play_status():
  valid_responses = ['yes', 'no']
  while True:
    try:
      response = input('do you to play again? (Yes or No): ')
      if response.lower() not in valid_responses:
        raise ValueError('Yes or No onlly' )
      
      if response.lower()=='yes':
        return True
      else:
        os.system('cls' if os.name == 'nt' else 'clear' )
        print('Thanks for playing! ')
        exit()
    except ValueError as err:
      print(err)

def play_rps():
  play = True
  while play:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')
    print('rock, paper, scissors - shoot!')

    user_choice = input('chose your weapon'' [R]ock, [P]aper, or [S]cissors: ')

    if not re.match("[SsRrPp]", user_choice):
      print('please chose a latter: ')
      print('[R]ock, [P]eper, or [S]cissors')
      continue
      
    print(f'you chose: {user_choice}')

    choices = ['R','P','S']
    opp_choice = random.choice(choices)

    print(f'i chose: {opp_choice}')

    if opp_choice == user_choice.upper():
        print('Tie')
        play = check_play_status()
    elif opp_choice == 'R' and user_choice.upper()=="S":
        print('Rock beats scissors, i win!')
        play = check_play_status()
    elif opp_choice == 'S' and user_choice.upper()=="P":
        print('Scissors beats Paper, i win!')
        play = check_play_status()
    elif opp_choice == 'P' and user_choice.upper()=="R":
        print('Paper beats Rock, i win!')
        play = check_play_status()
    else:
        print('You win!\n')
        play = check_play_status()

if __name__ == '__main__':
  play_rps()

        
