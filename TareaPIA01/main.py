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
    print("¡Bienvenido a piedra, papel o tijera!")


# Punto de entrada del programa
if __name__ == "__main__":
    main()