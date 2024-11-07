import qrcode as qr
img = qr.make("https://www.youtube.com/@codewithvijay07")
img.save("codewithvijay07_youtube.png")