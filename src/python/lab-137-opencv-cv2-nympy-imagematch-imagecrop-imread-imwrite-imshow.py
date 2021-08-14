#
# filename    : lab-137-opencv-cv2-nympy-imagematch.py
# Description : Find a subimage or partial image inside another large image
# Docs        :
#               * https://stackoverflow.com/questions/17566752/how-to-find-subimage-using-the-pil-library
#               * https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
# Requirements:
#				* pip install matplotlib
#				* pip install numpy
#               * pip install opencv-python
#

import cv2
import numpy as np

# large image printscreen
image_full = cv2.imread("screenshoot-04-full-screen.png")  

# partial image - to check if is inside large image
image_partial_1_is_subimage = cv2.imread('screenshoot-05-partial-screen.png')
image_partial_2_is_subimage = cv2.imread('screenshoot-06-partial-screen.png')
image_partial_3_is_not_subimage = cv2.imread('screenshoot-07-not-a-partial-screen.png')

# print shape of images - heigth, width, channes
print('\n\n1. Images shape\n')
print(f'* image_full.shape                     : {image_full.shape}')
print(f'* image_partial_1_is_subimage.shape    : {image_partial_1_is_subimage.shape}')
print(f'* image_partial_2_is_subimage.shape    : {image_partial_2_is_subimage.shape}')
print(f'* image_partial_3_is_not_subimage.shape: {image_partial_3_is_not_subimage.shape}')

# evaluate result partial images inside large image - using differents methods
method = cv2.TM_CCOEFF_NORMED
result_1 = cv2.matchTemplate(image_full, image_partial_1_is_subimage, method)
result_2 = cv2.matchTemplate(image_full, image_partial_2_is_subimage, method)
result_3 = cv2.matchTemplate(image_full, image_partial_3_is_not_subimage, method)
result_4 = cv2.matchTemplate(image_full, image_full, method)

# print result
print('\n\n2. Matching results - method: cv2.TM_CCOEFF_NORMED\n')
print('* image_partial_1_is_subimage     match image_full - result_1.shape(y,x): ', np.unravel_index(result_1.argmax(),result_1.shape))
print('* image_partial_2_is_subimage     match image_full - result_2.shape(y,x): ', np.unravel_index(result_2.argmax(),result_2.shape))
print('* image_partial_3_is_not_subimage match image_full - result_3.shape(y,x): ', np.unravel_index(result_3.argmax(),result_3.shape))
print('* image_full                      match image_full - result_4.shape(y,x): ', np.unravel_index(result_4.argmax(),result_4.shape))
print('\nPS: Observe that results are zeroes in both situations: \n    a) partial is not subimage ; \n    b) partial and full are same images')

# print table results
print('\n\n3. Crop and copy a portion of full image\n')
print('+-------------------------------------------------------------+')
print('|    (x1, y1)                                                 |')
print('|    [ +----------------------+ ] image_partial_1_is_subimage |')
print('|      |                      |                               |')
print('|      |         ROI          |                               |')
print('|      |                      |                               |')
print('|    [ +----------------------+ ] image_partial_2_is_subimage |')
print('|                           (x2, y2)                          |')
print('+-------------------------------------------------------------+')
print('')
x1 = np.unravel_index(result_1.argmax(),result_1.shape)[1]
y1 = np.unravel_index(result_1.argmax(),result_1.shape)[0] + image_partial_1_is_subimage.shape[0]
x2 = x1 + image_partial_2_is_subimage.shape[1]
y2 = np.unravel_index(result_2.argmax(),result_2.shape)[0]
print(f'x1 = cv2.matchTemplate(image_full, image_partial_1_is_subimage).(x) = {x1}')
print(f'y1 = cv2.matchTemplate(image_full, image_partial_1_is_subimage).(y) + image_partial_1_is_subimage.shape.(y) = {np.unravel_index(result_1.argmax(),result_1.shape)[0]} + {image_partial_1_is_subimage.shape[0]} = {y1}')
print(f'x2 = x1 + image_partial_2_is_subimage.shape(x) = {x1} + {image_partial_2_is_subimage.shape[1]} = {x2}')
print(f'y2 = cv2.matchTemplate(image_full, image_partial_2_is_subimage).(y) = {y2}')

image_cropped = image_full[y1:y2, x1:x2]
cv2.imwrite('screenshoot-08-cropped.png', image_cropped)


# Show images
print('\n\n4. Show images\n')

print('* screenshoot-04-full-screen.png')
#cv2.imshow('screenshoot-04-full-screen.png', image_full)
#cv2.waitKey(0)

print('* screenshoot-05-partial-screen.png')
#cv2.imshow('screenshoot-05-partial-screen.png', image_partial_1_is_subimage)
#cv2.waitKey(0)

print('* screenshoot-06-partial-screen.png')
#cv2.imshow('screenshoot-06-partial-screen.png', image_partial_1_is_subimage)
#cv2.waitKey(0)

print('* screenshoot-08-cropped.png')
#cv2.imshow("screenshoot-08-cropped.png", image_cropped)
#cv2.waitKey(0)
