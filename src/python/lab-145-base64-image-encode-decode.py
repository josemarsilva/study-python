#
# filename    : * [`lab-144-py3rijndael-aes-algorithm.py`](./src/python/lab-144-py3rijndael-aes-algorithm.py)
# Description : Base64 Encoding
# Docs        :
#               * https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
#               * https://stackoverflow.com/questions/50369637/how-to-base64-encode-an-image-using-python
# Requirements:
#               * 
#

# import
import base64

file_base64_image_original = 'file-20-base64-image-original.jpg'
file_base64_image_encoded  = 'file-21-base64-image-encoded.txt'
file_base64_image_decoded  = 'file-22-base64-image-decoded.jpg'

# encode
encoded_string = ""
with open(file_base64_image_original, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

with open(file_base64_image_encoded, "w") as image_file:
    image_file.write(encoded_string.decode('utf-8')) # utf-8 or ascii

#decode
decoded_string = ""
with open(file_base64_image_encoded, "r") as image_file:
    decoded_string = image_file.read()
decoded_bytes = base64.b64decode(decoded_string)
with open(file_base64_image_decoded, "wb") as image_file:
    image_file.write(decoded_bytes)

print(f'Python Base64 Encode/ Decode image file:')
print(f'  - file_base64_image_original: {file_base64_image_original}')
print(f'  - file_base64_image_encoded : {file_base64_image_encoded}')
print(f'  - file_base64_image_decoded : {file_base64_image_decoded}')



