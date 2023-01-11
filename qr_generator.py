import argparse
import csv
import segno

def qr_generator(csv_file, delimit): 
    """
    Read an CSV file as an input
    and generate QR Code from those file.
    """
    with open(csv_file) as csvFile:
        # Read the CSV file and defined the delimiter
        csvReader = csv.reader(csvFile, delimiter=delimit)
        
        # Skip the header of CSV file
        next(csvReader)
        for line in csvReader:
            # Create a list from each columns of the CSV file
            col = list(line)
            # Choose which field to be created as QR Code
            # As example in the example.csv file there are 4 columns
            # Item ID, Book Title, Author, and Price
            # The Book Title, Author, and Price was chosen to generate QR Code
            qrcode = segno.make_qr(f'Title: {col[1]} \nAuthor: {col[2]} \nPrice: {col[3]}')
            qrcode.save(f'{col[0]}.png', scale=10)
            print(f'{col[0]}.png successfully created')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Batch QR Code Generator from CSV file")
    parser.add_argument("-i", "--input", help="CSV file to generate QR code")
    parser.add_argument("-d", "--delimiter", help="Special character as columns delimiter")
    
    args = parser.parse_args()
    csv_file = args.input
    delimit = args.delimiter
    
    if csv_file and delimit is not None:
        qr_generator(csv_file, delimit)
    else:
        print("Please choose an CSV file as an input and defined the delimiter")
