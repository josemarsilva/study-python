#
# filename    : lab-138-tesseract-ocr.py
# Description : Read full image, read top-left image mark, read botton-rigth mark, crop image and
#               transform image into test
# Docs        :
#               * https://pypi.org/project/pytesseract/
#               * https://www.youtube.com/watch?v=DG5D8A3zi4o
#               * https://stackoverflow.com/questions/68401654/using-tesseract-ocr-in-python-to-get-number-from-images
# Requirements:
#				* pip install matplotlib
#				* pip install numpy
#               * pip install opencv-python
#               * INSTALL Tesseract
#                   + Pre-requisites
#                       * pip install pillow
#                   + Python Package Libraries
#                       * pip install pytesseract
#                   + Download and run Tesseract installer executable for your OS Windows
#                       - https://github.com/UB-Mannheim/tesseract/wiki
#                       - tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe (64 bit)
#                       - Destination path: C:\Program Files\Tesseract-OCR
#                       - Path for executable: "C:\Program Files\Tesseract-OCR\tesseract.exe"

import cv2
import numpy as np
import pytesseract as tess

def crop_image_rectangle(image_full, image_top_left, image_botton_right):
    method = cv2.TM_CCOEFF_NORMED
    match_template_top_left = cv2.matchTemplate(image_full, image_top_left, method)
    match_template_botton_right = cv2.matchTemplate(image_full, image_botton_right, method)
    # Debug
    print(f'image_full.shape                    : {image_full.shape}')
    print(f'image_top_left.shape                : {image_top_left.shape}')
    print(f'image_botton_right.shape            : {image_botton_right.shape}')
    print(f'match_template_top_left.argmax()    : {match_template_top_left.argmax()}')
    print(f'match_template_top_left.shape       : {match_template_top_left.shape}')
    print(f'match_template_botton_right.argmax(): {match_template_botton_right.argmax()}')
    print(f'match_template_botton_right.shape   : {match_template_botton_right.shape}')
    # image crop success?
    if match_template_top_left.argmax()==0 or match_template_botton_right.argmax()==0:
        return None
    # return crop image ...
    x1 = np.unravel_index(match_template_top_left.argmax(),match_template_top_left.shape)[1]
    y1 = np.unravel_index(match_template_top_left.argmax(), match_template_top_left.shape)[0] + image_top_left.shape[0]
    x2 = x1 + image_botton_right.shape[1]
    y2 = np.unravel_index(match_template_botton_right.argmax(),match_template_botton_right.shape)[0]
    image_crop_top_left_botton_right = image_full[y1:y2, x1:x2]
    return image_crop_top_left_botton_right


# __main__

image_full = cv2.imread("screenshoot-04-full-screen.png")  
image_top_left = cv2.imread('screenshoot-05-partial-screen.png')
image_botton_rigth = cv2.imread('screenshoot-06-partial-screen.png')
image_cropped = crop_image_rectangle(image_full, image_top_left, image_botton_rigth)

if image_cropped is not None:
    cv2.imshow('image_cropped', image_cropped)
    cv2.waitKey(0)
else:
    print(f'Sorry image_cropped is None')
    exit(0)

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe';
text = tess.image_to_string(image_cropped)
print('\nTesseract - image_to_string(image_cropped):\n')
print(text)
