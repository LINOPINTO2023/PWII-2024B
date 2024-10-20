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
		"""Devuelve el negativo de la imagen"""
		negativo = []
		for i in self.img:
			filaNegativo = []
			#Se analizará caracter por caracter y se usará invColor para cambiar los caracteres
			for j in i:
				nuevoColor = self._invColor(j)
				filaNegativo.append(nuevoColor)
			negativo.append(filaNegativo)
		return Picture(negativo)

	def join(self, p):
		""" Devuelve una nueva figura poniendo la figura del argumento 
		al lado derecho de la figura actual """
		imagenesJuntas = []
		for i, fila in enumerate(self.img):
			#Juntamos ambas filas de caracteres en uno solo
			combFilas = list(fila) + list(p.img[i])
			#Lo almacenamos en nuestra variable
			imagenesJuntas.append(combFilas)
		return Picture(imagenesJuntas)

	def up(self, p):
		"""Devuelve la figura 'p' encima de la figura actual"""
		figuraEncima = []
		#Arriba estará la figura p
		for i in p.img:
			figuraEncima.append(i[::1])
		#Luego se pondrá la otra imagen
		for i in self.img:
			figuraEncima.append(i[::1])
		return Picture(figuraEncima)

	def under(self, p):
		""" Devuelve una nueva figura poniendo la figura p sobre la
		figura actual """
		#Copiamos todo el contenido en nuestra nueva variable
		figuraSobrepuesta = [list(fil) for fil in self.img]
		#Vamos analizando cada caracter de cada fila con bucles
		for i, fil in enumerate(p.img):
			for j, col in enumerate(fil):
				#Se sobreescribirá si se presenta espacios/caracteres vacíos
				if figuraSobrepuesta[i][j] == ' ':
					figuraSobrepuesta[i][j] = col
		return Picture(figuraSobrepuesta)

	def horizontalRepeat(self, n):
		""" Devuelve una nueva figura repitiendo la figura actual al costado
		la cantidad de veces que indique el valor de n """
		figuraHorizontal = []
		for i in self.img:
			#Se irá almacenando n filas en una sola hasta terminar el bucle
			figuraHorizontal.append(i * n)
		return Picture(figuraHorizontal)

	def verticalRepeat(self, n):
		figuraVertical = []
		for i in range(n):
			for j in self.img:
				figuraVertical.append(j[::1])
		return Picture(figuraVertical)