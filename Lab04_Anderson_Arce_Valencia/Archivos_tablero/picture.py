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
    img = [row[::-1] for row in self.img]  
    return Picture(img)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
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
     
    return Picture(p.img + self.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    repeated_img = []
    for row in self.img:
            repeated_img.append(row * n)
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    return Picture(self.img * n)


  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated_img = list(zip(*self.img[::-1]))
    rotated_img = [''.join(row) for row in rotated_img]
    return Picture(rotated_img)

