import numpy as np

from hittable import Hittable, HitRecord
from ray import Ray


class Sphere(Hittable):
    def __init__(self, center: np.ndarray, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> (bool, HitRecord):
        oc = r.origin - self.center
        a = np.dot(r.direction, r.direction)
        half_b = np.dot(oc, r.direction)
        c = np.dot(oc, oc) - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0.:
            return False, rec
        sqrtd = np.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        if root <= ray_tmin or ray_tmax <= root:
            root = (-half_b + sqrtd) / a
            if root <= ray_tmin or ray_tmax <= root:
                return False, rec

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True, rec
