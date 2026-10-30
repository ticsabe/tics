import random
numerosecreto = random.randint(0, 100)
intentos = 0
while True:
    intentos += 1
    numero = int(input("Adivina el número secreto (entre 1 y 100): "))
    if numero == numerosecreto:
        print("¡Felicidades! Has adivinado el número secreto en", intentos, "intentos.")
        break
    elif numero < numerosecreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")

        