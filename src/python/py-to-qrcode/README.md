# py-to-qrcode

`py-to-qrcode.py` is a command-line Python utility that converts the contents of a file into one or more QR Codes. It is useful for transferring files in environments where only images can be moved (air‑gapped systems, printed media, screenshots, etc.).

The script reads a binary file, calculates its MD5 hash for integrity verification, and generates QR Codes containing metadata and file data.

---

## Features

* Read any file in **binary mode**
* Generate **QR Codes (version 1–40)**
* Configurable **error correction level** (L, M, Q, H)
* Configurable **maximum data size per QR Code**
* Generate an **index QR Code** with metadata:

  * Original file name
  * Total number of chunks
  * MD5 checksum

---

## Requirements

* Python **3.8+**
* Required libraries:

```bash
pip install qrcode[pil] pillow
```

---

## Usage

```bash
python py-to-qrcode.py <input_file> <output_base_file> [options]
```

### Positional arguments

| Argument           | Description                              |
| ------------------ | ---------------------------------------- |
| `input_file`       | Path to the input file (e.g. `data.bin`) |
| `output_base_file` | Base name for output files (e.g. `data`) |

### Optional arguments

| Option        | Default | Description                                |
| ------------- | ------- | ------------------------------------------ |
| `--max-chunk` | `2000`  | Maximum number of bytes per QR Code        |
| `--version`   | `40`    | QR Code version (1–40)                     |
| `--ec`        | `H`     | Error correction level: `L`, `M`, `Q`, `H` |

---

## Example

```bash
python py-to-qrcode.py sample.txt sample_qr --max-chunk 1500 --version 40 --ec H
```

This will generate at least one QR Code:

* `sample_qr_index.png` → Metadata and integrity information

---

## Index QR Code Format

The index QR Code contains metadata in the following format:

```
FILE:<filename>|CHUNKS:<total_chunks>|MD5:<md5_hash>|START
```

Example:

```
FILE:sample.txt|CHUNKS:3|MD5:9e107d9d372bb6826bd81d3542a419d6|START
```

This allows a future decoder to:

* Validate file integrity
* Know how many QR Codes must be read
* Reconstruct the original file

---

## Notes & Limitations

* The script currently generates **only the index QR Code**. Chunked QR Code generation for file data can be extended.
* QR Codes with high error correction (`H`) reduce usable capacity per version.
* Very large files should use compression (e.g., gzip + base64) before encoding.

---

## Troubleshooting

* **"invalid version" errors** usually mean the data exceeds the capacity of the selected QR version and error correction level.
* Reduce `--max-chunk` or increase `--version`.

---

## Future Improvements

* Automatic chunk QR Code generation
* Optional gzip + base64 compression
* QR Code sequence numbering
* Decoder companion script

---

## License

This project is provided for educational and experimental purposes. Add a license if you plan to distribute it.
