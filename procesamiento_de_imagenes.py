from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

# PARTE I - Transformando una imagen de color a escala de grises

# Aquí importamos el archivo de imagen como una matriz de formas (nx, ny, nz)
archivo_imagen = 'Lena.PNG'
imagen_entrada = imread(archivo_imagen)  # esta es la representación de matriz de la imagen de entrada
[nx, ny, nz] = np.shape(imagen_entrada)  # nx: alto, ny: ancho, nz: colores (RGB)

# Extrayendo cada uno de los componentes RGB
r_img, g_img, b_img = imagen_entrada[:, :, 0], imagen_entrada[:, :, 1], imagen_entrada[:, :, 2]

# La siguiente operación tomará pesos y parámetros para convertir la imagen en color a escala de grises
gamma = 1.400  # un parametro
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722  # pesos para los componentes RGB respectivamente
imagen_escala_grises = r_const * r_img ** gamma + g_const * g_img ** gamma + b_const * b_img ** gamma

# Este comando mostrará la imagen en escala de grises junto a la imagen original
fig1 = plt.figure(1)
ax1, ax2 = fig1.add_subplot(121), fig1.add_subplot(122)
ax1.imshow(imagen_entrada)
ax2.imshow(imagen_escala_grises, cmap=plt.get_cmap('gray'))
fig1.show()

# PARTE II - Aplicando el operador de Sobel

# Aquí definimos las matrices asociadas al filtro Sobel
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
[filas, columnas] = np.shape(imagen_escala_grises)  # debemos conocer la forma de la entrada de la imagen de escala de grises
imagen_filtro_sobel = np.zeros(shape=(filas, columnas))  # inicialización de la salida de la imagen

# Ahora "barremos" la imagen en ambas direcciones x e y y calculamos la salida
for i in range(filas - 2):
    for j in range(columnas - 2):
        gx = np.sum(np.multiply(Gx, imagen_escala_grises[i:i + 3, j:j + 3]))  # dirección x
        gy = np.sum(np.multiply(Gy, imagen_escala_grises[i:i + 3, j:j + 3]))  # dirección y
        imagen_filtro_sobel[i + 1, j + 1] = np.sqrt(gx ** 2 + gy ** 2)  # calculo de la hipotenusa

# Mostrar la imagen original y la imagen filtrada de Sobel
fig2 = plt.figure(2)
ax1, ax2 = fig2.add_subplot(121), fig2.add_subplot(122)
ax1.imshow(imagen_entrada)
ax2.imshow(imagen_filtro_sobel, cmap=plt.get_cmap('gray'))
fig2.show()
