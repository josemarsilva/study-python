#
# filename    : lab-137-opencv-cv2-nympy-imagematch.py
# Description : Find a subimage or partial image inside another large image
# Docs        :
#               * https://stackoverflow.com/questions/17566752/how-to-find-subimage-using-the-pil-library
#               * https://stackoverflow.com/questions/9084609/how-to-copy-a-image-region-using-opencv-in-python
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
image_partial_1_is_subimage = cv2.imread("screenshoot-05-partial-screen.png")
image_partial_2_is_subimage = cv2.imread("screenshoot-06-partial-screen.png")
image_partial_3_is_not_subimage = cv2.imread("screenshoot-07-partial-screen.png")

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
print('* image_partial_2_is_subimage     match image_full - result_2.shape(y,x): ', np.unravel_index(result_2.argmax(),result_1.shape))
print('* image_partial_3_is_not_subimage match image_full - result_3.shape(y,x): ', np.unravel_index(result_3.argmax(),result_1.shape))
print('* image_full                      match image_full - result_4.shape(y,x): ', np.unravel_index(result_4.argmax(),result_1.shape))
print('\nPS: Observe that results are zeroes in both situations: \n    a) partial is not subimage ; \n    b) partial and full are same images')

# print table results
print('\n\n3. Tabulation of matching results - method: cv2.TM_CCOEFF_NORMED\n')
print('                                | image_full')
print('--------------------------------+------------')
print('image_partial_1_is_subimage     |', result_1.shape[0], result_1.shape[1] )
print('image_partial_2_is_subimage     |', result_2.shape[0], result_2.shape[1] )
print('image_partial_3_is_not_subimage |', result_3.shape[0], result_3.shape[1] )
print('image_full                      |', result_4.shape[0], result_4.shape[1] )

