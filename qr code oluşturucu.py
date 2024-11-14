pip install qrcode



import qrcode

data = "" //link
img = qrcode.make(data)

img.save("qr_code.png")