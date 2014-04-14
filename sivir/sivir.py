from sivir_summoner import SivirSummoner

class Sivir(SivirSummoner):
	def __init__(self):
		SivirSummoner.__init__(self)
	
	@classmethod
	def from_region(self, region):
		self.region = region
		return self
	
	@classmethod
	def by_user(self, user):
		self.user = user
		return self
	
	@classmethod
	def by_user_id(self, user_id):
		self.user_id = user_id
	
print Sivir.from_region("br").by_user("nulled").get_data()