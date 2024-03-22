import sys

import numpy as np
from tqdm import tqdm

from color import MAX_COLOR_VALUE, write_color


def main():
    image_width: int = 256
    image_height: int = 256

    print(f"P3\n{image_width} {image_height}\n{MAX_COLOR_VALUE}")

    pixel_color = np.zeros(3)

    for j in tqdm(range(image_height)):
        for i in range(image_width):
            pixel_color[0] = i / (image_width - 1)
            pixel_color[1] = j / (image_height - 1)
            pixel_color[2] = 0
            write_color(pixel_color)
            
    print("Done!", file=sys.stderr)


if __name__ == "__main__":
    main()
