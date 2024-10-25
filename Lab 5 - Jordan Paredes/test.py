import random
class AdivinaPalabra:
    def __init__(self, palabras, intentos=5):
        self.palabras = palabras
        self.intentos = intentos
        self.palabra_secreta = random.choice(palabras)
        self.palabra_oculta = self.ocultar_letras(self.palabra_secreta)
        self.intentos_restantes = intentos

    def ocultar_letras(self, palabra):
        letras = list(palabra)
        num_letras_a_ocultar = int(len(letras) * 0.6)
        indices_a_ocultar = random.sample(range(len(letras)), num_letras_a_ocultar)

        for i in indices_a_ocultar:
            letras[i] = '_'

        return ''.join(letras)

    def actualizar_palabra(self, letra):
        nueva_palabra = ''.join(
            letra if self.palabra_secreta[i] == letra else self.palabra_oculta[i]
            for i in range(len(self.palabra_secreta))
        )
        self.palabra_oculta = nueva_palabra
        return nueva_palabra

    def adivinar(self, intento):
        if len(intento) == 1:  # Intentar adivinar una letra
            if intento in self.palabra_secreta:
                self.actualizar_palabra(intento)
                print("¡Correcto! La palabra es ahora:", self.palabra_oculta)
            else:
                self.intentos_restantes -= 1
                print("Letra incorrecta. Te quedan", self.intentos_restantes, "intentos.")
        elif len(intento) == len(self.palabra_secreta):  # Intentar adivinar la palabra completa
            if intento == self.palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra:", self.palabra_secreta)
                return True  # Indica que el juego ha terminado
            else:
                self.intentos_restantes -= 1
                print("Respuesta incorrecta. Te quedan", self.intentos_restantes, "intentos.")
        else:
            print("Entrada no válida. Introduce una letra o una palabra de", len(self.palabra_secreta), "letras.")

        return self.palabra_oculta == self.palabra_secreta  # Retorna True si la palabra está completa

    def jugar(self):
        print("¡Bienvenido al juego de adivinar palabras!\n")
        print("Adivina la palabra:", self.palabra_oculta)
        print("Tienes", self.intentos_restantes, "intentos.\n")

        while self.intentos_restantes > 0:
            intento = input("Introduce una letra o intenta resolver la palabra completa: ")
            if self.adivinar(intento):
                print("¡Ganaste!")
                break

            if self.intentos_restantes == 0:
                print("Lo siento, te has quedado sin intentos. La palabra era:", self.palabra_secreta)
                break


palabras = ["murcielago", "elefante", "computadora", "python", "programacion"]

juego = AdivinaPalabra(palabras)
juego.jugar()
