from interpreter import draw
from chessPictures import knight

# Caballo blanco (original)
caballo_blanco = knight

# Caballo negro (versión negativa usando la función `negative()`)
caballo_negro = knight.negative()

# Junta los caballos en la misma fila usando la función `join()`
fila = caballo_blanco.join(caballo_negro)

# Segunda fila, intercambiando blanco y negro usando `join()`
fila_invertida = caballo_negro.join(caballo_blanco)

# Une las dos filas verticalmente usando `up()`
resultado = fila.up(fila_invertida)

# Dibuja el resultado
draw(resultado)

