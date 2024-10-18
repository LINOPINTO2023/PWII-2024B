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
        img = [row[::-1] for row in self.img]  # Invertir las columnas
        return Picture(img)

    def horizontalMirror(self):
        img = self.img[::-1]  # Invertir las filas
        return Picture(img)

    def negative(self):
        img = [[self._invColor(pixel) for pixel in row] for row in self.img]  # Mantener formato de lista
        return Picture(img)

    def join(self, other):
        img = []
        for i in range(len(self.img)):
         img.append(''.join(self.img[i]) + ''.join(other.img[i]))
        return Picture(img)

    def up(self, other):
        img = other.img + self.img  # Concatenar las listas
        return Picture(img)

    def under(self, other):
        img = [[other.img[i][j] if self.img[i][j] == ' ' else self.img[i][j]
                for j in range(len(self.img[i]))] for i in range(len(self.img))]
        return Picture(img)

    def horizontalRepeat(self, n):
        repeated = self
        for _ in range(n - 1):
            repeated = repeated.join(self)
        return repeated

    def verticalRepeat(self, n):
        repeated = self
        for _ in range(n - 1):
            repeated = repeated.up(self)
        return repeated

    def rotate(self):
        rotated = list(zip(*self.img[::-1]))  # Rotar 90 grados
        return Picture([list(row) for row in rotated])
