#
# filename    : lab-143-base64-encoding.py
# Description : Base64 Encoding
# Docs        :
#               * https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# Requirements:
#               * 
#

# import
import base64

# encode
message = "Python is fun"                               #  'Python is fun'
message_bytes = message.encode('ascii')                 # b'Python is fun'
base64_bytes = base64.b64encode(message_bytes)          # b'UHl0aG9uIGlzIGZ1bg=='
base64_message = base64_bytes.decode('ascii')           #  'UHl0aG9uIGlzIGZ1bg=='
#decode
message_bytes = base64.b64decode(base64_bytes)          # b'Python is fun'
message_base64_decoded = message_bytes.decode('ascii')  #  'Python is fun'

print(f'Python Base64 Encoding:')
print(f'  - message(original)      : {message}')
print(f'  - message(base64 encoded): {base64_message}')
print(f'  - message(base64 decoded): {message_base64_decoded}')


