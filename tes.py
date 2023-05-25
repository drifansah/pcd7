# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
#jika menggunakan google colab jgn lupa load code di bawah ini
#from google.colab.patches import cv2_imshow


#bgr
img = cv2.imread('vespa.jpg')

#rgb
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# tampilkan gambar awal tanpa filter
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5,5),np.float32)/25
print(kernel)

# lakukan filtering
kucing_filter = cv2.filter2D(img,-1,kernel)
cv2.imshow('image',kucing_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)

# plot pertama, gambar asli
plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])

# kedua, hasil filter
plt.subplot(122),plt.imshow(kucing_filter),
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Plot!
plt.show()