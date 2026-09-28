import random

palabras = ["python", "computadora", "programacion", "universidad", "algoritmo"]

palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 6

print("================================")
print("       JUEGO DEL AHORCADO")
print("================================")

while intentos > 0:

    # Mostrar la palabra
    palabra_mostrada = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print("\nPalabra:", palabra_mostrada)
    print("Intentos restantes:", intentos)

    # Comprobar si ganó
    if all(letra in letras_adivinadas for letra in palabra):
        print("\n¡Felicidades! Adivinaste la palabra.")
        break

    letra = input("Ingresa una letra: ").lower()

    # Validaciones
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solamente una letra.")
        continue

    if letra in letras_adivinadas:
        print("Ya habías utilizado esa letra.")
        continue

    letras_adivinadas.append(letra)

    # Comprobar letra
    if letra in palabra:
        print("¡Correcto! La letra está en la palabra.")
    else:
        intentos -= 1
        print("Incorrecto. Esa letra no está en la palabra.")

else:
    print("\n¡Perdiste!")
    print("La palabra era:", palabra)