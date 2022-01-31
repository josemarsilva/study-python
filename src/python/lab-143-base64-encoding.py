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
message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
#decode
message_bytes = base64.b64decode(base64_bytes)
message_base64_decoded = message_bytes.decode('ascii')

print(f'Python Base64 Encoding:')
print(f'  - message(original)      : {message}')
print(f'  - message(base64 encoded): {base64_message}')
print(f'  - message(base64 decoded): {message_base64_decoded}')


