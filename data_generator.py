from PIL import Image, ImageDraw
import random
import sys
import os


PATH = "triangle_test"
IMAGE_SIZE = 416
SET_SIZE = 500 if len(sys.argv) == 1 else int(sys.argv[1])


def save_random_triangle(index, path):
    
    img = Image.new('RGB', (IMAGE_SIZE, IMAGE_SIZE), 'black')
    draw = ImageDraw.Draw(img)

    coords = []
    for i in range(6):
        coords.append(random.randint(2, IMAGE_SIZE-3))

    x = coords[0::2]
    y = coords[1::2]
    min_x, min_y, max_x, max_y = min(x)-1, min(y)-1, max(x)+1, max(y)+1
    x_center, y_center = (min_x + max_x) / 2, (min_y + max_y) / 2
    height, width = max_y - min_y, max_x - min_x
    
    with open('{}/{}.txt'.format(path, index), 'w+') as f:
        f.write('0 {} {} {} {}'.format(x_center/IMAGE_SIZE, y_center/IMAGE_SIZE, width/IMAGE_SIZE, height/IMAGE_SIZE))
    
    draw.polygon(coords, fill='white', outline='white')
    img.save('{}/{}.jpg'.format(path, index))

    with open('{}/train.txt'.format(path), 'a') as f:
        f.write('{}/{}.jpg\n'.format(path, index))


os.makedirs('{}'.format(PATH), exist_ok=True)

for i in range(SET_SIZE):
    save_random_triangle(i, PATH)


