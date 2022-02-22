import pyqrcode
import png
from pyqrcode import QRCode

txt = "ContactTracingForm.txt"
link = pyqrcode.create(txt)
link.png('grcodetracing.png', scale = 6)