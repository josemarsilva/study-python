# py-file-to-qrcode

`py-file-to-qrcode.py` is a command-line Python utility that converts the contents of a file into one or more QR Codes. It is useful for transferring files in environments where only images can be moved (air‑gapped systems, printed media, screenshots, etc.).

The script reads a binary file, calculates its MD5 hash for integrity verification, and generates QR Codes containing metadata and file data.

---

## Features

* Read any file any format
* Converts Base64 and split in pieces
* Generate **QR Codes (version 1–40)** splited in pieces
* Generate an **index QR Code** with metadata


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
python py-file-to-qrcode.py <input_file> <output_base_file> [options]
```

### Positional arguments

| Argument           | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `input_file`       | Path to the input file (e.g. `file.txt`)               |
| `output_base_file` | Base name for output files (e.g. `file-base64-qrcode`) |

### Optional arguments

| Option         | Default | Description                                     |
| -------------- | ------- | ----------------------------------------------- |
| `--mode`       |  `0`    | `0`: To QRCode splited pieces; `1`: from Base64 |
| `--max-chunk`  | `2000`  | Maximum number of bytes per QR Code             |
| `--version`    | `40`    | QR Code version (1–40)                          |
| `--ec`         | `H`     | Error correction level: `L`, `M`, `Q`, `H`      |
| `--debug-level | `0`     | `0`: nodebug, `1`: topics, `2`: all             |

---

## Examples

* Example no. 1: mode=0 is convert File-To-Base64QRCode
  * Read text or binary file `sample.txt`
  * Converts file to Base64 and Split in chunks to Convert to QRCode Image (.png)
  * Write output image files `sample_qrcode_base64_1.png` .. `sample_qrcode_base64_<n>>.png`

```bash
# converts any file to a Base64 + QRCode 
python py-file-to-qrcode.py sample.txt sample_qrcode_base64 --mode=0 --debug-level=1
```



---

## Notes & Limitations

* Parameter mode is used to convert File-to-Base64QRCode or Base64QRCode-to-File
* QR Codes with high error correction (`H`) reduce usable capacity per version.
* Very large files should use compression (e.g., gzip + base64) before encoding.

---

## Troubleshooting

* **"invalid version" errors** usually mean the data exceeds the capacity of the selected QR version and error correction level.
* Reduce `--max-chunk` or increase `--version`.

---

## Future Improvements

* Automatic base64 compression + chunk pieces + QR Code generation basefilename-piece.png
* QR Code sequence numbering

---

## License

This project is provided for educational and experimental purposes. Add a license if you plan to distribute it.
