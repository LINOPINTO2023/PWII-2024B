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
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        return Picture(self.img[::-1])

    def negative(self):
        negated_img = [''.join(map(self._invColor, line)) for line in self.img]
        return Picture(negated_img)

    def join(self, p):
        joined_img = [line1 + line2 for line1, line2 in zip(self.img, p.img)]
        return Picture(joined_img)

    def up(self, p):
         return Picture(p.img + self.img)

    def under(self, p):
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
            repeated_img = []
        for row in self.img:
            repeated_img.append(row * n)
        return Picture(repeated_img)

    def verticalRepeat(self, n):
        repeated_img = [line * n for line in self.img]
        return Picture(self.img * n)

    def rotate(self):
        return Picture(None)
