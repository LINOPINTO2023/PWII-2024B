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
    for fila in self.img:
        horizontal.insert(0, fila)  # Agrega cada fila al inicio de la nueva lista
    return Picture(horizontal)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = []
    for fila in self.img:
      nueva_fila = ""
      for color in fila:
          nueva_fila += self._invColor(color)
      negativo.append(nueva_fila)
    return Picture(negativo)
  
  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    nueva_img = []
    for fila1, fila2 in zip(self.img, p.img):
      nueva_img.append(fila1 + fila2)
    return Picture(nueva_img)

  def up(self, p):
    """ Devuelve una nueva figura con la pieza del argumento sobre la figura actual """
    nueva_img = []
    max_length = max(len(self.img), len(p.img))
    for i in range(max_length):
      fila_actual = self.img[i] if i < len(self.img) else ""  
      fila_nueva = p.img[i] if i < len(p.img) else ""  
      nueva_fila = ""  
      for j in range(max(len(fila_actual), len(fila_nueva))):
        if j < len(fila_nueva) and fila_nueva[j] != " ":
          nueva_fila += fila_nueva[j]
        else:
          nueva_fila += fila_actual[j] if j < len(fila_actual) else " "  
      nueva_img.append(nueva_fila)
    return Picture(nueva_img)
  
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(self.img + p.img)
  
  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n """
    return Picture(self.img * n)