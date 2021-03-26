import pylab as pl
import numpy as np


def _loadDots():
    array = []
    file = open("dots.txt", "r")
    for line in file:
        array.append(eval(line))
    return array


def _loadDotToStar():
    dot = []
    file = open("dot-star.txt", "r")
    dot = eval(file.readline())
    return dot


def _validarPuntoAEstrellar(x, y, S):
    X = []
    Y = []
    for p in S:
        X.append(p[0])
        Y.append(p[1])

    X.sort()
    Y.sort()

    if(x > X[len(X)-1]):
        print('ES MAYOR AL PUNTO MAS LEJANO EN X')
        return False
    elif(x < X[0]):
        print('ES MENOR AL PUNTO MAS CERCANO EN X')
        return False

    if(y > Y[len(Y)-1]):
        print('ES MAYOR AL PUNTO MAS LEJANO EN Y')
        return False
    elif(y < Y[0]):
        print('ES MENOR AL PUNTO MAS CERCANO EN Y')
        return False

    return True


A = _loadDots()
P = _loadDotToStar()
X = []
Y = []

fig = pl.figure()
ax = fig.add_subplot(111)

for i, point in enumerate(A):
    pl.plot(point[0], point[1], marker="o", color="red")
    pl.annotate('P['+str(i)+']',
                xy=(point[0], point[1]), xycoords='data',
                xytext=(+10, +30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    X.append(point[0])
    Y.append(point[1])

# Para cerrar el polígono.
X.append(A[0][0])
Y.append(A[0][1])

ax.plot(X, Y, color="blue")

if(_validarPuntoAEstrellar(P[0], P[1], A)):
    ax.plot(P[0], P[1], marker="o")

    for i in A:
        ax.plot([P[0], i[0]], [P[1], i[1]], color="green")

pl.show()
