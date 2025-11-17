import os 
import requests

from .base_api_adapter import BaseAPIAdapter
from dotenv import load_dotenv

load_dotenv()


class ProviderOneAdapter(BaseAPIAdapter):
	def fetch_data(self):
		try:
			headers = {
				'X-API-KEY': os.getenv('PROVIDER_ONE_KEY'),
				'Accept': 'application/json'
			}
			api_request_url = f"https://property-detail-api.fly.dev/provider-1/property?address={self.address}"
			response = requests.get(api_request_url, headers=headers)
			return response.json().get("data", None)

		except Exception as e:
			raise e
		
	def normalize(self, raw_data):
		normalized_response = {
			"Normalized Address":raw_data.get("formattedAddress", None),
			"Square Footage": raw_data.get("squareFootage", None),
			"Lot Size (Acres)": float(raw_data.get("lotSizeSqFt", None)/43560) if raw_data.get("lotSizeSqFt", None) else None,
			"Year Built": raw_data.get("yearBuilt", None),
			"Property Type": raw_data.get("propertyType", None),
			"Bedrooms": raw_data.get("bedrooms", None),
			"Bathrooms": raw_data.get("bathrooms", None),
			"Room Count": raw_data.get("features", None).get("roomCount", None) if raw_data.get("features", None) else None,
			"Septic System": raw_data.get("features", None).get("septicSystem", None) if raw_data.get("features", None) else None,
			"Sale Price": raw_data.get("lastSalePrice", None),
		}
		return normalized_response

	def get_data(self):
		raw = self.fetch_data()
		return self.normalize(raw)