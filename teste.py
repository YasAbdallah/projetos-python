from rembg import remove
from PIL import Image

input_path = 'C:\\Users\\05916892195\\Pictures\\Sample Pictures\\download.jpg'
output_path = 'C:\\Users\\05916892195\\Pictures\\Sample Pictures\\download1-removed.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)