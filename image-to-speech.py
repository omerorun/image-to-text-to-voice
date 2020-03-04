import cv2
from gtts import gTTS
import os
import pytesseract
# path of the tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'

# path of the image that contains text
path = r'C:\Users\user\Desktop\deneme3.jpeg'
  
# Using cv2.imread() method 
img = cv2.imread(path) 

text = pytesseract.image_to_string(img)

language = 'tr'

audio = gTTS(text=text, lang=language, slow=False)

#saves the file
audio.save('sesDeneme.mp3')
#runs the file
os.system("start sesDeneme.mp3")