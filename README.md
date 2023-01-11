# Simple-Batch-QR-Code-Generator
Simple batch QR code generator from CSV file using Python

## Requirements
Install segno module to use as QR code generator
``` shell
# Install segno module using pip
pip install segno
```

## Testing
In this repository there is example.csv as an example that can be used to generate QR codes
Make sure that the `qr_generator.py` and the CSV are in one fodler
Run the program
``` shell
python qr_generator.py -i "example.csv" -d ";"
```
The `-i` or `--input` argument is used to specify the CSV file
The `-d` or `--delimiter` argument is used to specify the special character that was used as tab delimiter

