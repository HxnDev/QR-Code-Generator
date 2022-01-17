import pyqrcode # Install using "pip install pyqrcode"
import png  # Install using "pip install pypng"

s = input("Enter you website link = ")
url = pyqrcode.create(s)    # Generating QR Code
url.svg("myqr.svg", scale=8)    # Saving it in SVG Format
url.png('myqr.png', scale=6)    # Saving it in PNG Format
