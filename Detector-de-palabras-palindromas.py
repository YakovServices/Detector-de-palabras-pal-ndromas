import os

def limpiar_terminal():
    """
    Limpia la terminal dependiendo del sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo (se lee igual al derecho y al revés).
    Ignora espacios y la distinción entre mayúsculas y minúsculas.
    Devuelve True si es palíndromo y la palabra procesada.
    """
    palabra_procesada = ''.join(caracter.lower() for caracter in palabra if caracter.isalnum())
    return palabra_procesada == palabra_procesada[::-1], palabra_procesada

def colorear_texto(texto, color):
    """
    Devuelve el texto envuelto en códigos de escape ANSI para el color especificado y negritas.
    """
    colores = {
        "verde": "\033[1;92m",  # Negritas y verde
        "rojo": "\033[1;91m",    # Negritas y rojo
        "reset": "\033[0m"
    }
    return f"{colores[color]}{texto}{colores['reset']}"

def capitalizar_primera_letra(palabra):
    """
    Devuelve la palabra con la primera letra en mayúscula y el resto igual.
    """
    if not palabra:
        return ""
    return palabra[0].upper() + palabra[1:]

if __name__ == "__main__":
    print("Detector de palabras Palíndromas")
    try:
        while True:
            entrada_original = input("Ingresa una palabra (o 'salir' para terminar, o 'limpiar' para vaciar la terminal): ")
            if entrada_original.lower() == 'salir':
                print("¡Hasta luego!")
                break
            elif entrada_original.lower() == 'limpiar':
                limpiar_terminal()
                print("Detector de palabras Palíndromas")
                continue  # Vuelve al inicio del bucle para pedir otra entrada
            elif entrada_original:
                es_pal, _ = es_palindromo(entrada_original)
                palabra_formateada = capitalizar_primera_letra(entrada_original)
                if es_pal:
                    print(f"{colorear_texto(palabra_formateada, 'verde')}")
                else:
                    print(f"{colorear_texto(palabra_formateada, 'rojo')}")
            else:
                print("Por favor, ingresa una palabra.")
    except KeyboardInterrupt:
        print("\n¡Saliendo del detector de palíndromos!")
    finally:
        print("¡Hasta luego!")
