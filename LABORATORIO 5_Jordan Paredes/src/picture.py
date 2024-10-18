"""Author: JP-777"""

from colors import *
class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, char):
        inverter = {'_': '=', '=': '_', '.': '@', '@': '.'}
        return inverter.get(char, char)

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        return Picture(self.img[::-1])

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative_img = []
        for row in self.img:
            new_row = ''.join([self._invColor(char) for char in row])
            negative_img.append(new_row)
        return Picture(negative_img)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        joined_img = []
        for i in range(len(self.img)):
            joined_img.append(self.img[i] + p.img[i])
        return Picture(joined_img)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p encima de la figura actual """
        return Picture(p.img + self.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p debajo de la figura actual """
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repeated_img = []
        for row in self.img:
            repeated_img.append(row * n)
        return Picture(repeated_img)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        return Picture(self.img * n)

    #Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados en sentido horario"""
        rotated_img = list(zip(*self.img[::-1]))
        rotated_img = [''.join(row) for row in rotated_img]
        return Picture(rotated_img)
    
    #Soy muy vicioso
    def superponer(self, p):
        """ Devuelve una nueva figura con la imagen actual sobrepuesta en la imagen p.
            Los espacios (' ') en la imagen actual no reemplazan el contenido en p."""
        if len(self.img) != len(p.img):
          raise ValueError("Las imágenes deben tener el mismo número de filas para superponerse")

        superpuesta = []
        for fila_self, fila_p in zip(self.img, p.img):
            nueva_fila = ""
            for char_self, char_p in zip(fila_self, fila_p):
                if char_self == ' ':
                    nueva_fila += char_p
                else:
                    nueva_fila += char_self
            superpuesta.append(nueva_fila)

        return Picture(superpuesta)
