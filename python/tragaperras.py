
# import random
# emojis = ["🍒", "🍋", "🍊", "🍉", "🍇", "⭐", "💎"]
# puntos1 = 0

# for ronda in range(3):
#     print(f"Ronda {ronda + 1}:")
#     tirada = [random.choice(emojis) for _ in range(3)]
#     print(" | ".join(tirada))
    
#     if tirada[0] == tirada[1] == tirada[2]:
#         puntos1 += 10
#         print("¡Tres iguales! Has ganado 10 puntos.")
#     elif tirada[0] == tirada[1] or tirada[1] == tirada[2] or tirada[0] == tirada[2]:
#         puntos1 += 5
#         print("¡Dos iguales! Has ganado 5 puntos.")
#     else:
#         print("No hay coincidencias. No has ganado puntos.")

# print(f"Total de puntos: {puntos1}")



resp = input("¿Cómo te llamas? ")
respuesta = input("¿Quieres jugar a la tragaperras? (sí/no) ") 
if respuesta == "sí":
    print("¡Genial! Vamos a jugar, ", resp)
    
for jugadores in range(1, 2):
    print("Jugador", jugadores)




import random 

puntos = 0


for xxx in range (1,3):

    secreto = random.randint(1, 10)
    if secreto == 1:
        print("🦄")
        puntos = puntos +1
    if secreto == 2:
        print("🐱")
        puntos = puntos +2
    if secreto == 3:
        print("🐶")
        puntos = puntos +3
    if secreto == 4:
        print("🐼")
        puntos = puntos +4      
    if secreto == 5:
        print("🐸")
        puntos = puntos +5
    if secreto == 6:
        print("🐵")
        puntos = puntos +6
    if secreto == 7:
        print("🐯")
        puntos = puntos +7
    if secreto == 8:
        print("🐰")
        puntos = puntos +8
    if secreto == 9:
        print("🐷")
        puntos = puntos +9          
    if secreto == 10:
        print("🐮")
secreto = random.randint(1, 10)
if secreto == 1:
    print("🦄")
if secreto == 2:
    print("🐱")
if secreto == 3:
    print("🐶")
if secreto == 4:
    print("🐼")
if secreto == 5:
    print("🐸")
if secreto == 6:
    print("🐵")
if secreto == 7:
    print("🐯")
if secreto == 8:
    print("🐰")
if secreto == 9:
    print("🐷")
if secreto == 10:
    print("🐮")

print ("Total de puntos: ", puntos )


resp = input("¿Cómo te llamas? ")
respuesta = input("¿Quieres jugar a la tragaperras? (sí/no) ") 
if respuesta == "sí":
    print("¡Genial! Vamos a jugar, ", resp)

for jugadores in range(2, 3):
    print("Jugador", jugadores)
import random 

puntos = 0


for xxx in range (1,3):

    secreto = random.randint(1, 10)
    if secreto == 1:
        print("🦄")
        puntos = puntos +1
    if secreto == 2:
        print("🐱")
        puntos = puntos +2
    if secreto == 3:
        print("🐶")
        puntos = puntos +3
    if secreto == 4:
        print("🐼")
        puntos = puntos +4      
    if secreto == 5:
        print("🐸")
        puntos = puntos +5
    if secreto == 6:
        print("🐵")
        puntos = puntos +6
    if secreto == 7:
        print("🐯")
        puntos = puntos +7
    if secreto == 8:
        print("🐰")
        puntos = puntos +8
    if secreto == 9:
        print("🐷")
        puntos = puntos +9          
    if secreto == 10:
        print("🐮")
secreto = random.randint(1, 10)
if secreto == 1:
    print("🦄")
if secreto == 2:
    print("🐱")
if secreto == 3:
    print("🐶")
if secreto == 4:
    print("🐼")
if secreto == 5:
    print("🐸")
if secreto == 6:
    print("🐵")
if secreto == 7:
    print("🐯")
if secreto == 8:
    print("🐰")
if secreto == 9:
    print("🐷")
if secreto == 10:
    print("🐮")

print ("Total de puntos: ", puntos )



if jugadores in range (1,2) > jugadores in range (2,3):
    print("El jugador 1 ha ganado.")
else:
    print("El jugador 2 ha ganado.")
