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
		return Picture(self.img[::-1])

	def negative(self):
		""" Devuelve un negativo de la imagen """
		negated_img = [''.join(map(self._invColor, line)) for line in self.img] 
		return Picture(negated_img)

	def join(self, p):
		""" Devuelve una nueva figura poniendo la figura del argumento 
		al lado derecho de la figura actual """
		joined_img = [line1 + line2 for line1, line2 in zip(self.img, p.img)]
		return Picture(joined_img)

	def up(self, p):
		""" Devuelve una nueva figura colocando la figura p encima de la figura actual,
        reemplazando los caracteres de la figura actual con los de p. """
		combined_img = []

		for i in range(len(self.img)):
			# Obtiene la línea de la figura actual y de la figura p
			line_self = self.img[i]
			line_piece = p.img[i]

			# Inicializamos una lista vacía para los caracteres de la nueva línea
			new_line_chars = []

			for piece, self_char in zip(line_piece, line_self):
				if piece != ' ':
					new_line_chars.append(piece)
				else:
					new_line_chars.append(self_char)
			new_line = ''.join(new_line_chars)

			combined_img.append(new_line)

		return Picture(combined_img)  # Retornar la nueva figura
	
	def under(self, p):
		""" Devuelve una nueva figura poniendo la figura p sobre la figura actual """
		return Picture(self.img + p.img)  # Coloca la imagen p debajo

	def horizontalRepeat(self, n):
		""" Devuelve una nueva figura repitiendo la figura actual al costado
		la cantidad de veces que indique el valor de n """
		repeated_img = [line * n for line in self.img]  # Repite cada línea n veces
		return Picture(repeated_img)

	def verticalRepeat(self, n):
		""" Devuelve una nueva figura repitiendo la figura actual debajo 
        la cantidad de veces que indique el valor de n """
		return Picture(self.img * n)  

	#Extra: Sólo para realmente viciosos 
	def rotate(self):
		"""Devuelve una figura rotada en 90 grados, puede ser en sentido horario
		o antihorario"""
		return Picture(None)