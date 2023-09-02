import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data =" https://www.thestatesman.com"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test.png")

data1 ="https://github.com/kennyz23"

qr.add_data(data1)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test1.png")

data2 ="www.youtube.com"

qr.add_data(data2)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
img.save("test2.png")

