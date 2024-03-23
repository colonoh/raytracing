import numpy as np


class Ray:
    def __init__(self, origin: np.ndarray, direction: np.ndarray):
        self.origin = origin
        self.direction = direction

    def at(t: float) -> np.ndarray:
        return self.origin + t * self.direction

    def unit_direction(self) -> np.ndarray:
        return self.direction / np.linalg.norm(self.direction)
