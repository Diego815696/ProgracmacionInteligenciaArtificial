import random

#Constantes para las jugadas
PIEDRA = "piedra"
PAPEL = "papel"
TIJERAS = "tijera"

# Función que determina quién gana
def decidir_ganador(accion_usuario, accion_ordenador):
    if accion_usuario == PIEDRA:

        if accion_ordenador == PIEDRA:
            return "Ambos eligieron piedra. ¡Empate!"

        elif accion_ordenador == PAPEL:
            return "Papel envuelve piedra. ¡Perdiste!"

        else:
            return "Piedra rompe tijera. ¡Ganaste!"

    elif accion_usuario == PAPEL:

        if accion_ordenador == PIEDRA:
            return "Papel envuelve piedra. ¡Ganaste!"

        elif accion_ordenador == PAPEL:
            return "Ambos eligieron papel. ¡Empate!"

        else:
            return "Tijera corta papel. ¡Perdiste!"

    else:  # El usuario eligió tijera

        if accion_ordenador == PIEDRA:
            return "Piedra rompe tijera. ¡Perdiste!"

        elif accion_ordenador == PAPEL:
            return "Tijera corta papel. ¡Ganaste!"

        else:
            return "Ambos eligieron tijera. ¡Empate!"

# Lógica del programa
def main():

    # Lista de posibles jugadas
    opciones = [PIEDRA, PAPEL, TIJERAS]

    # Bucle que permite jugar varias rondas
    while True:

        # Solicitamos la elección al usuario
        accion_usuario = input("Elige piedra, papel o tijera: ").lower().strip()

        # Comprobamos si la elección es válida
        if accion_usuario not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        # El ordenador elige una opción al azar
        accion_ordenador = random.choice(opciones)

        # Mostramos las elecciones
        print(f"\nElegiste {accion_usuario}. El ordenador eligió {accion_ordenador}.")

        # Determinamos el ganador
        resultado = decidir_ganador(accion_usuario, accion_ordenador)
        print(resultado)

        # Preguntamos si desea continuar
        continuar = input("\n¿Quieres jugar otra ronda? (s/n): ").lower().strip()

        if continuar != "s":
            print("¡Gracias por jugar!")
            break


# Punto de entrada del programa
if __name__ == "__main__":
    main()