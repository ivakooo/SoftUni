import pyqrcode
import png
from pyqrcode import QRCode

address = "https://www.facebook.com/GeorgiYordanovGhostRider/"
url = pyqrcode.create(address)
url.png("Georgi_Yordanov.png", scale=8)
