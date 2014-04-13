import requests
import sivir_request



class Sivir(SivirRequest):
	def __init__(self, key="123"):
		if key == "":
			raise Exception("You have to enter the API Key or Hecarim is going to be with you at night.")
		else:
			self.key = key

	def from_region(self, region):
		print region

	def by_user(self, user):
		print Sirvir


s = SivirRequest("key", "params")
