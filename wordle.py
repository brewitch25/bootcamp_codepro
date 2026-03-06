
print("Bienvenido al juegom wordle!")

# ------ Aca se definen las variables ----- #
usuario = input("Introduzca una palabra:")
palabra_a_adivinar = "gatos"


# ------ En esta porcion de codigo va a verificar si en el primer intento ya se adivina la palabra --- #
if usuario == palabra_a_adivinar:
    print("Primer intento, ganaste el juego!")

# ---- Si no acierta la palabra a la primera, pasa a esta parte de codigo ---- #
# ----- En parte del codigo se ve las cantidades de vidas del usuario ------ #


def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    cantidad_letras_de_palabra_a_encontrar = 5

    #creamos una lista vacia para almacenar el resultado
    letras_verificadas = []

    for posicion in range(cantidad_letras_de_palabra_a_encontrar): #5

        # es ogual el indice 0 de palabra_a_encontrar a indice 0 de palabra_ingresada?
        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]


        # la letra del indice 0 de palabra_ingresada en la palabra_a_encontrar
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            # si se cumple guardamos en la lista de letras verificadas
            letras_verificadas.append('['+palabra_ingresada[posicion]+']')

        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append('('+palabra_ingresada[posicion]+')')

        else:
            letras_verificadas.append(palabra_ingresada[posicion])

        
    return letras_verificadas

resultado = obtener_fila_verificada(usuario, palabra_a_adivinar)
print(resultado)

# Conteo de turnos
turnos = 5

while turnos > 0 :
    print(f"Te quedan {turnos} intentos, siga jugando!")
    palabra = input("Intente con otra palabra")
    turnos = turnos - 1 
    print("Palabra")

print("Ya no quedan intentos")