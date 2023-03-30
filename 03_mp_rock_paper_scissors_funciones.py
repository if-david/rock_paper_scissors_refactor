# Librerias
import os
import random

#Funcion para limpiar pantalla
def clean_screen():
    os.system("cls")
    
#Funcion para pausar la pantalla
def pause_screen():
    os.system("pause") 

#Funcion para obtener la eleccion del jugador
def player_choice():
    player_chooses = input("¿Qué eliges? ").lower()
    while not player_chooses in ('piedra', 'papel', 'tijeras'):
        print("POR FAVOR ELIGE UNA OPCIÓN VÁLIDA! \n")
        player_chooses = input("¿Qué eliges? ").lower()
    return player_chooses

#Funcion para obtener la eleccion de la computadora
def computer_choice():
    computer_chooses = random.choice(('piedra', 'papel', 'tijeras'))
    return computer_chooses

def start_game():
    #Contadores con valores de inicio
    user_victories = 0
    computer_victories = 0
    number_of_rounds = 0
    print("Bienvenid@ al juego ""Piedra, Papel o Tijeras""")
    print("El primero que obtenga 3 victorias será el ganador!")
    pause_screen()

    # ciclo de juego
    while (user_victories < 3) and (computer_victories < 3):
        number_of_rounds = number_of_rounds + 1 #Contador de rondas
        clean_screen() # Limpiar pantalla antes de cada ronda
        print(f"\nLa computadora tiene {computer_victories} victorias")
        print(f"Tienes {user_victories} victorias \n")
        print('*'*10)
        print("Round", number_of_rounds)
        print('*'*10)

        player_plays = player_choice() #El jugador elije
        computer_plays = computer_choice() #La computadora elige
        print(f"La computadora elige: {computer_plays}")
        
        # Compara para saber quien gana, pierde o empata
        if computer_plays == player_plays:
            print("-----> EMPATE! Juguemos de nuevo! \n")
            pause_screen()
        elif (player_plays == "piedra" and computer_plays == "tijeras") or (player_plays == "papel" and computer_plays == "piedra") or (player_plays == "tijeras" and computer_plays == "papel"):
            user_victories = user_victories + 1
            print("-----> GANASTE! \n")
            pause_screen()
        elif (player_plays == "piedra" and computer_plays == "papel") or (player_plays == "papel" and computer_plays == "tijeras") or (player_plays == "tijeras" and computer_plays == "piedra"):
            computer_victories = computer_victories + 1
            print("-----> PERDISTE! \n")
            pause_screen()

    # Detiene el juego cuando alguien gana tres veces
        if computer_victories == 3:
            clean_screen() #limpia la pantalla
            print(f"La computadora obtuvo {computer_victories} victorias \nHAS PERDIDO! jajajaja")
            break
        elif user_victories == 3:
            clean_screen() #limpia la pantalla
            print(f"FELICIDADES!!! Obtuviste {user_victories} victorias \n¡Eres mas listo de lo que pareces!")
            break

start_game()