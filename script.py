import argparse
import json
import random
from PIL import Image

def append_images(images,bg_color=(255,255,255), aligment='center'):

    widths, heights = zip(*(i.size for i in images))


    new_width = sum(widths)
    new_height = max(heights)


    new_im = Image.new('RGB', (new_width, new_height), color=bg_color)

    offset = 0
    for im in images:
        y = 0
        if aligment == 'center':
            y = int((new_height - im.size[1])/2)
        elif aligment == 'bottom':
            y = new_height - im.size[1]
        new_im.paste(im, (offset, y))
        offset += im.size[0]


    return new_im

def permutate(args):
    layers = []
    dst = None
    print(args.config)
    with open(args.config) as file:
        config = json.load(file)
        for layer in config['layers']:
            if random.random() <= layer['probability']:
                for option in layer['options']:
                    if random.random() <= option['probability']:
                        print(f"{layer['name']}/{option['type']}")
                        layers.append(f"layers/{layer['name']}/{option['type']}")

    images = map(Image.open,layers)
    combo_2 = append_images(images, aligment='center')
    combo_2.save('out/img.jpg')

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config', action='store', dest='config', type=str)
    args = parser.parse_args()
    permutate(args)
