import barcode
from barcode.writer import ImageWriter

# Function to generate and save barcode
def generate_barcode(data, filename):
    barcode_type = barcode.get_barcode_class('code128')  # Choose the barcode format
    barcode_obj = barcode_type(data, writer=ImageWriter())  # Create barcode object
    barcode_obj.save(filename)  # Save barcode image
    print(f"Barcode saved as {filename}.png")

# Example usage
data = "123456781332"  # Data to encode in the barcode
filename = "simple_barcode"  # Name of the output file
generate_barcode(data, filename)
