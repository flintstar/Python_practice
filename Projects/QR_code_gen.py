#importing required modules
import pyqrcode
import png

# Take input and convert it to a QR code
url = input("Insert your link: ")
qr_code = pyqrcode.create(url)
qr_code.png("link.png", scale=6)
# print(f"Please confirm the link entered:{url}")
qr_code.show()