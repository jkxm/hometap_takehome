import os 
import requests

from .base_api_adapter import BaseAPIAdapter
from dotenv import load_dotenv

load_dotenv()


class ProviderTwoAdapter(BaseAPIAdapter):
	def fetch_data(self):
		try:
			headers = {
				'X-API-KEY': os.getenv('PROVIDER_ONE_KEY'),
				'Accept': 'application/json'
			}
			api_request_url = f"https://property-detail-api.fly.dev/provider-2/property?address={self.address}"
			response = requests.get(api_request_url, headers=headers)
			return response.json().get("data", None)

		except Exception as e:
			raise e
		
	def normalize(self, raw_data):
		normalized_response = {
			"Normalized Address":raw_data.get("NormalizedAddress", None),
			"Square Footage": raw_data.get("SquareFootage", None),
			"Lot Size (Acres)": raw_data.get("LotSizeAcres", None),
			"Year Built": raw_data.get("YearConstructed", None),
			"Property Type": raw_data.get("PropertyType", None),
			"Bedrooms": raw_data.get("Bedrooms", None),
			"Bathrooms": raw_data.get("Bathrooms", None),
			"Room Count": raw_data.get("RoomCount", None),
			"Septic System": raw_data.get("SepticSystem", None),
			"Sale Price": raw_data.get("SalePrice", None),
		}
		return normalized_response

	def get_data(self):
		raw = self.fetch_data()
		return self.normalize(raw)