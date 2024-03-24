import sys

import numpy as np

from ray import Ray


class HitRecord:
    def __init__(self):
        # initializes empty
        self.p = np.array([0., 0., 0.])
        self.normal = np.array([0., 0., 0.])
        self.t = 0.

    def set_face_normal(self, ray: Ray, outward_normal: np.ndarray):
        # sets the hit record normal vector
        # NOTE: `outward_normal` assumed to be unit vector
        self.front_face = np.dot(ray.direction, outward_normal)
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable:
    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> (bool, HitRecord):
        raise NotImplemented
