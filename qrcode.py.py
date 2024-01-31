
# QRCODE GENERATOR 


# Importing library
import qrcode as qr
from PIL import Image 
 
# Data to be encoded
data = 'Hi,You are in ANBHI github page...'
 
# Encoding data using make() function
img = qr.make(data)
 
# # Creating an instance of QRCode class
qr = qr.QRCode(version = 1,
                error_correction= qr.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 5) 
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'white',
                    back_color = 'purple')
 
# Saving as an image file 
img.save('QRCODE.png') 
