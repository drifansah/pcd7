#Import Library
import matplotlib.pyplot as plt#plt sebagai objejk marplotib.pyplot
#matplotlib inline

from skimage import data#di import fungsi data dari library skimage
from skimage.io import imread#di import fungsi imread dari library skimage
from skimage.color import rgb2gray #di import fungsi rgb2gray dari library skimage
import numpy as np#np sebagai objek numpy

import cv2
#Load Image
citra1 = imread(fname="vespa.jpg")
print(citra1.shape)#tampilkan pada terminal nilai ukuran citra1

plt.imshow(citra1, cmap='gray')#tampilkan citra1 dengan warna gray
#Proses Konvolusi
kernel = np.array([[-1, 0, -1], #membuat kernel 3x3
                   [0, 4, 0], 
                   [-1, 0, -1]])

citraOutput = cv2.filter2D(citra1, -1, kernel)#cv2.filter2D() digunakan untuk menerapkan filter kernel pada citra citra1
#citra1: Citra yang akan diolah menggunakan filter kernel. Citra ini dapat berupa citra grayscale atau citra berwarna.
#-1: Parameter kedua yang menentukan kedalaman (depth) citra output. Nilai -1 menandakan bahwa kedalaman output akan sama dengan kedalaman citra input.
#kernel: Kernel filter yang akan diterapkan pada citra. Kernel ini adalah matriks yang berisi bobot untuk mempengaruhi piksel-piksel di sekitarnya.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap = 'gray')
ax[1].set_title("Citra Output")
plt.show()
