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
    for value in reversed(self.img):
      horizontal.append(value[::1])
    return Picture(horizontal)


  def negative(self):
    """ Devuelve el negativo de la imagen """
    nuevaImagen = []
    for value in self.img:
      row = []
      for caracter in value:
        row.append(self._invColor(caracter))
      nuevaImagen.append(row)    
    return Picture(nuevaImagen)


  def join(self, p):
    """ pone la imagen al lado derecho usando el argumento p """
    nuevaImagen = []

    for index, value in enumerate(self.img):
      nuevaImagen.append(list(value) + list(p.img[index]))

    return Picture(nuevaImagen)
  
  def up(self, p):
    """Devuelve a la figura encima de la actual """
    nuevaImagen = []
    #copiar todo p a nueva imange
    for value in p.img:
      nuevaImagen.append(value[::1])
    
    for value in self.img:
      nuevaImagen.append(value[::1])
    return Picture(nuevaImagen)


  def under(self, p):
    """ Devuelve una nueva y lla pone ensima de la actual"""
    nuevaImagen = []
    for value in self.img:
        nuevaImagen.append(list(value))

    for i, value in enumerate(p.img):
      for j, caracter in enumerate(value):
        if(nuevaImagen[i][j] == ' '):
          nuevaImagen[i][j] = caracter
        

    return Picture(nuevaImagen)
    
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    aux = self
    for _ in range(n-1):
      aux = aux.join(self) 
    return aux


  def verticalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad
de veces que indique el valor de n"""
    aux = self
    for _ in range(n-1):
      aux = aux.up(self) 
    return aux
