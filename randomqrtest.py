import qrcode

# Data to encode in the QR code
data = "https://www.example.com"  # Replace this with any URL or text

# Generate the QR code
qr = qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)

# Print the QR code in ASCII
qr.print_ascii()

