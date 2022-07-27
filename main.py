# Create any link into a qr-code ready image
#install dependencies
import pyqrcode

#insert link and create image - fill in with your own profile link
link = pyqrcode.create('https://linkedin.com/in/')
link.png('qrcode.png', scale= 8)
