
import random

palabras = ["PYTHON", "UNSA", "SISTEMAS", "CONFIGURACION", "VIERNES", "ADIVINAR"]
cant_intentos = 5

def ocultar_letras(palabra, porcentaje_oculto=0.6):
    posiciones_a_ocultar = random.sample(range(len(palabra)), int(len(palabra) * porcentaje_oculto))
    return "".join("_" if i in posiciones_a_ocultar else letra for i, letra in enumerate(palabra))

#funcion del juego 
def jugar():
    palabra = random.choice(palabras)
    palabra_oculta = ocultar_letras(palabra)
    intentos_restantes = cant_intentos

    print("##########################")
    print("--¡ADIVINA LA PALABRA!--")
    print(f"QUE PALABRA ES: {palabra_oculta}")
    
    while intentos_restantes > 0:
        intento = input("PON UNA LETRA O LA PALABRA COMPLETA: ")
        #una letra adivinada
        if len(intento) == 1 and intento in palabra:
            palabra_oculta = "".join(intento if palabra[i] == intento else palabra_oculta[i] for i in range(len(palabra)))
            print(f"ADVINASTE UNA LETRA, AHORA LA PALABRA ES: {palabra_oculta}")
        #toda la plabra
        elif intento == palabra:
            print(f"EXCELENTE!! ADIVINASTE TODA LA PLABRA: {palabra}")
            return
        #no esta la letra
        else:
            intentos_restantes -= 1
            print(f"LETRA INCORRECTA. TE QUEDAN [{intentos_restantes}] INTENTOS.")
        
        if "_" not in palabra_oculta:
            print(f"COMPLETASTE DE ADIVINAR LA PALABRA: {palabra_oculta}")
            return

    print(f"CHALES SE TE ACABARON LOS INTENTOS, LA PALABRA ERA => {palabra}")
    
#ejecucion del juego XD
jugar()
