
from abc import ABC
from abc import abstractmethod
'''
normalized_response = {
	"Normalized Address":address,
	"Square Footage": 2165,
	"Lot Size (Acres)": 0.43,
	"Year Built": 1975,
	"Property Type": "Townhouse",
	"Bedrooms": 2,
	"Bathrooms": 2,
	"Room Count": 5,
	"Septic System": "Yes",
	"Sale Price": 350000,
}

'''

class BaseAPIAdapter(ABC):

	@abstractmethod
	def fetch_data(self):
		pass
	
	@abstractmethod
	def normalize(self, raw_data):
		pass
	
	
	def __init__(self, address: str):
		self.address = address

	def get_data(self):
		raw = self.fetch_data()
		return self.normalize(raw)
