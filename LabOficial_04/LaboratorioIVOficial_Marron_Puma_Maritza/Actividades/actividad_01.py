import numpy as np
def esEscalar(m):
  d = m[0][0]
  for i in range(len(m)):
    for j in range(len(m)):
      if i != j:
        if m[i][j] != 0:
          print(m[i][j])
          print(f"Elemento fuera del alcance de la diagonal superior e inferior: {m[i][j]}")
          return False
      elif m[i][j] != d:
          
        print(m[i][j])
        print(f"Elemento en el alcance de la diagonal superior e inferior es diferente : {m[i][j]}")
        return False
  print("La matriz es escalar")
  return True
matriz_escalar1 = np.array([[3, 0, 0],
                           [0, 3, 0],
                           [0, 0, 3]])
matriz_noescalar2 = np.array([[3, 0, 0],
                           [0, 2, 0],
                           [0, 0, 3]])
print("Resultados sera matriz escalar:")
esEscalar(matriz_escalar1)
print("Resultados sera matriz escalar:")
esEscalar(matriz_noescalar2)
