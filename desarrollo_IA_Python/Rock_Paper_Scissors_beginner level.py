import random

opciones = ["piedra", "papel", "tijera"]

while True:
    eleccion_usuario = input("Elige piedra, papel o tijera: ")

    while eleccion_usuario not in opciones:
        print("Opción inválida. Elige piedra, papel o tijera.")
        eleccion_usuario = input("Elige piedra, papel o tijera: ")

    eleccion_computadora = random.choice(opciones)

    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La computadora eligió: {eleccion_computadora}")

    if eleccion_usuario == eleccion_computadora:
        print("¡Empate!")
    elif (
        (eleccion_usuario == "piedra" and eleccion_computadora == "tijera")
        or (eleccion_usuario == "papel" and eleccion_computadora == "piedra")
        or (eleccion_usuario == "tijera" and eleccion_computadora == "papel")
    ):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

    jugar_de_nuevo = input("¿Quieres jugar otra vez? (sí/no): ")
    if jugar_de_nuevo != "sí":
        break
