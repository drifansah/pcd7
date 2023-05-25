#Import Library
import matplotlib.pyplot as plt
#matplotlib inline

from skimage import data#di import fungsi data dari library skimage
from skimage.io import imread#di import fungsi imread dari library skimage
from skimage.color import rgb2gray #di import fungsi rgb2gray dari library skimage
import numpy as np#np sebagai objek numpy

#Load & Plot Input Image
citra1 = imread(fname="boneka2.tif")
citra2 = imread(fname="vespa2.jpg")

print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Citra 2")
plt.show()

#Menyiapkan variable output
copyCitra1 = citra1.copy()#mengcopy gambar pada citra1 ke dalam variabel copycitra1
copyCitra2 = citra2.copy()

m1,n1= copyCitra1.shape
output1 = np.empty([m1, n1])#Array output1 dibuat menggunakan np.empty() dengan ukuran yang sama seperti citra asli.

m2,n2 ,d2= copyCitra2.shape
output2 = np.empty([m2, n2, d2])
print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)

print('m1 : ',m1)
print('n1 : ',n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()

#Proses Filter Batas Pada Citra Input 1
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        
        a1 = baris
        b1 = kolom
        
        #rumus dari filtering batas
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
        #penentuan nilai piksel   
        if np.any(copyCitra1[baris, kolom] < minPiksel ):
            output1[baris, kolom] = minPiksel
        else :
            if np.any(copyCitra1[baris, kolom] > maksPiksel) :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]
#Proses Filter Batas Pada Citra Input 2
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        
        a1 = baris1
        b1 = kolom1
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if np.any(copyCitra2[baris1, kolom1] < minPiksel) :
            output2[baris1, kolom1] = minPiksel
        else :
            if np.any(copyCitra2[baris1, kolom1] > maksPiksel) :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]
#Plot Citra Input dan Output Hasil dari Filter Batas
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 2")

ax[2].imshow(output1, cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")
plt.show()