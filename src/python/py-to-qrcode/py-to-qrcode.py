#
# file: py-to-qrcode.py
#

# import libraries

import os
import sys
import qrcode
from PIL import Image
import argparse
import hashlib
import math
import base64


# generate_qrcode()

def generate_qrcode(data, output_name, version=40, ec='H'):
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
    img.save(output_name)
    print(f"Generated successfully '{output_name}'")


# split_chunks()

def split_chunks(text: str, max_size: int):
    return [text[i:i + max_size] for i in range(0, len(text), max_size)]



# file_md5()

def file_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



def normalize_content(text: str) -> str:
    normalized = []
    for ch in text:
        code = ord(ch)
        # Tab real → \t
        if ch == '\t':
            normalized.append('\\t')
        # CR ou LF → \n
        elif ch == '\r' or ch == '\n':
            normalized.append('\\n')
        # Qualquer caractere fora do UTF-7 (ASCII)
        elif code > 127:
            normalized.append('?')
        # ASCII válido
        else:
            normalized.append(ch)

    return ''.join(normalized)


# main()

# parser arguments

parser = argparse.ArgumentParser(description="py-to-qrcode.py: Text file to QRCode")
parser.add_argument('input_file', help='Input file path. (ex: file.txt)')
parser.add_argument('output_base_file', help = 'Output base file name. (ex: file)')
parser.add_argument('--max-chunk', type=int, default=1000, help='Max size per QRCode (bytes)')
parser.add_argument('--version', type=int, default=40, help='QR version(1-40)')
parser.add_argument('--ec', default='H', choices=['L', 'M', 'Q', 'H'], help='Error correction: L=7%% / M=15%% / Q=25%% / H=30%%')

args = parser.parse_args()


# check args validation

if not os.path.isfile(args.input_file):
    print(f"Error: input_file '{input_file}'does not exists")
    sys.exit(1)


# read file, calculate hash, split chunks

with open(args.input_file, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
#content = normalize_content(content)
file_hash = hashlib.md5(content.encode("utf-8")).hexdigest()
chunks = split_chunks(content, args.max_chunk)
total_chunks = len(chunks)

print(f"DEBUG file_hash: {file_hash}")

# Generate index QRCode with metadata
for idx, chunk in enumerate(chunks, start=1):
    data = chunk
    print(f"DEBUG data: {data}")
    
    generate_qrcode(
        data=data,
        output_name=f"{args.output_base_file}_{idx}.png",
        version=args.version,
        ec=args.ec
    )
