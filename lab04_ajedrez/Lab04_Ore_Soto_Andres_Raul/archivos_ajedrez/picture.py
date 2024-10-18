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
        return vertical

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = []
        for numero in range(len(self.img)):
            horizontal.append(self.img[len(self.img) -1 - numero])
        return horizontal

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
        return vertical
    
    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        combined = []
        
        max_rows = max(len(self.img), len(p.img))
        
        self_img_extended = self.img + [' ' * len(self.img[0])] * (max_rows - len(self.img))
        p_img_extended = p.img + [' ' * len(p.img[0])] * (max_rows - len(p.img))

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
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return Picture(None)

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
