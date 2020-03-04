Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# path 
path = r'C:\Users\user\Desktop\deneme.png'
  
# Using cv2.imread() method 
img = cv2.imread(path) 

text = pytesseract.image_to_string(img)
print(img)
SyntaxError: multiple statements found while compiling a single statement
>>> 

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# path 
path = r'C:\Users\user\Desktop\deneme.png'
  
# Using cv2.imread() method 
img = cv2.imread(path) 

text = pytesseract.image_to_string(img)
print(img)
