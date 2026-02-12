#
# file: py-file-to-qrcode.py
#

# import libraries

import os
import sys
import qrcode
from PIL import Image
import argparse
import base64


def generate_qrcode(data, output_file, version=40, ec='H'):
    # Generate QR code image from data bytes
    qr = qrcode.QRCode(
        version = version,
        error_correction=getattr(qrcode.constants, f"ERROR_CORRECT_{ec}"),
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"Generated successfully '{output_file}'")



def split_chunks(text: str, max_size: int):
    return [text[i:i + max_size] for i in range(0, len(text), max_size)]



def mode_file_to_base64_qrcode():
    if (args.debug_level >= 1):
        print(f"DEBUG mode_file_to_base64_qrcode()")
    # read file, calculate hash, split chunks
    with open(args.input_file, 'rb') as f:
        content_bytes = f.read()

    chunks = split_chunks(content_bytes, args.max_chunk)
    total_chunks = len(chunks)
    # Generate index QRCode with metadata

    for idx, chunk in enumerate(chunks, start=1):
        # data = chunk
        encoded_chunk = base64.b64encode(chunk).decode('ascii')
        if (args.debug_level >= 2):
            print(f"DEBUG encoded_chunk: {encoded_chunk}")
        generate_qrcode(
            # data=data,
            data=encoded_chunk,
            output_file=f"{args.output_file}_{idx}.png",
            version=args.version,
            ec=args.ec
        )



def mode_base64_to_file():
    if (args.debug_level >= 1):
        print(f"DEBUG mode_base64_to_file()")


# main()

# parser arguments

parser = argparse.ArgumentParser(description="py-file-to-qrcode.py: Text file to QRCode")
parser.add_argument('input_file', help='Input file path. (ex: file.txt, file-base64-qrcode-1.png)')
parser.add_argument('output_file', help = 'Output file. (ex: file-base64-qrcode, file.txt)')
parser.add_argument('--mode', type=int, default=0, choices=[0, 1], help='Mode. (ex: 0=file to Base64/QRCode/image, 1=Base64/QRCode/image to file)')
parser.add_argument('--max-chunk', type=int, default=800, help='Max size per QRCode (bytes)')
parser.add_argument('--version', type=int, default=40, help='QR version(1-40)')
parser.add_argument('--ec', default='H', choices=['L', 'M', 'Q', 'H'], help='Error correction: L=7%% / M=15%% / Q=25%% / H=30%%')
parser.add_argument('--debug-level', type=int, default=0, choices=[0, 1, 2], help='Debug level. (ex: 0=nodebug, 1=topics, 2=full)')

args = parser.parse_args()


# check args validation

if not os.path.isfile(args.input_file):
    print(f"Error: input_file '{args.input_file}'does not exists")
    sys.exit(1)

# switch case mode:

if args.mode == 0:
    mode_file_to_base64_qrcode()
elif args.mode == 1:
    mode_base64_to_file()

