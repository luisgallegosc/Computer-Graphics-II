import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from matplotlib.animation import FuncAnimation

# superficie bezier con 16 puntos
# puntos de borde
A = np.array([0, 0, 0])
B = np.array([1, 0, 1])
C = np.array([1, 1, 0])
D = np.array([0, 1, 1])

# puntos centrales de control
E00 = np.array([0.2, 0.2, 0.5])
E10 = np.array([0.8, 0.2, 0.5])
E11 = np.array([0.8, 0.8, 0.5])
E01 = np.array([0.2, 0.8, 0.5])

# puntos de control
AB0 = np.array([0.3, 0, 0.7])
AB1 = np.array([0.7, 0, 0.7])
BC0 = np.array([1, 0.3, 0.7])
BC1 = np.array([1, 0.7, 0.7])
CD1 = np.array([0.7, 1, 0.7])
CD0 = np.array([0.3, 1, 0.7])
DA1 = np.array([0, 0.7, 0.7])
DA0 = np.array([0, 0.3, 0.7])

# interpolacion lineal
n = 16
ss = np.linspace(0, 1, n)
ts = np.linspace(0, 1, n)
shape = (n, n, 3)

# Función para interpolar sin índices
def interpolar0(A, B, C, D):
    """
    Realiza la interpolación sin índices de los puntos de control.
    """
    return np.array([
        (1-t)*(1-s)*A + (1-t)*s*B + t*(1-s)*D + t*s*C
        for s in ss for t in ts]).reshape(shape)

# Función para interpolar con índices
def interpolar(A, B, C, D):
    """
    Realiza la interpolación con índices de los puntos de control.
    """
    return np.array([
        (1-t)*(1-s)*A[i, j] + (1-t)*s*B[i, j] + t*(1-s)*D[i, j] + t*s*C[i, j]
        for i, s in enumerate(ss) for j, t in enumerate(ts)]).reshape(shape)

# primera interpolacion
P00 = interpolar0(A, AB0, E00, DA0)
P01 = interpolar0(AB0, AB1, E10, E00)
P02 = interpolar0(AB1, B, BC0, E10)
P10 = interpolar0(DA0, E00, E01, DA1)
P11 = interpolar0(E00, E10, E11, E01)
P12 = interpolar0(E10, BC0, BC1, E11)
P20 = interpolar0(DA1, E01, CD0, D)
P21 = interpolar0(E01, E11, CD1, CD0)
P22 = interpolar0(E11, BC1, C, CD1)

# segunda interpolacion
Q00 = interpolar(P00, P01, P11, P10)
Q01 = interpolar(P01, P02, P12, P11)
Q10 = interpolar(P10, P11, P21, P20)
Q11 = interpolar(P11, P12, P22, P21)

# ultima interpolacion
R = interpolar(Q00, Q01, Q11, Q10)
xs = R[:,:,0]
ys = R[:,:,1]
zs = R[:,:,2]

# dibujar
fig = plt.figure(figsize=(8, 8))
s = fig.add_subplot(111, projection="3d")

# dibujar superficie
s.plot_surface(xs, ys, zs)

# dibujar alambres
def alambre(A, B):
    """
    Dibuja un alambre entre dos puntos.
    """
    xyz = list(zip(A, B))
    s.plot(xyz[0], xyz[1], xyz[2], color="r", lw=2)
    pass

def alambres(A, B, C, D):
    """
    Dibuja los alambres de un polígono.
    """
    alambre(A, B)
    alambre(B, C)
    alambre(C, D)
    pass

alambres(A, AB0, AB1, B)
alambres(D, CD0, CD1, C)
alambres(A, DA0, DA1, D)
alambres(B, BC0, BC1, C)
alambres(DA0, E00, E10, BC0)
alambres(DA1, E01, E11, BC1)
alambres(AB0, E00, E01, CD0)
alambres(AB1, E10, E11, CD1)

# dibujar puntos
def poner_punto(p, label):
    """
    Dibuja un punto en el gráfico y le agrega una etiqueta.
    """
    s.scatter(p[0], p[1], p[2], color="b")
    s.text(p[0], p[1], p[2], label, size=20, color="k", zorder=1)
    pass

poner_punto(A, "A")
poner_punto(B, "B")
poner_punto(C, "C")
poner_punto(D, "D")
poner_punto(E00, "E00")
poner_punto(E01, "E01")
poner_punto(E11, "E11")
poner_punto(E10, "E10")
poner_punto(AB0, "AB0")
poner_punto(AB1, "AB1")
poner_punto(BC0, "BC0")
poner_punto(BC1, "BC1")
poner_punto(CD0, "CD0")
poner_punto(CD1, "CD1")
poner_punto(DA0, "DA0")
poner_punto(DA1, "DA1")

# axis
s.set_xlim(-0.2, 1.2)
s.set_ylim(-0.2, 1.2)
s.set_zlim(-0.2, 1.2)
s.set_xlabel("x")
s.set_ylabel("y")
s.set_zlabel("z")
s.view_init(elev=30., azim=-135)

plt.show()
