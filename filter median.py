#Import Library
import matplotlib.pyplot as plt
#matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np
#Load & Plot Input Image
citra1 = imread(fname="vespa2.jpg")
citra2 = imread(fname="astro.jpg")

print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Citra 2")

#Menyiapkan variable output
copyCitra1 = citra1.copy()
copyCitra2 = citra2.copy()

m1,n1, d1= copyCitra1.shape
output1 = np.empty([m1, n1, d1])

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
#Proses Filter Median Pada Citra Input 1
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]
        
        # Urutkan
        dataA = np.ravel(dataA)  # Flatten the array
        dataA.sort()
        
        output1[a1, b1] = dataA[5]
#Proses Filter Median Pada Citra Input 2
for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris  
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]
        
        # Urutkan
        dataA = np.ravel(dataA)  # Flatten the array
        dataA.sort()
        
        output2[a1, b1] = dataA[5]
#Plot Citra Input dan Output Hasil dari Filter Rerata
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 1")

ax[2].imshow(output1.astype(np.uint8), cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2.astype(np.uint8), cmap = 'gray')
ax[3].set_title("Output Citra 2")
plt.show()