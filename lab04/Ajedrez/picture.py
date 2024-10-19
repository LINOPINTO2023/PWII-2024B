from colors import *
class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])#invertir fila
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]  # Invertir lista de las filas
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative = []
        for row in self.img:
            neg_row = [self._invColor(pixel) for pixel in row]
            negative.append(neg_row)
        return Picture(negative)

    def join(self, p):
      """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
      joined = []
      for row1, row2 in zip(self.img, p.img):
          joined.append("".join(row1) + "".join(row2))  # Convertimos las filas en cadenas antes de concatenarlas
      return Picture(joined)


    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p debajo de la figura actual """
        return Picture(self.img + p.img)  # Concatenamos las imágenes verticalmente

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
        return self.up(p)  # Igual a `up`, ya que son conceptos similares pero invertidos

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repeated = []
        for row in self.img:
            repeated.append(row * n)  # Repetimos cada fila n veces
        return Picture(repeated)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo n veces """
        return Picture(self.img * n)  # Repetimos la imagen entera n veces

    # Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados en sentido horario"""
        rotated = list(zip(*self.img[::-1]))  # Rotación de 90 grados
        rotated = [list(row) for row in rotated]  # Convertimos las tuplas a listas
        return Picture(rotated)
