#
# filename    : lab-141-jwt-encode-decode.py
# Description : JWT Encode Decode
# Docs        :
#               * https://pypi.org/project/jwt/
#               * https://pyjwt.readthedocs.io/en/stable/
# Requirements:
#               * pip install pyjwt
#

import jwt
#
dict_jwt_original_keys_values = {"hello": "world", "par": "impar", "cpf": "123.456.789-01", "cnpj": "12.345.678/0001-23" }
str_jwt_secret = "secret"
str_jwt_algorithm = "HS256"
print(f"Parameters:")
print(f"- dict_jwt_original_keys_values: {dict_jwt_original_keys_values}")
print(f"- str_jwt_secret               : {str_jwt_secret}")
print(f"- str_jwt_algorithm            : {str_jwt_algorithm}")
print(f"")

# Encode
encoded_jwt = jwt.encode(dict_jwt_original_keys_values, str_jwt_secret, algorithm=str_jwt_algorithm)
print(f"Invoke and Result of Encode:")
print(f"- invoke     : jwt.encode(dict_original_keys_values, str_jwt_secret, algorithm=str_jwt_algorithm)")
print(f"- result     : {encoded_jwt}")
print(f"")

# Decode
decoded_jwt = jwt.decode(encoded_jwt, str_jwt_secret, algorithms=["HS256"])
print(f"Invoke and Result of Decode:")
print(f"- invoke     : decoded_jwt = jwt.decode(encoded_jwt, str_jwt_secret, algorithms=['HS256'])")
print(f"- result     : {decoded_jwt}")
print(f"")

