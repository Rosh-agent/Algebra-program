from fractions import Fraction


def f(valor):
    return str(valor) if valor.denominator != 1 else str(valor.numerator)


def leer_fraccion(mensaje):
    while True:
        try:
            dato = input(mensaje).strip().replace(",", ".")
            valor = Fraction(dato)
            return valor
        except:
            print("Error: ingrese un número válido. Ejemplo: 2, 0.5 o 1/2")


def imprimir_sistema(A, B):
    print("\nSistema ingresado:")
    variables = ["x", "y", "z"]
    for i in range(3):
        ecuacion = ""
        for j in range(3):
            signo = " + " if j > 0 and A[i][j] >= 0 else " "
            ecuacion += signo + f(A[i][j]) + variables[j]
        ecuacion += " = " + f(B[i])
        print("E" + str(i + 1) + ":", ecuacion)


def determinante_3x3(M):
    dp = M[0][0]*M[1][1]*M[2][2] + M[0][1] * \
        M[1][2]*M[2][0] + M[0][2]*M[1][0]*M[2][1]
    ds = M[0][2]*M[1][1]*M[2][0] + M[0][0] * \
        M[1][2]*M[2][1] + M[0][1]*M[1][0]*M[2][2]
    return dp - ds


def cramer(A, B):
    print("\n========== MÉTODO DE CRAMER ==========")

    Ds = determinante_3x3(A)
    print("Ds =", f(Ds))

    if Ds == 0:
        print("No se puede aplicar Cramer porque Ds = 0")
        return None

    Dx = [[B[i], A[i][1], A[i][2]] for i in range(3)]
    Dy = [[A[i][0], B[i], A[i][2]] for i in range(3)]
    Dz = [[A[i][0], A[i][1], B[i]] for i in range(3)]

    dx = determinante_3x3(Dx)
    dy = determinante_3x3(Dy)
    dz = determinante_3x3(Dz)

    print("Dx =", f(dx))
    print("Dy =", f(dy))
    print("Dz =", f(dz))

    x = dx / Ds
    y = dy / Ds
    z = dz / Ds

    print("x = Dx / Ds =", f(x))
    print("y = Dy / Ds =", f(y))
    print("z = Dz / Ds =", f(z))

    return x, y, z


def gauss(A, B):
    print("\n========== MÉTODO DE GAUSS ==========")

    M = [A[i][:] + [B[i]] for i in range(3)]

    for i in range(3):
        if M[i][i] == 0:
            for k in range(i + 1, 3):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    print("Se intercambia F", i + 1, "con F", k + 1)
                    break

        pivote = M[i][i]

        if pivote == 0:
            print("No se puede continuar, pivote cero.")
            return None

        for k in range(i + 1, 3):
            factor = -M[k][i] / pivote
            print("F" + str(k + 1), "=", f(factor),
                  "F" + str(i + 1), "+ F" + str(k + 1))

            for j in range(i, 4):
                M[k][j] = factor * M[i][j] + M[k][j]

    print("\nMatriz triangular:")
    for fila in M:
        print([f(x) for x in fila])

    z = M[2][3] / M[2][2]
    y = (M[1][3] - M[1][2] * z) / M[1][1]
    x = (M[0][3] - M[0][1] * y - M[0][2] * z) / M[0][0]

    print("\nz =", f(z))
    print("y =", f(y))
    print("x =", f(x))

    return x, y, z


def gauss_jordan(A, B):
    print("\n========== MÉTODO DE GAUSS-JORDAN ==========")

    M = [A[i][:] + [B[i]] for i in range(3)]

    for i in range(3):
        if M[i][i] == 0:
            for k in range(i + 1, 3):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    print("Se intercambia F", i + 1, "con F", k + 1)
                    break

        pivote = M[i][i]

        if pivote == 0:
            print("No se puede continuar, pivote cero.")
            return None

        print("F" + str(i + 1), "= F" + str(i + 1), "/", f(pivote))

        for j in range(4):
            M[i][j] = M[i][j] / pivote

        for k in range(3):
            if k != i:
                factor = -M[k][i]
                print("F" + str(k + 1), "=", f(factor),
                      "F" + str(i + 1), "+ F" + str(k + 1))

                for j in range(4):
                    M[k][j] = factor * M[i][j] + M[k][j]

    print("\nMatriz identidad:")
    for fila in M:
        print([f(x) for x in fila])

    x = M[0][3]
    y = M[1][3]
    z = M[2][3]

    print("\nx =", f(x))
    print("y =", f(y))
    print("z =", f(z))

    return x, y, z


def eliminacion(A, B):
    print("\n========== MÉTODO DE ELIMINACIÓN ==========")
    return gauss(A, B)


def sustitucion(A, B):
    print("\n========== MÉTODO DE SUSTITUCIÓN ==========")

    if A[0][0] == 0:
        print("No se puede despejar x desde E1 porque su coeficiente es 0.")
        return None

    print("Despejamos x de E1:")
    print("x = (" + f(B[0]) + " - " + f(A[0][1]) +
          "y - " + f(A[0][2]) + "z) / " + f(A[0][0]))

    a = A[0][0]
    b = A[0][1]
    c = A[0][2]
    d = B[0]

    nueva_A = []
    nueva_B = []

    for i in [1, 2]:
        coef_y = A[i][1] - A[i][0] * b / a
        coef_z = A[i][2] - A[i][0] * c / a
        indep = B[i] - A[i][0] * d / a

        nueva_A.append([coef_y, coef_z])
        nueva_B.append(indep)

    print("\nSistema reducido en y, z:")
    print(f(nueva_A[0][0]) + "y + " +
          f(nueva_A[0][1]) + "z = " + f(nueva_B[0]))
    print(f(nueva_A[1][0]) + "y + " +
          f(nueva_A[1][1]) + "z = " + f(nueva_B[1]))

    det = nueva_A[0][0]*nueva_A[1][1] - nueva_A[0][1]*nueva_A[1][0]

    if det == 0:
        print("No tiene solución única.")
        return None

    dy = nueva_B[0]*nueva_A[1][1] - nueva_A[0][1]*nueva_B[1]
    dz = nueva_A[0][0]*nueva_B[1] - nueva_B[0]*nueva_A[1][0]

    y = dy / det
    z = dz / det
    x = (d - b*y - c*z) / a

    print("\ny =", f(y))
    print("z =", f(z))
    print("x =", f(x))

    return x, y, z


def igualacion(A, B):
    print("\n========== MÉTODO DE IGUALACIÓN ==========")

    if A[0][0] == 0 or A[1][0] == 0 or A[2][0] == 0:
        print("No se puede despejar x en todas las ecuaciones porque algún coeficiente de x es 0.")
        return None

    print("Despejamos x en E1, E2 y E3.")

    nuevas = []

    for i in range(3):
        a = A[i][0]
        b = A[i][1]
        c = A[i][2]
        d = B[i]
        print("E" + str(i + 1) + ": x = (" + f(d) +
              " - " + f(b) + "y - " + f(c) + "z) / " + f(a))

    for par in [(0, 1), (0, 2)]:
        i, j = par

        ai = A[i][0]
        bi = A[i][1]
        ci = A[i][2]
        di = B[i]

        aj = A[j][0]
        bj = A[j][1]
        cj = A[j][2]
        dj = B[j]

        coef_y = aj*bi - ai*bj
        coef_z = aj*ci - ai*cj
        indep = aj*di - ai*dj

        nuevas.append([coef_y, coef_z, indep])

    print("\nSistema obtenido al igualar:")
    print(f(nuevas[0][0]) + "y + " +
          f(nuevas[0][1]) + "z = " + f(nuevas[0][2]))
    print(f(nuevas[1][0]) + "y + " +
          f(nuevas[1][1]) + "z = " + f(nuevas[1][2]))

    det = nuevas[0][0]*nuevas[1][1] - nuevas[0][1]*nuevas[1][0]

    if det == 0:
        print("No tiene solución única.")
        return None

    dy = nuevas[0][2]*nuevas[1][1] - nuevas[0][1]*nuevas[1][2]
    dz = nuevas[0][0]*nuevas[1][2] - nuevas[0][2]*nuevas[1][0]

    y = dy / det
    z = dz / det

    x = (B[0] - A[0][1]*y - A[0][2]*z) / A[0][0]

    print("\ny =", f(y))
    print("z =", f(z))
    print("x =", f(x))

    return x, y, z


def comprobacion(A, B, solucion):
    print("\n========== COMPROBACIÓN ==========")

    if solucion is None:
        print("No se puede comprobar porque no hay solución.")
        return

    x, y, z = solucion

    for i in range(3):
        resultado = A[i][0]*x + A[i][1]*y + A[i][2]*z
        print("E" + str(i + 1) + ":")
        print(f(A[i][0]) + "(" + f(x) + ") + " + f(A[i][1]) + "(" +
              f(y) + ") + " + f(A[i][2]) + "(" + f(z) + ") = " + f(resultado))

        if resultado == B[i]:
            print(f(resultado), "=", f(B[i]), "Correcto")
        else:
            print(f(resultado), "!=", f(B[i]), "Incorrecto")


def leer_sistema():
    A = []
    B = []

    print("Ingrese los coeficientes del sistema 3x3")
    print("Forma: ax + by + cz = d\n")

    for i in range(3):
        print("Ecuación", i + 1)
        a = leer_fraccion("Coeficiente de x: ")
        b = leer_fraccion("Coeficiente de y: ")
        c = leer_fraccion("Coeficiente de z: ")
        d = leer_fraccion("Resultado: ")

        A.append([a, b, c])
        B.append(d)
        print()

    return A, B


def ejemplo_problema_1():
    A = [
        [Fraction(2), Fraction(1), Fraction(3)],
        [Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(4)]
    ]

    B = [
        Fraction(100),
        Fraction(80),
        Fraction(100)
    ]

    return A, B


def menu():
    print("========== PROGRAMA DE MÉTODOS DE SISTEMAS 3x3 ==========")
    print("1. Usar ejemplo del Problema 1")
    print("2. Ingresar mi propio sistema")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        A, B = ejemplo_problema_1()
    elif opcion == "2":
        A, B = leer_sistema()
    else:
        print("Opción inválida.")
        return

    imprimir_sistema(A, B)

    while True:
        print("\n========== MENÚ DE MÉTODOS ==========")
        print("1. Igualación")
        print("2. Sustitución")
        print("3. Eliminación")
        print("4. Cramer")
        print("5. Gauss")
        print("6. Gauss-Jordan")
        print("7. Todos los métodos")
        print("8. Salir")

        metodo = input("Seleccione un método: ")

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
            print("Opción inválida.")


menu()
