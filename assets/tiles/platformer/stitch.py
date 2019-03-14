# You can use this Python script to stitch together your tiles
# into one tileset file

from PIL import Image
import sys
import os
import math

images = sys.argv[1:]

length = math.ceil(math.sqrt(len(images)))

tileset = Image.new('RGBA', (32 * length, 32 * length))

for i in len(images):
   image = Image.open(images[i])
   dx = im.size[0]
   dy = im.size[1]
   if dx != 32 or dy != 32:
      print('Image "' + image + '" was size (' + 
         str(dx) + ', ' + str(dy) + 
         '), and was not used in the tileset')
      continue
   x_tile = 32 * (i % length)
   y_tile = 32 * (i // length)
   for y in range(dy):
      for x in range(dx):
         tileset