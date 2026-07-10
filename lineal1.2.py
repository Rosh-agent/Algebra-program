from fractions import Fraction


def f(n):
    return str(n.numerator) if n.denominator == 1 else f"{n.numerator}/{n.denominator}"


def leer_fraccion(mensaje):
    while True:
        try:
            dato = input(mensaje).strip().replace(",", ".")
            return Fraction(dato)
        except:
            print("Error: ingrese un número válido. Ejemplo: 2, 0.5 o 1/2")


def imprimir_sistema(A, B):
    print("\n========== SISTEMA ORIGINAL ==========")
    for i in range(3):
        print(
            f"E{i+1}: {f(A[i][0])}x + {f(A[i][1])}y + {f(A[i][2])}z = {f(B[i])}")


def comprobacion(A, B, sol):
    print("\n========== COMPROBACIÓN ==========")
    if sol is None:
        print("No hay solución para comprobar.")
        return

    x, y, z = sol

    for i in range(3):
        resultado = A[i][0]*x + A[i][1]*y + A[i][2]*z
        print(
            f"E{i+1}: {f(A[i][0])}({f(x)}) + {f(A[i][1])}({f(y)}) + {f(A[i][2])}({f(z)}) = {f(resultado)}")
        print(f"{f(resultado)} = {f(B[i])}")


def resolver_2x2(a, b, e, c, d, f2):
    det = a*d - b*c
    if det == 0:
        return None

    y = (e*d - b*f2) / det
    z = (a*f2 - e*c) / det
    return y, z


def igualacion(A, B):
    print("\n========== MÉTODO DE IGUALACIÓN ==========")

    if A[0][0] == 0 or A[1][0] == 0 or A[2][0] == 0:
        print("No se puede despejar x porque algún coeficiente de x es cero.")
        return None

    print("\nPaso 1: Despejamos x en cada ecuación")

    despejes = []

    for i in range(3):
        a, b, c = A[i]
        d = B[i]
        print(f"E{i+1}: x = ({f(d)} - {f(b)}y - {f(c)}z) / {f(a)}")
        despejes.append((a, b, c, d))

    print("\nPaso 2: Igualamos E1 con E2")

    a1, b1, c1, d1 = despejes[0]
    a2, b2, c2, d2 = despejes[1]

    ny1 = a2*b1 - a1*b2
    nz1 = a2*c1 - a1*c2
    nb1 = a2*d1 - a1*d2

    print(f"({f(d1)} - {f(b1)}y - {f(c1)}z)/{f(a1)} = ({f(d2)} - {f(b2)}y - {f(c2)}z)/{f(a2)}")
    print(f"Resultado: {f(ny1)}y + {f(nz1)}z = {f(nb1)}")

    print("\nPaso 3: Igualamos E1 con E3")

    a3, b3, c3, d3 = despejes[2]

    ny2 = a3*b1 - a1*b3
    nz2 = a3*c1 - a1*c3
    nb2 = a3*d1 - a1*d3

    print(f"({f(d1)} - {f(b1)}y - {f(c1)}z)/{f(a1)} = ({f(d3)} - {f(b3)}y - {f(c3)}z)/{f(a3)}")
    print(f"Resultado: {f(ny2)}y + {f(nz2)}z = {f(nb2)}")

    print("\nPaso 4: Resolvemos el sistema 2x2")

    sol2 = resolver_2x2(ny1, nz1, nb1, ny2, nz2, nb2)

    if sol2 is None:
        print("No tiene solución única.")
        return None

    y, z = sol2
    x = (B[0] - A[0][1]*y - A[0][2]*z) / A[0][0]

    print(f"y = {f(y)}")
    print(f"z = {f(z)}")
    print(f"x = {f(x)}")

    return x, y, z


def sustitucion(A, B):
    print("\n========== MÉTODO DE SUSTITUCIÓN ==========")

    if A[0][0] == 0:
        print("No se puede despejar x desde E1 porque el coeficiente es cero.")
        return None

    a, b, c = A[0]
    d = B[0]

    print("\nPaso 1: Despejamos x de E1")
    print(f"E1: {f(a)}x + {f(b)}y + {f(c)}z = {f(d)}")
    print(f"x = ({f(d)} - {f(b)}y - {f(c)}z) / {f(a)}")

    nuevas = []

    print("\nPaso 2: Sustituimos x en E2 y E3")

    for i in [1, 2]:
        ai, bi, ci = A[i]
        di = B[i]

        print(f"\nEn E{i+1}: {f(ai)}x + {f(bi)}y + {f(ci)}z = {f(di)}")
        print(
            f"{f(ai)}[({f(d)} - {f(b)}y - {f(c)}z)/{f(a)}] + {f(bi)}y + {f(ci)}z = {f(di)}")

        ny = bi - ai*b/a
        nz = ci - ai*c/a
        nb = di - ai*d/a

        print(f"Resultado: {f(ny)}y + {f(nz)}z = {f(nb)}")
        nuevas.append((ny, nz, nb))

    print("\nPaso 3: Resolvemos el sistema 2x2")

    sol2 = resolver_2x2(nuevas[0][0], nuevas[0][1], nuevas[0][2],
                        nuevas[1][0], nuevas[1][1], nuevas[1][2])

    if sol2 is None:
        print("No tiene solución única.")
        return None

    y, z = sol2
    x = (d - b*y - c*z) / a

    print(f"y = {f(y)}")
    print(f"z = {f(z)}")

    print("\nPaso 4: Sustituimos y, z para hallar x")
    print(f"x = ({f(d)} - {f(b)}({f(y)}) - {f(c)}({f(z)})) / {f(a)}")
    print(f"x = {f(x)}")

    return x, y, z


def eliminacion(A, B):
    print("\n========== MÉTODO DE ELIMINACIÓN ==========")

    M = [A[i][:] + [B[i]] for i in range(3)]

    print("\nPaso 1: Eliminamos x de E2 y E3")

    for fila in [1, 2]:
        if M[0][0] == 0:
            print("No se puede usar E1 como pivote porque tiene cero en x.")
            return None

        factor = M[fila][0] / M[0][0]
        print(f"E{fila+1} = E{fila+1} - ({f(factor)})E1")

        for j in range(4):
            M[fila][j] = M[fila][j] - factor*M[0][j]

        print(
            f"Nueva E{fila+1}: {f(M[fila][1])}y + {f(M[fila][2])}z = {f(M[fila][3])}")

    print("\nPaso 2: Eliminamos y de E3")

    if M[1][1] == 0:
        print("No se puede continuar porque el pivote de y es cero.")
        return None

    factor = M[2][1] / M[1][1]
    print(f"E3 = E3 - ({f(factor)})E2")

    for j in range(4):
        M[2][j] = M[2][j] - factor*M[1][j]

    print(f"Nueva E3: {f(M[2][2])}z = {f(M[2][3])}")

    z = M[2][3] / M[2][2]
    y = (M[1][3] - M[1][2]*z) / M[1][1]
    x = (M[0][3] - M[0][1]*y - M[0][2]*z) / M[0][0]

    print("\nPaso 3: Sustitución hacia atrás")
    print(f"z = {f(z)}")
    print(f"y = {f(y)}")
    print(f"x = {f(x)}")

    return x, y, z


def determinante_3x3(M):
    positivo = M[0][0]*M[1][1]*M[2][2] + M[0][1] * \
        M[1][2]*M[2][0] + M[0][2]*M[1][0]*M[2][1]
    negativo = M[0][2]*M[1][1]*M[2][0] + M[0][0] * \
        M[1][2]*M[2][1] + M[0][1]*M[1][0]*M[2][2]
    return positivo - negativo


def mostrar_matriz(M, nombre):
    print(f"\n{nombre}:")
    for fila in M:
        print([f(x) for x in fila])


def cramer(A, B):
    print("\n========== MÉTODO DE CRAMER ==========")

    print("\nPaso 1: Calculamos el determinante principal Ds")
    mostrar_matriz(A, "Matriz Ds")

    Ds = determinante_3x3(A)
    print(f"Ds = {f(Ds)}")

    if Ds == 0:
        print("No se puede aplicar Cramer porque Ds = 0.")
        return None

    Dx = [[B[i], A[i][1], A[i][2]] for i in range(3)]
    Dy = [[A[i][0], B[i], A[i][2]] for i in range(3)]
    Dz = [[A[i][0], A[i][1], B[i]] for i in range(3)]

    print("\nPaso 2: Calculamos Dx, Dy y Dz")

    mostrar_matriz(Dx, "Matriz Dx")
    dx = determinante_3x3(Dx)
    print(f"Dx = {f(dx)}")

    mostrar_matriz(Dy, "Matriz Dy")
    dy = determinante_3x3(Dy)
    print(f"Dy = {f(dy)}")

    mostrar_matriz(Dz, "Matriz Dz")
    dz = determinante_3x3(Dz)
    print(f"Dz = {f(dz)}")

    print("\nPaso 3: Aplicamos las fórmulas")
    x = dx / Ds
    y = dy / Ds
    z = dz / Ds

    print(f"x = Dx / Ds = {f(dx)} / {f(Ds)} = {f(x)}")
    print(f"y = Dy / Ds = {f(dy)} / {f(Ds)} = {f(y)}")
    print(f"z = Dz / Ds = {f(dz)} / {f(Ds)} = {f(z)}")

    return x, y, z


def gauss(A, B):
    print("\n========== MÉTODO DE GAUSS ==========")

    M = [A[i][:] + [B[i]] for i in range(3)]

    print("\nMatriz aumentada inicial:")
    mostrar_matriz(M, "M")

    for i in range(3):
        if M[i][i] == 0:
            for k in range(i+1, 3):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    print(f"Se intercambia F{i+1} con F{k+1}")
                    break

        pivote = M[i][i]

        if pivote == 0:
            print("No se puede continuar porque el pivote es cero.")
            return None

        for k in range(i+1, 3):
            factor = -M[k][i] / pivote
            print(f"\nF{k+1} = {f(factor)}F{i+1} + F{k+1}")

            for j in range(i, 4):
                M[k][j] = factor*M[i][j] + M[k][j]

            mostrar_matriz(M, "Matriz actual")

    print("\nMatriz triangular superior obtenida:")
    mostrar_matriz(M, "M")

    z = M[2][3] / M[2][2]
    y = (M[1][3] - M[1][2]*z) / M[1][1]
    x = (M[0][3] - M[0][1]*y - M[0][2]*z) / M[0][0]

    print("\nSustitución hacia atrás:")
    print(f"z = {f(M[2][3])} / {f(M[2][2])} = {f(z)}")
    print(f"y = ({f(M[1][3])} - {f(M[1][2])}({f(z)})) / {f(M[1][1])} = {f(y)}")
    print(
        f"x = ({f(M[0][3])} - {f(M[0][1])}({f(y)}) - {f(M[0][2])}({f(z)})) / {f(M[0][0])} = {f(x)}")

    return x, y, z


def gauss_jordan(A, B):
    print("\n========== MÉTODO DE GAUSS-JORDAN ==========")

    M = [A[i][:] + [B[i]] for i in range(3)]

    print("\nMatriz aumentada inicial:")
    mostrar_matriz(M, "M")

    for i in range(3):
        if M[i][i] == 0:
            for k in range(i+1, 3):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    print(f"Se intercambia F{i+1} con F{k+1}")
                    break

        pivote = M[i][i]

        if pivote == 0:
            print("No se puede continuar porque el pivote es cero.")
            return None

        print(f"\nF{i+1} = F{i+1} / {f(pivote)}")

        for j in range(4):
            M[i][j] = M[i][j] / pivote

        mostrar_matriz(M, "Matriz actual")

        for k in range(3):
            if k != i:
                factor = -M[k][i]
                print(f"\nF{k+1} = {f(factor)}F{i+1} + F{k+1}")

                for j in range(4):
                    M[k][j] = factor*M[i][j] + M[k][j]

                mostrar_matriz(M, "Matriz actual")

    print("\nMatriz identidad obtenida:")
    mostrar_matriz(M, "M")

    x = M[0][3]
    y = M[1][3]
    z = M[2][3]

    print("\nSolución directa:")
    print(f"x = {f(x)}")
    print(f"y = {f(y)}")
    print(f"z = {f(z)}")

    return x, y, z


def leer_sistema():
    A = []
    B = []

    print("\nIngrese el sistema en forma ax + by + cz = d")
    print("Puede ingresar enteros, decimales o fracciones. Ejemplo: 2, 0.5, 1/2")

    for i in range(3):
        print(f"\nEcuación {i+1}:")
        a = leer_fraccion("Coeficiente de x: ")
        b = leer_fraccion("Coeficiente de y: ")
        c = leer_fraccion("Coeficiente de z: ")
        d = leer_fraccion("=: ")

        A.append([a, b, c])
        B.append(d)

    return A, B


def ejemplo_problema_1():
    A = [
        [Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1, 2), Fraction(1), Fraction(2)]
    ]

    B = [
        Fraction(100),
        Fraction(80),
        Fraction(50)
    ]

    return A, B


def menu():
    print("========== PROGRAMA SISTEMAS 3x3 ==========")
    print("1. Usar ejemplo del Problema 1")
    print("2. Ingresar mi propio sistema")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        A, B = ejemplo_problema_1()
    elif opcion == "2":
        A, B = leer_sistema()
    else:
        print("Opción incorrecta.")
        return

    imprimir_sistema(A, B)

    while True:
        print("\n========== MENÚ ==========")
        print("1. Igualación")
        print("2. Sustitución")
        print("3. Eliminación")
        print("4. Cramer")
        print("5. Gauss")
        print("6. Gauss-Jordan")
        print("7. Todos los métodos")
        print("8. Salir")

        metodo = input("Seleccione el método: ")

        if metodo == "1":
            sol = igualacion(A, B)
            comprobacion(A, B, sol)

        elif metodo == "2":
            sol = sustitucion(A, B)
            comprobacion(A, B, sol)

        elif metodo == "3":
            sol = eliminacion(A, B)
            comprobacion(A, B, sol)

        elif metodo == "4":
            sol = cramer(A, B)
            comprobacion(A, B, sol)

        elif metodo == "5":
            sol = gauss(A, B)
            comprobacion(A, B, sol)

        elif metodo == "6":
            sol = gauss_jordan(A, B)
            comprobacion(A, B, sol)

        elif metodo == "7":
            sol = igualacion(A, B)
            comprobacion(A, B, sol)

            sol = sustitucion(A, B)
            comprobacion(A, B, sol)

            sol = eliminacion(A, B)
            comprobacion(A, B, sol)

            sol = cramer(A, B)
            comprobacion(A, B, sol)

            sol = gauss(A, B)
            comprobacion(A, B, sol)

            sol = gauss_jordan(A, B)
            comprobacion(A, B, sol)

        elif metodo == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción incorrecta.")


menu()
