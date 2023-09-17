import matplotlib.pyplot as plt
import numpy as np
def spline(x, y):
    n=len(x)
    #se crea un diccionario con liso valores de cada x 
    a = {k: v for k, v in enumerate(y)}
    #se calcula la diferencia entre los  valores de x
    h = {k: x[k+1] - x[k] for k in range(n - 1)}
    #se crea la matrz A con la primera fila de unos y ceros
    A = [[1] + [0] * (n - 1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        #se agrega cada fila  la matriz A
        A.append(row)
        #se agrega la ultima fil ade ceros con uno en la ultima columna
    A.append([0] * (n-1) + [1]) 
    B=[0]
    #se crea una lista B con un cero inicial
    for k in range(1,n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1])/h[k-1]
        B.append(row)
    #se agrega un cero al final
    B.append(0)
    c = dict(zip(range(n), np.linalg.solve(A,B)))
    #se crean los diccionarios para almacenar los coeficientes
    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        #se calcula cada coeficiente d
        d[k] = (c[k+1] - c[k])/(3*h[k])
    #se crea un diccionario 
    s = {}
    for k in range(n-1):
        #se guardan las ecucaciones del spline
        eq = f'{a[k]}{b[k]:+}*(x-{x[k]}){c[k]:+}*(x-{x[k]})**2{d[k]:+}*(x-{x[k]})**3'
        s[k] = {'eq': eq, 'domain': [x[k],x[k+1]]}
    #se retorna al diccionario 
    return s
#valores de x y de y
x = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0]
y = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25]
eqs = spline(x,y)
print(eqs)
# aqui gneeramos los gtraficos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'],100)
    plt.plot(t,p(t),label=f"$S_{key}(x)$")
    # aqui se genera la imagen
plt.scatter(x,y)
#plt.legend()
plt.savefig('spline.png')
plt.show()
