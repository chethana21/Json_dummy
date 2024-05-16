import requests
from rest_call import rest_call
# user interaction & interaction with an api

class Newusermanagement:

     # method recevies api as a parameter & creating instance for Httprequest class to interact with api

    def __init__(self,api_url):
        self.http_request = rest_call(api_url)
    
    def get_common_keys_and_capitals(self):
        # Send a GET request to the API to retrieve all country data
        endpoint = f"all"
        api_url = f"{self.http_request.API_URL}/{endpoint}"
        all_countries_data = self.http_request.get_request(api_url)
        # Initialize a dictionary to store common keys (country names) and capitals
        common_keys_and_capitals = {}
        # Check if data is not empty and contains the "common" and "capital" keys
        if all_countries_data and isinstance(all_countries_data, list):
            for country_data in all_countries_data:
                if "common" in country_data and "capital" in country_data:
                    country_name = country_data["common"]
                    capital = country_data["capital"]

                    # Add the capital to the corresponding country in the dictionary
                    if country_name in common_keys_and_capitals:
                        if isinstance(common_keys_and_capitals[country_name], list):
                            common_keys_and_capitals[country_name].append(capital)
                        else:
                            common_keys_and_capitals[country_name] = [common_keys_and_capitals[country_name], capital]
                    else:
                        common_keys_and_capitals[country_name] = capital
        return common_keys_and_capitals
if __name__ == "__main__":
    api_url = "https://restcountries.com/v3.1"
    action_handler = Newusermanagement(api_url)
    result = action_handler.get_common_keys_and_capitals()
    # Print the result in the desired format
    for country, capitals in result.items():
        formatted_capitals = capitals if isinstance(capitals, list) else [capitals]
        formatted_output = f"{country}: {', '.join(formatted_capitals)}"
        print(formatted_output)                       

    def get_all_data(self):
            endpoint = f"all"
            api_url = f"{self.http_request.API_URL}/{endpoint}"
            response = self.http_request.get_request(api_url)
            return response

    def get_data_by_name(self, name):         
        endpoint = f"name/{name}"        
        api_url = f"{self.http_request.API_URL}/{endpoint}"     
        print(f"Fetching data by name: {name}")         
        response = self.http_request.get_request(api_url)         
        return response
    
    def get_data_by_full_name(self, full_name):         
        endpoint = f"name/{full_name}?fullText=true"        
        api_url = f"{self.http_request.API_URL}/{endpoint}"     
        print(f"Fetching data by full name: {full_name}")         
        response = self.http_request.get_request(api_url)         
        return response
    
    def get_data_by_code(self, country_code):         
        endpoint = f"alpha/{country_code}"        
        api_url = f"{self.http_request.API_URL}/{endpoint}"     
        print(f"Fetching data for country code: {country_code}")         
        response = self.http_request.get_request(api_url)         
        return response
    
    def get_countries_by_codes(self, country_codes):         
        codes = ",".join(country_codes)         
        endpoint = f"alpha?codes={codes}"        
        api_url = f"{self.http_request.API_URL}/{endpoint}" 
        print(f"Fetching data for country codes: {codes}")         
        response = self.http_request.get_request(api_url)         
        return response

    def get_data_by_currency(self, currency):          
        endpoint = f"currency/{currency}"        
        api_url = f"{self.http_request.API_URL}/{endpoint}" 
        print(f"Fetching data for currency: {currency}")         
        response = self.http_request.get_request(api_url)         
        return response
    
    