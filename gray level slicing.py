#Import Library
import numpy as np #np sebagai objek library numpy
import matplotlib.pyplot as plt #plt sebagai objek library matplotib.pyplot
#matplotlib inline
import cv2
from skimage import data #dari library skimage dipanggil fungsi data

#Gray Level Slice
img = cv2.imread('astro.jpg', 0)

row, column = img.shape#inisialisai ukuran img oleh variabel row dan column

img1 = np.zeros((row,column),dtype = 'uint8')#sebuah array kosong dengan ukuran yang sama seperti citra asli dibuat menggunakan np.zeros().
 

min_range = 10#minimal panjang
max_range = 60#maksimal panjang
 

for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:#jika nilai pixel pada img >minimal dan <maksimal maka nilai piksel menjadi 255
            img1[i,j] = 255
        else:
            img1[i,j] = 0#jika nilai pixel pada img <minimal dan >maksimal maka nilai piksel menjadi 0
#Plot Image
fig, axes = plt.subplots(2, 2, figsize=(12, 12))#membuat plot baris 2 kolom 2 dengan ukuran setiap plot 12x12
ax = axes.ravel()#axes adalah array multidimensi yang digunakan untuk mengatur tata letak subplots dalam sebuah gambar.
#Fungsi ravel() digunakan untuk mengubah array multidimensi menjadi array satu dimensi dengan urutan data yang sama seperti dalam array asli.

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(img1, cmap=plt.cm.gray)
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()