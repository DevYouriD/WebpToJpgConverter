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

# UI VERSION
# import PIL.Image
# from tkinter import *
# import os

# window = Tk()
# #window.iconbitmap('Resources/[FILENAME].ico')
# window.title('Image Converter')
# window.config(height=500, width=500, background='black')

# #MAIN FUNCTIONALITY
# def convertImage():
#     desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#     image = PIL.Image.open("Resources/test.webp").convert("RGB")
#     image.save(desktop + "\\test.jpg", "jpeg")

# Button(window, text='DO STUFF', command=convertImage, font='none 10 bold').place(relx=0.1, rely=0.2, anchor=CENTER)

# #CLOSE
# def close_window():
#     window.destroy()
#     exit()

# Button(window, text='EXIT', width=6, command=close_window, font='none 10 bold').place(relx=0.08, rely=0.95, anchor=CENTER)

# window.mainloop()