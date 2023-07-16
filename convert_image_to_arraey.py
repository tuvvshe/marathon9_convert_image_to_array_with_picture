from PIL import Image
image = Image.open('pngimage.png')

from numpy import asarray
data = asarray(image)
print(data)
