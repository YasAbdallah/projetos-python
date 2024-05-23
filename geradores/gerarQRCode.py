import qrcode
img = qrcode.make('Colocar qualque coisa aqui.')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")   