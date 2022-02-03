#
# filename    : lab-144-py3rijndael-aes-algorithm.py
# Description : Rijndael algorithm library for Python3
# Docs        :
#               * https://pypi.org/project/py3rijndael/
#               * https://github.com/meyt/py3rijndael/blob/master/py3rijndael/tests/test_rijndael_cbc.py
#				* https://stackoverflow.com/questions/63737685/how-to-do-mcrypt-rijndael-256-mcrypt-mode-cbc-in-python3
# Requirements:
#               * pip install py3rijndael
#

# import
from py3rijndael import RijndaelCbc, ZeroPadding
import base64

# setup
data_text = 'secret data'
block_size = 32

# use case #1: encrypt/decrypt - Key and InitVector as string blocksize 32
data_bytes = data_text.encode('utf-8')
key_value_1_32_bytes_string_ascii_utf8 = 'abcdefghijklmnopqrstuvwxyz123456' # must be: len(key) == 32 == block_size
key_1 = key_value_1_32_bytes_string_ascii_utf8.encode('utf-8')
iv_value_1_32_bytes_string_ascii_utf8 = 'abcdefghijklmnopqrstuvwxyz123456'  # must be: len(key) == 32 == block_size
iv_1 = iv_value_1_32_bytes_string_ascii_utf8.encode('utf-8')
# encrypt
if len(key_1) != block_size or len(iv_1) != block_size:
    raise Exception(f"key '{key_1}' and initial value '{iv_1}' must be {block_size} length")
rijndaelCbc_encrypt_1 = RijndaelCbc( key = key_1, iv = iv_1, padding = ZeroPadding(block_size), block_size = block_size )
ciphertext_encrypt_1 = rijndaelCbc_encrypt_1.encrypt(data_bytes)
data_encrypted_base64_1 = base64.b64encode(ciphertext_encrypt_1) # .decode('utf8')
# decrypt
rijndaelCbc_decrypt_1 = RijndaelCbc( key = key_1, iv = iv_1, padding = ZeroPadding(block_size), block_size = block_size )
data_bytes_decrypted_1 = rijndaelCbc_decrypt_1.decrypt(base64.b64decode(data_encrypted_base64_1))

# use case #2: encrypt/decrypt - Key and InitVector as byte-array blocksize 32
key_value_2_32_bytes_array_ascii_ord_numbers = chr(97) + chr(98) + chr(99) + chr(100) + chr(101) + chr(102) + chr(103) + chr(104) + chr(105) + chr(106) + chr(107) + chr(108) + chr(109) + chr(110) + chr(111) + chr(112) + chr(113) + chr(114) + chr(115) + chr(116) + chr(117) + chr(118) + chr(119) + chr(120) + chr(121) + chr(122) + chr(65) + chr(66) + chr(67) + chr(68) + chr(69) + chr(70)
key_2 = key_value_2_32_bytes_array_ascii_ord_numbers.encode('utf-8')
iv_value_2_32_bytes_string_ascii_utf8 = chr(70)+chr(69)+chr(68)+chr(67)+chr(66)+chr(65)+chr(122)+chr(121)+chr(120)+chr(119)+chr(118)+chr(117)+chr(116)+chr(115)+chr(114)+chr(113)+chr(112)+chr(111)+chr(110)+chr(109)+chr(108)+chr(107)+chr(106)+chr(105)+chr(104)+chr(103)+chr(102)+chr(101)+chr(100)+chr(99)+chr(98)+chr(97) # must be: len(key) == 32
iv_2 = iv_value_2_32_bytes_string_ascii_utf8.encode('utf-8')
# encrypt
if len(key_2) != block_size or len(iv_2) != block_size:
    raise Exception(f"key '{key_2}' and initial value '{iv_2}' must be {block_size} length")
rijndaelCbc_encrypt_2 = RijndaelCbc( key = key_2, iv = iv_2, padding = ZeroPadding(block_size), block_size = block_size )
ciphertext_encrypt_2 = rijndaelCbc_encrypt_2.encrypt(data_bytes)
data_encrypted_base64_2 = base64.b64encode(ciphertext_encrypt_2) # .decode('utf8')
# decrypt
rijndaelCbc_decrypt_2 = RijndaelCbc( key = key_2, iv = iv_2, padding = ZeroPadding(block_size), block_size = block_size )
data_bytes_decrypted_2 = rijndaelCbc_decrypt_2.decrypt(base64.b64decode(data_encrypted_base64_2))


print(f"Rijndael algorithm:")
print(f"  - data_text                : {data_text}")

print(f"")
print(f"  + use case #1: encrypt/decrypt - Key and InitVector as string blocksize 32")
print(f"    - data_bytes             : {data_bytes}")
print(f"    - key_1                  : {key_1}")
print(f"    - iv_1                   : {iv_1}")
print(f"    - ciphertext_encrypt_1   : {ciphertext_encrypt_1}")
print(f"    - data_encrypted_base64_1: {data_encrypted_base64_1}")
print(f"    - data_bytes_decrypted_1 : {data_bytes_decrypted_1}")
print(f"    - data_text_decrypted_1  : {data_bytes_decrypted_1.decode('utf-8')}")

print(f"")
print(f"  + use case #2: encrypt/decrypt - Key and InitVector as string blocksize 32")
print(f"    - data_bytes             : {data_bytes}")
print(f"    - key_2                  : {key_2}")
print(f"    - iv_2                   : {iv_2}")
print(f"    - ciphertext_encrypt_2   : {ciphertext_encrypt_2}")
print(f"    - data_encrypted_base64_2: {data_encrypted_base64_2}")
print(f"    - data_bytes_decrypted_2 : {data_bytes_decrypted_2}")
print(f"    - data_text_decrypted_2  : {data_bytes_decrypted_2.decode('utf-8')}")

