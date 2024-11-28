import requests
from lab7.classes.api_config import APIConfig

class DataRepository:
    def __init__(self, resource):
        self.api_url = f"{APIConfig().base_url}/{resource}"

    def get_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error: Unable to fetch data - {e}")