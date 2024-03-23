import sys

import numpy as np
from tqdm import tqdm

from color import MAX_COLOR_VALUE, write_color
from ray import Ray


def ray_color(r: Ray) -> np.ndarray:
    unit_direction = r.unit_direction()
    a = 0.5 * (unit_direction[1] + 1.)
    return (1. - a) * np.array([1., 1., 1.,]) + a * np.array([0.5, 0.7, 1.0])


def main():
    # image
    aspect_ratio: float = 16. / 9.
    image_width: int = 400
    # calculate the image height
    image_height: int = int(max((image_width / aspect_ratio), 1))

    # camera
    focal_length = 1.
    viewport_height = 2.
    viewport_width = viewport_height * image_width / image_height
    camera_center = np.array([0, 0, 0])

    # calculate the vectors across the horizontal and down the vertical viewport edges
    viewport_u = np.array([viewport_width, 0, 0])
    viewport_v = np.array([0, -viewport_height, 0])

    # calculate the horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    # calculate the locatin of the upper left pixel
    viewport_upper_left = camera_center - np.array([0, 0, focal_length]) - viewport_u/2 - viewport_v/2
    pixel_00_loc = viewport_upper_left + .5 * (pixel_delta_u + pixel_delta_v)

    # render
    print(f"P3\n{image_width} {image_height}\n{MAX_COLOR_VALUE}")

    pixel_color = np.zeros(3)
    for j in tqdm(range(image_height)):
        for i in range(image_width):
            pixel_center = pixel_00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
            ray_direction = pixel_center - camera_center
            r = Ray(camera_center, ray_direction)

            pixel_color = ray_color(r)
            write_color(pixel_color)
            
    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
