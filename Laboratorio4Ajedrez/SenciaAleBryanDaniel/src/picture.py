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
    img = [self.img[i] for i in range(len(self.img) - 1, -1, -1)]
    return Picture(img)

  def horizontalMirror(self):
    img = [row[::-1] for row in self.img]
    return Picture(img)

  def negative(self):
    img = []
    for row in self.img:
        new_row = ''
        for char in row:
            new_row += self._invColor(char)
        img.append(new_row)
    return Picture(img)

  def join(self, other):
    img = []
    for i in range(len(self.img)):
      img.append(self.img[i] + other.img[i])
    return Picture(img)

  def up(self, other):
    img = []
    for rowS in self.img:
      img.append(rowS)
    for rowO in other.img:
      img.append(rowO)
    return Picture(img)
  
  def under(self, other):
    img = []
    for row_self, row_other in zip(self.img, other.img):
      new_row = ''.join(char_self if char_self != ' ' else char_other for char_self, char_other in zip(row_self, row_other))
      img.append(new_row)
    return Picture(img)
  
  def horizontalRepeat(self, n):
    img = [self.img[i] * n for i in range(len(self.img))]
    return Picture(img)

  def verticalRepeat(self, n):
    return Picture(self.img * n)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

