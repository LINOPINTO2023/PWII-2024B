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
      vertical.append(value[::-1])

    return Picture(vertical)
  
  
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in reversed(self.img):
      horizontal.append(row[:])
    return Picture(horizontal)


  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative_img = []
    for row in self.img:
        neg_row = []
        for pixel in row:
            neg_row.append(self.invertColor(pixel))
        negative_img.append(neg_row)
    return Picture(negative_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    new_img = []
    for i, row in enumerate(self.img):
        new_img.append(row + p.img[i])
    return Picture(new_img)

  def up(self, p):
    img = []
    for value in p.img:
      img.append(value[::1])
    
    for value in self.img:
      img.append(value[::1])
    return Picture(img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    overlay_img = [row[:] for row in self.img]
    for i, row in enumerate(p.img):
        for j, pixel in enumerate(row):
            if overlay_img[i][j] == ' ':
                overlay_img[i][j] = pixel
    return Picture(overlay_img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated = self
    for _ in range(n - 1):
        repeated = repeated.join(self)
    return repeated

  def verticalRepeat(self, n):
    repeated = self
    for _ in range(n - 1):
        repeated = repeated.up(self)
    return repeated

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated = list(zip(*self.img[::-1]))
    return Picture([list(row) for row in rotated])