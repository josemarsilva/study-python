#
# filename    : lab-142-pycryptodome-cryptographic-primitives.py
# Description : PyCryptoDome 
# Docs        :
#               * https://pypi.org/project/pycryptodome/
#				* https://pycryptodome.readthedocs.io/en/latest/src/examples.html
#				* https://www.pycryptodome.org/en/latest/src/examples.html#encrypt-data-with-aes
# Requirements:
#               * pip install pycryptodome
#

# import
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# setup
data = b'secret data'

# use case #1: encode/decode - random 16 bytes AES.MODE_EAX
key_1 = get_random_bytes(16) # must be: len(key) == 16
cipher_encoder_1 = AES.new(key_1, AES.MODE_EAX)
nonce_encoder_1 = cipher_encoder_1.nonce
# encode: (ciphertext, tag) = ciphertext = (data, key, nonce)
ciphertext_1, tag_1 = cipher_encoder_1.encrypt_and_digest(data)
# decode:  data = (ciphertext, key, nonce)
cipher_decoder_1 = AES.new(key_1, AES.MODE_EAX, nonce_encoder_1)
data_decoded_1 = cipher_decoder_1.decrypt(ciphertext_1)
cipher_verify_1 = ''
try:
	cipher_decoder_1.verify(tag_1)
	cipher_verify_1 = 'OK'
except ValueError:
	cipher_verify_1 = 'VALUE-ERROR'


# use case #2: encode/decode - predefined string[16] bytes AES.MODE_EAX
key_16_predefined_ascii_utf8_chars = 'abcdefghijklmnop'  # must be: len(key) == 16
key_2 = key_16_predefined_ascii_utf8_chars.encode('utf-8')
cipher_encoder_2 = AES.new(key_2, AES.MODE_EAX)
nonce_encoder_2 = cipher_encoder_2.nonce
# encode: (ciphertext, tag) = ciphertext = (data, key, nonce)
ciphertext_2, tag_2 = cipher_encoder_2.encrypt_and_digest(data)
# decode:  data = (ciphertext, key, nonce)
cipher_decoder_2 = AES.new(key_2, AES.MODE_EAX, nonce_encoder_2)
data_decoded_2 = cipher_decoder_2.decrypt(ciphertext_2)
cipher_verify_2 = ''
try:
	cipher_decoder_2.verify(tag_2)
	cipher_verify_2 = 'OK'
except ValueError:
	cipher_verify_2 = 'VALUE-ERROR'


# use case #3: encode/decode - predefined byte array[n] bytes AES.MODE_EAX
key_16_predefined_ascii_ord_numbers = [97, 97+1, 97+2, 97+3, 97+4, 97+5, 97+6, 97+7, 97+8, 97+9, 97+10, 97+11, 97+12, 97+13, 97+14, 97+15] # 'abcde'
key_16_predefined_byte_array = ''
for c in key_16_predefined_ascii_ord_numbers:
	key_16_predefined_byte_array = key_16_predefined_byte_array + chr(c)
key_3 = key_16_predefined_byte_array.encode('utf-8')
cipher_encoder_3 = AES.new(key_3, AES.MODE_EAX)
nonce_encoder_3 = cipher_encoder_3.nonce
cipher_encoder_3 = AES.new(key_3, AES.MODE_EAX)
nonce_encoder_3 = cipher_encoder_3.nonce
# encode: (ciphertext, tag) = ciphertext = (data, key, nonce)
ciphertext_3, tag_3 = cipher_encoder_3.encrypt_and_digest(data)
# decode:  data = (ciphertext, key, nonce)
cipher_decoder_3 = AES.new(key_3, AES.MODE_EAX, nonce_encoder_3)
data_decoded_3 = cipher_decoder_3.decrypt(ciphertext_3)
cipher_verify_3 = ''
try:
	cipher_decoder_3.verify(tag_3)
	cipher_verify_3 = 'OK'
except ValueError:
	cipher_verify_3 = 'VALUE-ERROR'


# 
print(f"PycryptoDome Cryptographic Primitives:")
print(f"  - data              : {data}")

print(f"")
print(f"  + use case #1: encode/decode - random 16 bytes AES.MODE_EAX")
print(f"    - key_1           : {key_1}")
print(f"    - tag_1           : {tag_1}")
print(f"    - nonce_encoder_1 : {nonce_encoder_1}")
print(f"    - ciphertext_1    : {ciphertext_1}")
print(f"    - data_decoded_1  : {data_decoded_1}")
print(f"    - cipher_verify_1  : {cipher_verify_1}")

print(f"")
print(f"  + use case #2: encode/decode - predefined string[16] bytes AES.MODE_EAX")
print(f"    - key_2           : {key_2}")
print(f"    - tag_2           : {tag_2}")
print(f"    - nonce_encoder_2 : {nonce_encoder_2}")
print(f"    - ciphertext_2    : {ciphertext_2}")
print(f"    - data_decoded_2  : {data_decoded_2}")
print(f"    - cipher_verify_2  : {cipher_verify_2}")
print(f"")

print(f"")
print(f"  + use case #3: encode/decode - predefined string[16] bytes AES.MODE_EAX")
print(f"    - key_3           : {key_3}")
print(f"    - tag_3           : {tag_3}")
print(f"    - nonce_encoder_3 : {nonce_encoder_3}")
print(f"    - ciphertext_3    : {ciphertext_3}")
print(f"    - data_decoded_3  : {data_decoded_3}")
print(f"    - cipher_verify_3  : {cipher_verify_3}")
print(f"")
