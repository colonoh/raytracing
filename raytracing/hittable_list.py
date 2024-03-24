import numpy as np

from hittable import Hittable, HitRecord
from ray import Ray


class HittableList(Hittable):
	def __init__(self, obj: Hittable = None):
		self.objects = []
		if obj:
			self.objects.append(obj)

	def clear(self):
		self.objects.clear()

	def add(self, obj):
		self.objects.append(obj)

	def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> (bool, HitRecord):
		# NOTE: returns a modified rec 
		temp_rec = HitRecord()
		hit_anything = False
		closest_so_far = ray_tmax

		for obj in self.objects:
			hit, temp_rec = obj.hit(r, ray_tmin, closest_so_far, temp_rec)
			if hit:
				hit_anything = True
				closest_so_far = temp_rec.t
				rec = temp_rec

		return hit_anything, rec



