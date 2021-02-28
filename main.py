from PIL import Image
import math

def are_equal(pix_a, pix_b, threshold):
    #if pix_a[x, y] == pix_b[x, y]:
    #    return True 
    if abs(pix_a[0] - pix_b[0]) < threshold and abs(pix_a[1] - pix_b[1]) < threshold and abs(pix_a[2] - pix_b[2]) < threshold:
        return True
    return False

im_a = Image.open('goog90.jpg')
pix_a = im_a.load()

im_b = Image.open('goog60.jpg')
pix_b = im_b.load()

width, height = im_a.size

im_out = Image.new('RGB', (width, height))
pix_out = im_out.load()

for x in range(width):
    for y in range(height):
        if are_equal(pix_a[x,y], pix_b[x,y], 10):
            pix_out[x, y] = pix_a[x, y]
        else:
            pix_out[x,y] = (255,0,255)

im_out.save('output.png')
