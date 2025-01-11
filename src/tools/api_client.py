import requests
import python_config

from config.settings import API_BASE_URL, API_KEY

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    def get_ad_groups(self):
        response = requests.get(f"{self.base_url}/api/v1/ad-groups", headers=self.headers)
        return response.json()

    def create_it_role(self, role_data):
        
        response = requests.post(
            f"{self.base_url}/api/v1/roles",
            headers=self.headers,
            json=role_data
        )
        print("printing the API response :" )
        print(response.json)

        return response.json()

    def update_business_role(self, role_id, role_data):
        response = requests.put(
            f"{self.base_url}/api/v1/roles/{role_id}",
            headers=self.headers,
            json=role_data
        )
        print("printing the API response :update_business_role")
        print(response.json)
        return response.json()