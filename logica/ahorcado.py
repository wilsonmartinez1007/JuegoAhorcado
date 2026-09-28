import random

PALABRAS = [
    # Programación
    "python", "computadora", "programacion", "algoritmo", "variable",
    "funcion", "compilador", "servidor", "teclado", "pantalla",
    "internet", "software", "hardware", "memoria", "procesador",
    "archivo", "carpeta", "codigo", "sistema", "red",
    "base", "datos", "interfaz", "navegador", "ciclo",
    "condicion", "lista", "diccionario", "cadena", "objeto",
    # Universidad
    "universidad", "estudiante", "profesor", "semestre", "examen",
    "tarea", "biblioteca", "cuaderno", "proyecto", "matricula",
    "ingenieria", "calculo", "fisica", "laboratorio", "tesis",
    # Innovación
    "innovacion", "empresa", "emprendimiento", "estrategia", "mercado",
]
MAX_INTENTOS = 6


def nueva_partida():
    return {
        "palabra": random.choice(PALABRAS),
        "letras_adivinadas": [],
        "intentos": MAX_INTENTOS,
        "mensaje": "Elige una letra para comenzar.",
        "tipo": "info",
        "terminado": False,
    }


def palabra_mostrada(estado):
    return [l if l in estado["letras_adivinadas"] or estado["terminado"] else "_"
            for l in estado["palabra"]]


def gano(estado):
    return all(l in estado["letras_adivinadas"] for l in estado["palabra"])


def jugar_letra(estado, letra):
    letra = letra.lower()

    if estado["terminado"]:
        return estado

    # Validaciones
    if len(letra) != 1 or not letra.isalpha():
        estado["mensaje"], estado["tipo"] = "Por favor, ingresa solamente una letra.", "info"
        return estado

    if letra in estado["letras_adivinadas"]:
        estado["mensaje"], estado["tipo"] = "Ya habías utilizado esa letra.", "info"
        return estado

    estado["letras_adivinadas"].append(letra)

    # Comprobar letra
    if letra in estado["palabra"]:
        estado["mensaje"], estado["tipo"] = "¡Correcto! La letra está en la palabra.", "ok"
    else:
        estado["intentos"] -= 1
        estado["mensaje"], estado["tipo"] = "Incorrecto. Esa letra no está en la palabra.", "bad"

    # Comprobar si ganó o perdió
    if gano(estado):
        estado["mensaje"], estado["tipo"] = "¡Felicidades! Adivinaste la palabra.", "ok"
        estado["terminado"] = True
    elif estado["intentos"] == 0:
        estado["mensaje"] = f"¡Perdiste! La palabra era: {estado['palabra']}"
        estado["tipo"] = "bad"
        estado["terminado"] = True

    return estado


# Modo consola (solo se ejecuta si corres este archivo directamente)
if __name__ == "__main__":
    print("================================")
    print("       JUEGO DEL AHORCADO")
    print("================================")

    estado = nueva_partida()
    while not estado["terminado"]:
        print("\nPalabra:", " ".join(palabra_mostrada(estado)))
        print("Intentos restantes:", estado["intentos"])
        estado = jugar_letra(estado, input("Ingresa una letra: "))
        print(estado["mensaje"])