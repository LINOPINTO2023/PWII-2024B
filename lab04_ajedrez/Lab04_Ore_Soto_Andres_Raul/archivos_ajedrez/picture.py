from .colors import *

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
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = []
        for numero in range(len(self.img)):
            horizontal.append(self.img[len(self.img) -1 - numero])
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        vertical = []
        for fila in self.img:
            horizontal = []
            for letra in fila:
                if letra == "#":
                    horizontal.append(".")
                else:
                    horizontal.append("#")
            vertical.append(horizontal)
        return Picture(vertical)
    
    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        combined = []
        
        max_rows = max(len(self.img), len(p.img))
        
        # Asegúrate de que cada fila es una cadena de caracteres
        self_img_extended = [row if isinstance(row, str) else ''.join(row) for row in self.img]
        p_img_extended = [row if isinstance(row, str) else ''.join(row) for row in p.img]

        # Extiende las filas para que ambas imágenes tengan el mismo número de filas
        self_img_extended += [' ' * len(self_img_extended[0])] * (max_rows - len(self_img_extended))
        p_img_extended += [' ' * len(p_img_extended[0])] * (max_rows - len(p_img_extended))

        for i in range(max_rows):
            row_self = self_img_extended[i]
            row_p = p_img_extended[i]
            combined.append(row_self + row_p)
        
        return Picture(combined)

    def up(self, p):
        """Devuelve una nueva figura poniendo la figura recibida como argumento,
        encima de la figura actual"""
        
        combined = []
        max_rows = len(self.img) + len(p.img)
        combined.extend(p.img) 
        combined.extend(self.img)
        return Picture(combined)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p encima de la
            figura actual, sustituyéndola en su posición. """
        figures = ["king", "bishop", "knight", "queen", "rock", "pawn", "square"]
        if p not in figures:
            print("Ingrese una figura válida")
            return self
        new_figure = []
        



    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        return Picture(None)

    # Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
