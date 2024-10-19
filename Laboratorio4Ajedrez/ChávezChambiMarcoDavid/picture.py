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
    length = len(self.img)
    for x  in range(length):
      horizontal.append(self.img[length-x-1])
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    imgNeg = []
    for row in self.img:
        negRow = []
        for pixel in row:
            negRow.append(self._invColor(pixel))
        imgNeg.append(negRow)
    return Picture(imgNeg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    newImg = []

    for index, value in enumerate(self.img):
      newImg.append(list(value) + list(p.img[index]))

    return Picture(newImg)
  
  def up(self, p):   
    ImgUp = p.img + self.img    
    return Picture(ImgUp)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    newImg = [list(fila) for fila in self.img]  
    for i, fila in enumerate(p.img):
      for j, caracter in enumerate(fila):
        if newImg[i][j] == ' ':  
          newImg[i][j] = caracter  
    return Picture(newImg)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeatImgH = []
    for x in self.img:
      repeatImgH.append(x)
    while(n > 0):
      count = 0
      for y in self.img:
        repeatImgH[count] += y
        count += 1
      n -= 1
    return Picture(repeatImgH)    

  def verticalRepeat(self, n):
    repeatImgV = []
    for x in self.img:
      repeatImgV.append(x)
    while(n > 0):
      repeatImgV += self.img
      n -= 1
    return Picture(repeatImgV)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

