from sivir_request import SivirRequest

class SivirSummoner(SivirRequest):
  def __init__(self): pass

  @classmethod
  def get_data(self):
    return SivirRequest(self.region, "/summoner/by-name/" + self.user).request()



