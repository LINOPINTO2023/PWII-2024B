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
    horizontal=[]
    cont=len(self.img)-1
    for i in range(len(self.img)):
      horizontal.append(self.img[cont])
      cont-=1
    return horizontal

  def negative(self):
    """ Devuelve un negativo de la imagen """
    c = self.img
    a = []
    for i in range(len(c)):
      text = ""
      texto = c[i]
      for j in range(len(texto)):
        if texto[j] != " ":
          text = text + self._invColor(texto[j])
        else:
          text = text + texto[j]
      a.append(text)
    return Picture(a)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    nuevo=[]
    cadena=""
    for i in range(len(self.img)):
      cadena=self.img[i]+p.img[i]
      nuevo.append(cadena)
    return Picture(nuevo)

  def up(self, p):
    auxiliar = p.img
    self.img = p.img + self.img
    return Picture(self.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    c = self.img
    b = p.img
    a = []
    for i in range(len(c)):
      text = ""
      texto = c[i]
      texto1 = b[i]
      for j in range(len(texto)):
        if(texto1[j]!=" "):
          text+=texto1[j]
        else:
          text+=texto[j]
      a.append(text)
    return Picture(a)
    
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    imagen = self.img
    nuevo = []
    tamaño = int(len(self.img))
    for x in range(tamaño):
      cadena = ""
      for i in range(n):
        cadena = cadena + str(imagen[x])
      nuevo.append(cadena)
    return Picture(nuevo)

  def verticalRepeat(self, n):
    imagen = self.img
    nuevo = []
    for x in range(n):
      nuevo = nuevo + imagen
    return Picture(nuevo)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
