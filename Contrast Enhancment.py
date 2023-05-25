#import library
import numpy as np #np sebagai objek library numpy
import matplotlib.pyplot as plt #plt sebagai objek library matplotib.pyplot
#matplotlib inline
import cv2
import matplotlib.image as mpimg #mpimg sebagai objek library matplotib.image
from skimage import data #dari library skimage dipanggil fungsi data

#read image
image = cv2.imread('vespa2.jpg',0) #variabel image menampung gambar dengan format vespa.jpg

#Penerapan Histogram Equalization (HE)
image_equalized = cv2.equalizeHist(image)#Fungsi cv2.equalizeHist() digunakan untuk melakukan ekualisasi histogram pada citra grayscale.

#Penerapan Metode Contrast Limited Adaptive Histogram Equalization (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))#Fungsi cv2.createCLAHE() digunakan untuk membuat objek CLAHE. Parameter clipLimit menentukan batasan kontras yang diterapkan pada setiap bagian kecil citra, sedangkan tileGridSize menentukan ukuran grid untuk membagi citra menjadi bagian-bagian kecil yang independen.

#Apply CLAHE to the original image
image_clahe = clahe.apply(image)#Metode apply() dari objek CLAHE digunakan untuk menerapkan CLAHE pada citra asli. Hasilnya disimpan dalam variabel image_clahe.
#Penerapan metode Contrast Stretching (CS)
# Create an empty array to store the final output
# Contrast Stretching (CS) dilakukan untuk meningkatkan kontras dalam citra. Nilai intensitas piksel dalam citra diperpanjang ke seluruh rentang 0 hingga 255 dengan memanfaatkan nilai minimum dan maksimum. Hasilnya disimpan dalam variabel image_cs. Perhatikan bahwa citra hasil CS diubah menjadi tipe data 'uint8' menggunakan astype('uint8').
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#sebuah array kosong dengan ukuran yang sama seperti citra asli dibuat menggunakan np.zeros().

# Apply Min-Max Contrasting
#Variabel min dan max digunakan untuk menyimpan nilai intensitas piksel minimum dan maksimum dalam citra.
min = np.min(image)
max = np.max(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)
#Penerapan Metode Perkalian Konstanta
copyCamera = image.copy().astype(float)

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])#Array output1 dibuat menggunakan np.empty() dengan ukuran yang sama seperti citra copyCamera.

#Dalam nested loop ini, kita melakukan iterasi pada setiap baris dan kolom dalam citra.
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        #Variabel a1 dan b1 digunakan untuk menyimpan koordinat baris dan kolom piksel saat ini.
        a1 = baris
        b1 = kolom
        #Pada setiap iterasi, nilai piksel pada koordinat (baris, kolom) dalam citra copyCamera dikalikan dengan konstanta 1.9, dan hasilnya disimpan pada koordinat (a1, b1) dalam array output1.
        #Dengan melakukan operasi perkalian dengan konstanta, citra copyCamera akan mengalami peningkatan intensitas piksel. Nilai 1.9 dalam kode tersebut menunjukkan faktor perkalian yang diterapkan pada intensitas piksel. 
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9
#Plot Image
fig, axes = plt.subplots(5, 2, figsize=(20, 20))#terdapat 5 plot dan baris dua setiap plotnya serta ukuran plotnya 20x20
ax = axes.ravel()#axes adalah array multidimensi yang digunakan untuk mengatur tata letak subplots dalam sebuah gambar.
#Fungsi ravel() digunakan untuk mengubah array multidimensi menjadi array satu dimensi dengan urutan data yang sama seperti dalam array asli.

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(image_equalized, cmap=plt.cm.gray)
ax[2].set_title("Citra Output HE")
ax[3].hist(image_equalized.ravel(), bins=256)
ax[3].set_title('Histogram Output HE Method')

ax[4].imshow(image_cs, cmap=plt.cm.gray)
ax[4].set_title("Citra Output CS")
ax[5].hist(image_cs.ravel(), bins=256)
ax[5].set_title('Histogram Output CS Method')

ax[6].imshow(image_clahe, cmap=plt.cm.gray)
ax[6].set_title("Citra Grayscale CLAHE")
ax[7].hist(image_clahe.ravel(), bins=256)
ax[7].set_title('Histogram Output CLAHE Method')

ax[8].imshow(output1, cmap=plt.cm.gray)
ax[8].set_title("Citra Grayscale Perkalian Konstanta")
ax[9].hist(output1.ravel(), bins=256)
ax[9].set_title('Histogram Output Perkalian Konstanta Method')

fig.tight_layout()
plt.show()