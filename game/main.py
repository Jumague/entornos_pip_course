import random
import math

options = ('piedra', 'papel', 'tijera')


def selection(option):
  if option == 1:
    return 'piedra'
  elif option == 2:
    return 'papel'
  elif option == 3:
    return 'tijera'
  else:
    return None


def combat(user, computer):
  if user == computer:
    print('hay un empate', end='\n\n')
  elif user == 'piedra':
    if computer == 'papel':
      print('el papel gana a piedra')
      print('computer gana!..', end='\n\n')
      return 'computer'
    else:
      print('la piedra gana a tijera')
      print('user gana!..', end='\n\n')
      return 'user'
  elif user == 'papel':
    if computer == 'piedra':
      print('el papel gana a piedra')
      print('user gana!..', end='\n\n')
      return 'user'
    else:
      print('tijera gana a papel')
      print('computer gana!..', end='\n\n')
      return 'computer'
  else:
      if computer == 'papel':
        print('la tijera gana a papel')
        print('user gana!..', end='\n\n')
        return 'user'
      else:
        print('la piedra gana a tijeras')
        print('computer gana!..', end='\n\n')
        return 'computer'


def aleatorio(max, min):
  return math.floor(random.random() * (max - min + 1) + min)


def game():
  round = 0
  wins = 3
  computer_wins = 0
  user_wins = 0
  while True:
    round +=1
    print(f'RONDA: {round}', end='\n\n')
    user_option = input("Elige una opcion:\n Piedra \n Papel \n Tijera \n\n    ")
    print('')
    user_option = user_option.lower()
    # hacemos una validacion de la entrada
    if user_option not in options:
      print(f'La opcion que ingresaste no es valida,\n por favor ingresa una de las siguientes opciones => {options}', end='\n\n')
      print('=' * 50, end='\n\n')
      continue 
      
      user_option = user_option.lower()
      
    computer_option = random.choice(options)
  
    print('user selection => ', user_option,
          '\ncomputer selection => ', computer_option, '\n')
  
    win = combat(user_option, computer_option)

    if win == 'user':
      user_wins += 1
    elif win == 'computer':
      computer_wins += 1

    if user_wins == wins:
      print(f'El ganador es el usuario {user_wins} a {computer_wins} a la computadora\nen {round} rondas')
      break 
    elif computer_wins == wins:
      print(f'El ganador es la computadora {computer_wins} a {user_wins} a el usuario\nen {round} rondas')
      break
    print('=' * 50, end='\n\n')
if __name__ == '__main__':
  game()
