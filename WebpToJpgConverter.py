from PIL import Image
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
image = Image.open("Resources/test.webp").convert("RGB")
image.save(desktop + "\\test.jpg", "jpeg")