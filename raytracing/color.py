import numpy as np



MAX_COLOR_VALUE: int = 255


def write_color(vector):
    print(f"{int(MAX_COLOR_VALUE * vector[0])} {int(MAX_COLOR_VALUE * vector[1])} {int(MAX_COLOR_VALUE * vector[2])}")
