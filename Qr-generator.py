import qrcode

# Function to generate a QR code
def generate_qr_code(data, filename="qrcode.png"):
    # Create a QR Code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Ensures that the QR code fits the data
    
    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

# Main function to take user input and generate the QR code
def main():
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")
    generate_qr_code(data, filename)

# Run the program
if __name__ == "__main__":
    main()

