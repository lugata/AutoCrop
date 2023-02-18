import cv2

# Load the image and convert it to grayscale
image = cv2.imread('foto/foto 1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the face detector and detect faces in the image
detector = cv2.CascadeClassifier('library/model1.xml')
faces = detector.detectMultiScale(gray, 1.3, 5)

# Memuat model deteksi wajah menggunakan cv2 Cascade Classifier
face_detector = cv2.CascadeClassifier("library/model1.xml")

# Melakukan cropping pada gambar jika wajah terdeteksi
if len(faces) > 0:
  # Mengambil koordinat wajah pertama yang terdeteksi
  x, y, w, h = faces[0]

  height = 1800 # Tinggi foto yang diinginkan
  # Menghitung ukuran cropping yang diinginkan
  top_crop = int(height * 0.25) # 25% dari tinggi wajah
  bottom_crop = int(height * 0.75) # 75% dari tinggi wajah
  width = 1200 # Lebar foto yang diinginkan

  # Melakukan cropping pada gambar
  cropped_image = image[y - top_crop:y + bottom_crop, x:x + w]

  # Mengubah ukuran gambar yang telah di-cropping
  resized_image = cv2.resize(cropped_image, (width, height))

  # Menyimpan gambar yang telah di-cropping dan diubah ukurannya
  cv2.imwrite("foto_cropped.jpg", resized_image)
