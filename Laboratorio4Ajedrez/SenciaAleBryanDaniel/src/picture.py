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
    img = self.img[::-1]
    return Picture(img)

  def horizontalMirror(self):
    img = [row[::-1] for row in self.img]
    return Picture(img)

  def negative(self):
    img = [(''.join([self._invColor(char) for char in row])) for row in self.img]
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
    for i in range(len(self.img)):
      row = []
      for j in range(len(self.img[i])):
        charS = self.img[i][j]
        charO = other.img[i][j]
        if(charS == ' '):
          row.append(charO)
        else:
          row.append(charS)
      img.append(row)
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

