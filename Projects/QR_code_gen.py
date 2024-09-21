
import pyqrcode
import png


url = input("Insert your link:   ")
qr_code = pyqrcode.create(url)
qr_code.png("link", scale=6)
# print(f"Please confirm the link entered:{url}")
qr_code.show()