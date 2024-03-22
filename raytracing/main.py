import sys

import numpy as np
from tqdm import tqdm


MAX_COLOR_VALUE: int = 255


def main():
    image_width: int = 256
    image_height: int = 256

    print(f"P3\n{image_width} {image_height}\n{MAX_COLOR_VALUE}")

    for j in tqdm(range(image_height)):
        for i in range(image_width):
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0

            ir = int(MAX_COLOR_VALUE * r)
            ig = int(MAX_COLOR_VALUE * g)
            ib = int(MAX_COLOR_VALUE * b)

            print(f"{ir} {ig} {ib}")

    print("Done!", file=sys.stderr)


if __name__ == "__main__":
    main()
