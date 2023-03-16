import PIL.Image
import os

baseDirectory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
sourceDirectory = baseDirectory + "Resources"
targetDirectory = baseDirectory + "Results"

def convertFiles():
    index = 0
    for file in os.listdir(sourceDirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".webp"): 
            image = PIL.Image.open(sourceDirectory + "\\" + filename).convert("RGB")
            image.save(targetDirectory + f"\\image{index}.jpg", "jpeg")
            index += 1

if not os.path.exists(sourceDirectory):
    os.makedirs(sourceDirectory)
if not os.path.exists(targetDirectory):
    os.makedirs(targetDirectory)
if os.path.exists(sourceDirectory) and os.path.exists(sourceDirectory):
    convertFiles()
