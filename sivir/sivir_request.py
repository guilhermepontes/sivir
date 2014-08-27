import requests, json, os
import sivir_messages

class SivirRequest:
  def __init__(self, region = "", params = ""):
    if not all((region, params)):
      SivirMessages.error(["region", "params"])
    else:
      self.region = region
      self.params = params
      self.config()

  @staticmethod
  def load_config_file():
    path        = os.path.dirname(os.path.abspath(__file__))
    config_file = open(path + "/config/sivir_config.json").read()
    return json.loads(config_file)

  @classmethod
  def config(self):
    config = self.load_config_file()

    self.__api_key        = config["api_key"]
    self.__api_version    = config["api_version"]
    self.__production_url = config["production_url"]

  @classmethod
  def make_url(self, prod, region, api_version, params):
    url = prod + region + "/" + api_version + params
    url = url if url[-1:] == "/" else url + "/"
    return url

  @staticmethod
  def make_api_param(key):
    return {"api_key": key}

  def request(self):
    url = self.make_url(self.__production_url, self.region, self.__api_version, self.params)
    api = self.make_api_param(self.__api_key)
    r = requests.get(url, params = api)
    return r.text