import requests
import json
import os

class SivirRequest:
	def __init__(self, region = "", params = ""):
		if not all((region, params)):
			raise Exception("You have to enter the <URL> AND <PARAMS> AND <REGION> or Hecarim is going to be with you at night.")
		else:
			self.region = region
			self.params = params
			self.config()

	@classmethod
	def config(self): 
		path        = os.path.abspath(".") + "/sivir/"
		config_file = open(path + "config/sivir_config.json").read()
		config      = json.loads(config_file)
		
		self.__api_key        = config["api_key"]
		self.__api_version    = config["api_version"]
		self.__production_url = config["production_url"]
	
	def request(self):
		url = self.__production_url + self.region + "/" + self.__api_version + self.params
		url = url if url[-1:] == "/" else url + "/"
		api = {"api_key": self.__api_key}

		r = requests.get(url, params = api)
		return r.text