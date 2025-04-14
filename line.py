import math as math
def line():

     A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese e;; coeficiente X2: "))
    print("El coeficiente A de su ecuación en la recta es: ", A)
    print("El coeficiente B de su ecuación en la recta es: ", B)
    print("El coeficiente X1 de su ecuación en la recta es: ",  X1)
    print("El coeficiente X2 de su ecuación en la recta es: ", X2)
    print("Para la siguiente ecuación: ")
    print(f"\tY = {A}X + {B}")
    print("Dado los siguientes puntos: ")
    Y1 = A * X1 + B
    Y2 = A * X2 + B
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")
    P1 = (X1, A*X1 + B)
    P2 = (X2, A*X2 + B)
    print(f"La distancia entre ellos es: {math.dist(P1, P2)}")
