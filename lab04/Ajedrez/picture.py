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
        combined = []
        max_rows = max(len(self.img), len(p.img))  # Asegurarnos de recorrer todas las filas
        for i in range(max_rows):
            if i < len(self.img):
                row_self = self.img[i]  # Fila del tablero
            else:
                row_self = [" "] * len(self.img[0])  # Si p es más grande, rellenar con espacios

            if i < len(p.img):
                row_p = p.img[i]  # Fila de las piezas
            else:
                row_p = [" "] * len(p.img[0])  # Si self es más grande, rellenar con espacios

            combined_row = []
            for pixel_self, pixel_p in zip(row_self, row_p):
                if pixel_p != " ":
                    combined_row.append(pixel_p)
                else:
                    combined_row.append(pixel_self)
            combined.append("".join(combined_row))

        return Picture(combined)

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
