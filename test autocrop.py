import sys
from pathlib import Path

import PIL
from PIL import Image
from autocrop import Cropper

cropper = Cropper(width=1200, height=1800, face_percent=30)

crop_positions = cropper._crop_positions

crop_positions(1200, 1800, 1346, 1406, 1588, 1588)

#Get a Numpy array of the cropped image
cropped_array = cropper.crop('foto/foto 1.jpg')

cropped_image = Image.fromarray(cropped_array)

cropped_image.save('cropped.jpg', dpi=(300, 300))