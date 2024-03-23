import numpy as np



MAX_COLOR_VALUE: int = 255


def write_color(v: np.ndarray):
    print(f"{int(MAX_COLOR_VALUE * v[0])} {int(MAX_COLOR_VALUE * v[1])} {int(MAX_COLOR_VALUE * v[2])}")
