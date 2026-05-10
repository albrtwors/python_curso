# try:  except: | trycatch
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while(True):
    try:
        number1 = int(input("Ingrese un numero: "))
        print(number1)
        break
    except:
        print('No ingresaste un valor integer')
        clear()