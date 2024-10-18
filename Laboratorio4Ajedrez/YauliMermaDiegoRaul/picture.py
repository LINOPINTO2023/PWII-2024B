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
    """Devuelve el espejo vertical de la imagen"""
    vertical = []
    for fila in self.img:
      nuevaFila = fila[::-1]  # Invertimos la fila
      vertical.append(nuevaFila)  # Agregamos la fila invertida a la nueva imagen
    return Picture(vertical)

  def horizontalMirror(self):
    """Devuelve el espejo horizontal de la imagen"""
    horizontal = []
    for fila in reversed(self.img):  # Invertimos el orden de las filas
      nuevaFila = fila[::1]  # Clonamos la fila (sin invertir horizontalmente)
      horizontal.append(nuevaFila)  # Agregamos la fila clonada a la nueva imagen
    return Picture(horizontal)

  def negative(self):
    """Devuelve el negativo de la imagen"""
    nuevaImagen = []
    for fila in self.img:
      nuevaFila = []
      for caracter in fila:
        nuevoColor = self._invColor(caracter)  # Invertimos el color
        nuevaFila.append(nuevoColor)  # Agregamos el color invertido a la nueva fila
      nuevaImagen.append(nuevaFila)  # Agregamos la fila invertida a la nueva imagen
    return Picture(nuevaImagen)

  def join(self, p):
    """Pone la imagen al lado derecho usando el argumento p"""
    nuevaImagen = []
    for indice, fila in enumerate(self.img):
      nuevaFila = list(fila) + list(p.img[indice])  # Unimos las filas de ambas imágenes
      nuevaImagen.append(nuevaFila)  # Agregamos la fila unida a la nueva imagen
    return Picture(nuevaImagen)

  def up(self, p):
    """Devuelve la figura 'p' encima de la figura actual"""
    nuevaImagen = []
    for fila in p.img:  # Agregamos las filas de la imagen 'p' primero
      nuevaImagen.append(fila[::1])  # Clonamos la fila para evitar mutaciones
    for fila in self.img:  # Agregamos las filas de la imagen actual
      nuevaImagen.append(fila[::1])  # Clonamos la fila para evitar mutaciones
    return Picture(nuevaImagen)

  def under(self, p):
    """Devuelve una nueva imagen con 'p' sobrepuesta encima de la imagen actual"""
    nuevaImagen = [list(fila) for fila in self.img]  # Copiamos las filas de la imagen actual
    for i, fila in enumerate(p.img):
      for j, caracter in enumerate(fila):
        if nuevaImagen[i][j] == ' ':  # Solo sobreescribimos si hay espacio vacío
          nuevaImagen[i][j] = caracter  # Sobreescribimos con el carácter de 'p'
    return Picture(nuevaImagen)

  def horizontalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual al costado n veces"""
    nuevaImagen = []
    for fila in self.img:
      filaRepetida = fila * n  # Repetimos la fila 'n' veces
      nuevaImagen.append(filaRepetida)  # Agregamos la fila repetida a la nueva imagen
    return Picture(nuevaImagen)

  def verticalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual hacia abajo n veces"""
    nuevaImagen = []
    for _ in range(n):
      for fila in self.img:
        nuevaImagen.append(fila[::1])  # Clonamos cada fila de la imagen original
    return Picture(nuevaImagen)
