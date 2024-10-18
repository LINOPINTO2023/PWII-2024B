def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(f"Los elementos que no son parte de la diagonal deben ser 0. Posición:[{i}][{j}]: {m[i][j]}")
                    return False
            elif m[i][j] != d:
                print(f"La diagonal no tiene los mismos valores en la posición:[{i}][{j}]: {m[i][j]}")
                return False
    return True
def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

