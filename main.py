import cv2
from tkinter import filedialog as fd
import numpy as np
import pytesseract
from PIL import Image
import os

directory = r'C:\Users\Haier\Desktop\alpha'
# c=1
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg"):
#         im = Image.open(filename)
#         name='img'+str(c)+'.png'
#         rgb_im = im.convert('RGB')
#         rgb_im.save(name)
#         c+=1
#         print(os.path.join(directory, filename))
#         continue
#     else:
#         continue
#

#
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg"):
#         os.remove(filename)
#         continue
#     else:
#         continue


pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
t=0
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)
        with open('job'+str(t)+'.txt', "w") as f:
            f.writelines(text)
        t+=1



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
print(text)