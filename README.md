# Simple-Batch-QR-Code-Generator
Simple batch QR code generator from CSV file using Python

## Requirements
Install segno module to be used as QR code generator
``` shell
# Install segno module using pip
pip install segno
```

## Testing
In this repository there is `example.csv` as an example that can be used to generate QR codes <br>
Make sure that the `qr_generator.py` and the CSV file are in one folder <br>
* Run the program
``` shell
python qr_generator.py -i "example.csv" -d ";"
```
The `-i` or `--input` argument is used to specify the CSV file <br>
The `-d` or `--delimiter` argument is used to specify the special character that was used as tab delimiter

