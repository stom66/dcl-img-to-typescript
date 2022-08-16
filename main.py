#!/usr/bin/python

import numpy
from PIL import Image

# Specify your input image
image_path = "input.png"



# Function to read the pixel values from an image
def get_image(image_path):
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "RGBA":
        channels = 4
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((height, width, channels))
    return pixel_values


image = get_image(image_path)

# Print some basic info to the console
print("Image dimensions: ")
print("  Rows: " + str(len(image)))
print("  Cols: " + str(len(image[0])))


## create and open the output file
f = open("output.ts", "w")

# Set a blank count for some basic stats
count = 0

for row, cols in enumerate(image):
    rownum = "// Row " + str(row)
    #print(rownum)
    f.write(rownum+"\r\n")
    for col, c in enumerate(cols):
        #print("//   ["+str(col)+","+str(row)+"] ("+str(c)+")")
        if c[3] > 0.5:
            count +=1
            line = "{ position: new Vector3(brickOffsetX + brickSize * " + str(col+1) + ", GameManager.PLANE_HEIGHT, brickOffsetZ - brickSize * " + str(row-1) + "), color: Color3.FromInts(" + str(c[0]) + ", " + str(c[1]) + ", " + str(c[2]) + ") },"
            f.write(line+"\r\n")
            #print(line)

f.close()
print("Total pixels: "+str(count)+"/"+str(len(image) * len(image[0])))
