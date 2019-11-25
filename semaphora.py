#!/usr/bin/env python3

import svgutils
import argparse

# 3 4 5
# 2 X 6
# 1 0 7

symbols = {
    'A': (0, 1), 'B': (0, 2), 'C': (0, 3), 'D': (0, 4), 'E': (0, 5), 'F': (0, 6),
    'G': (0, 7), 'H': (1, 2), 'I': (1, 3), 'J': (4, 6), 'K': (1, 4), 'L': (1, 5),
    'M': (1, 6), 'N': (1, 7), 'O': (2, 3), 'P': (2, 4), 'Q': (2, 5), 'R': (2, 6),
    'S': (2, 7), 'T': (3, 4), 'U': (3, 5), 'V': (4, 7), 'W': (5, 6), 'X': (5, 7),
    'Y': (3, 6), 'Z': (7, 6), '#': (4, 5), '1': (0, 1), '2': (0, 2), '3': (0, 3),
    '4': (0, 4), '5': (0, 5), '6': (0, 6), '7': (0, 7), '8': (1, 2), '9': (1, 3),
    '0': (1, 4), ' ': (0, 0)  # Remove space?
}

parser = argparse.ArgumentParser(description='Generate semaphore images')

# This library is so fiddley... no. It's an svg. Do it yourself.
# parser.add_argument('--scale', type=float, help='Scale factor')

# svgutils can't and svgmanip is both broken and requires Node to do so
# parser.add_argument('--render', type=float, help='Render to PNG')

parser.add_argument('text', type=str, help='Text to convert')

args = vars(parser.parse_args())

text = args['text'].upper()
# I could regex but I could also not
bad_chars = set(x for x in text if x not in symbols)
if bad_chars:
    # ...and I wrote the regex anyway
    raise RuntimeError('Invalid characters, [A-Z0-9 ]+ only: {}'.format(bad_chars))

ring = svgutils.transform.fromfile('ring.svg')
# ... bad news, svgutils applies rotation to the object instead of returning a rotated copy
line = svgutils.transform.fromfile('line.svg')

if line.get_size() != ring.get_size():
    raise RuntimeError('Ring/line size mismatch! Too lazy to rotate/compost properly!')

# Hope you aligned things right!
# OMG THESE AREN'T NUMBERS AAAAA
center = [int(x[:-2])/2 for x in ring.get_size()]

# Don't make me read from disk every single time I have to draw this please
# I could try deepcopying or something but let's not assume how any of this library works
# ...amazing. to_str returns bytes but fromstring
line = line.to_str().decode()

# I think they need to be added all in one go or it'll append instead of compost? Idk.
elements = [ring.getroot()]

for letter in text:
    positions = symbols[letter]
    elem = svgutils.transform.fromstring(line).getroot()
    elem.rotate(45*positions[0], *center)
    elements.append(elem)
    elem = svgutils.transform.fromstring(line).getroot()
    elem.rotate(45*positions[1], *center)
    elements.append(elem)

figure = svgutils.transform.SVGFigure(*ring.get_size())
figure.append(elements)
figure.save(text + '.svg')
