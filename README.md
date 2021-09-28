# optical_character_reading
A freelance project, reading phone numbers from images (OCR)

Customer has a request to convert phone numbers from russian public ads website. Below you can find one sample link. He had already collected images from the websites and needed script for converting phone numbers from image files to text files. 

SAMPLE: https://www.avito.ru/skovorodino/avtomobili/mazda_6_mps_2006_2217076575

There are two folders named by: txt, img. Images has been placed in img folder. At the end converting, all data will be saved in txt folder with the same name as image file.

Need to install / Libraries:
- pytesserract
- pillow

Download tesseract and install:
https://tesseract-ocr.github.io/tessdoc/

Windows users:
Has to show the path to tesseract.exe file. In my code "main.py" you will see it.
