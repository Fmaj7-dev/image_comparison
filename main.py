from PIL import Image

im_a = Image.open('goog90.jpg')
pix_a = im_a.load()

im_b = Image.open('goog60.jpg')
pix_b = im_b.load()

width, height = im_a.size

im_out = Image.new('RGB', (width, height))
pix_out = im_out.load()

for x in range(width):
    for y in range(height):
        if pix_a[x, y][0] == pix_b[x, y][0] and pix_a[x, y][1] == pix_b[x, y][1] and pix_a[x, y][2] == pix_b[x, y][2]:
            pix_out[x, y] = pix_a[x, y]
        else:
            pix_out[x,y] = (255,0,255)

im_out.save('output.png')
