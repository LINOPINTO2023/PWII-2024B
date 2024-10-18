from .colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = self.img[::-1]
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = [''.join(reversed(line)) for line in self.img]
    return Picture(horizontal)

  def negative(self):
    negative_img = [''.join(self._invColor(char) for char in line) for line in self.img]
    return Picture(negative_img)

  def join(self, p):
    return Picture([line1 + line2 for line1, line2 in zip(self.img, p.img)])

  def up(self, p):
    return Picture(self.img + p.img)

  def under(self, p):
    return Picture(p.img + self.img )
  
  def horizontalRepeat(self, n):
    return Picture([line * n for line in self.img])

  def verticalRepeat(self, n):
    return Picture(self.img * n)

  def rotate(self):
    rotated_img = [''.join(row[col] for row in reversed(self.img)) for col in range(len(self.img[0]))]
    return Picture(rotated_img)