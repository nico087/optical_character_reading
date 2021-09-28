import pytesseract
from PIL import Image
import os


def convert_img_to_txt():

    for file in os.listdir('img'):
        if file.endswith((".png", ".PNG")):
            choose_image = Image.open(f"img/{file}")
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

            file_name = choose_image.filename
            file_name = file_name.split(".", 2)[0].split("/", 1)[1]

            custom_configurations = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(choose_image, config=custom_configurations)

            txt_folder_path = 'C:/Users/nijat/PycharmProjects/optical_character_reading/txt/'

            with open(f'{txt_folder_path}{file_name}.txt', 'w') as txt_file:
                txt_file.write(text)

        print("Converting Finished!")

    else:
        pass


def main():
    convert_img_to_txt()


if __name__ == "__main__":
    main()