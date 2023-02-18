#mengimport library yang dibutuhkan
import cv2
import numpy as np

#membaca gambar
image = cv2.imread('foto/foto 1.jpg')

#mengubah gambar menjadi grayscale untuk deteksi yang lebih mudah
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#menggunakan haar cascades untuk mendeteksi wajah di gambar
face_cascade = cv2.CascadeClassifier('library/model1.xml')
wajah = face_cascade.detectMultiScale(gray_image, 1.3, 5)

#menggambar bounding box di sekitar wajah yang terdeteksi
for (x,y,w,h) in wajah:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)

#mencari titik tengah koordinat bounding box wajah
x_tengah = x + w//2
y_tengah = y + h//2
titik_tengah = (x_tengah, y_tengah)

#memotong gambar hanya pada bounding box di sekitar wajah
wajah_terpotong = image[y:y+h, x:x+w]

#mengubah ukuran wajah yang terpotong menjadi persegi
wajah_terpotong_persegi = cv2.resize(wajah_terpotong, (400,400))

#menyimpan wajah yang terpotong dan diubah menjadi persegi sebagai gambar baru
cv2.imwrite('wajah_terpotong.jpg', wajah_terpotong_persegi)

