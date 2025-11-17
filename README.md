## Instructions for Running Application

Same as the starter template instructions

Backend:
```bash
cd backend
poetry install
poetry shell
poetry run python manage.py runserver
```


Frontend:
```bash
cd frontend
yarn install
yarn dev
```

## Design Decisions

### Adapter Pattern

Given the requirements for the problem, I thought using the adapter pattern would be the best approach. 

The idea being, each api endpoint would get its own adapter class to retrieve data from their respective endpoint, and each class would be responsible for normalizing the response.

```
class BaseAPIAdapter(ABC):
	@abstractmethod
	def fetch_data(self): -> fetch data from api
		pass
	
	@abstractmethod
	def normalize(self, raw_data): -> normalize it
		pass
	
	
	def __init__(self, address: str):
		self.address = address

	def get_data(self):
		raw = self.fetch_data()
		return self.normalize(raw)
```

### Frontend
Simple loop through the returned data and creating a card per provider. 

**Used AI tools** for syntax help, ie how to create a grid and style the containers

```
 {Object.entries(apiResponse).map(([provider, data]) => (
	<div key={provider} className="bg-white p-6 rounded-lg shadow-md">
		<h3 className="text-lg font-bold mb-4 text-blue-600">{provider}</h3>
		<div className="space-y-2 text-sm">
		<div><span className="font-semibold">Address:</span> {data["Normalized Address"]}</div> -> each property listed in a row
		</div>
	</div>
	))}
```

## Additional Ideas
- representing api responses as a dataclass for easier validation/normalization
- include unit testing + mock api requests
- string enums for provider names instead of hard coding
- dockerizing application for easier sharing/startup
- hold api keys in a vault
- error window on frontend when exception is returned from the backend
- highlight differences between differnce providers
