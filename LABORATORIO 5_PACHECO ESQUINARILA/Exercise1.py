import random

palabras = ["encapsulation", "polymorphism", "asynchronous", "inheritance", "abstraction", "multithreading", "serialization"]


def ocultar_palabra(palabra):
    num_letras_a_ocultar = int(len(palabra) * 0.6)
    letras_a_ocultar = random.sample(range(len(palabra)), num_letras_a_ocultar)
    palabra_oculta = ''.join('_' if i in letras_a_ocultar else letra for i, letra in enumerate(palabra))
    return palabra_oculta
