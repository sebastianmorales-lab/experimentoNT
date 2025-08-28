#Images resized
from PIL import Image
import os

target_size = (512, 512)
input_folder = "imagenes_originales"
output_folder = "imagenes_redimensionadas"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        img = Image.open(os.path.join(input_folder, filename)).convert("RGBA")
        img_resized = img.resize(target_size, Image.ANTIALIAS)
        img_resized.save(os.path.join(output_folder, filename))