# working
from PIL import Image
img = Image.open('me.jpg').convert('LA')
img.save('greyscale.png')