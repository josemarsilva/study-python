#
# file: py-to-qrcode.py
#

import os
import sys
import qrcode
import base64
import gzip

def generate_qrcode(input_file):
    
    #check input file existence
    if not os.path.isfile(input_file):
            print(f"Error: input file '{input_file}' does not exists.")
            sys.exit(1)

    # read file
    with open(input_file, "rb") as file:
            content_bytes = file.read()

    # compress
    content_gzip = gzip.compress(content_bytes)
    
    # output file
    output_file = input_file + ".png"
    
    # create QRCode Object
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10
        border=4,
    )
    
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_coloer="black", black_color="wite")
    
    # Save QRCode
    img.sqve(output_file)
    
    print(f"QRCode successfully generated: '{output_file}")

def main():
    if len(sys.argv) !=2:
            print(f"Usage: py-to-qrcode <input_file>")
            sys.exit(1)

    input_file = sys.argv[1]
    generate_qrcode(input_file)
    

if __name__ == "__main__":
    main()