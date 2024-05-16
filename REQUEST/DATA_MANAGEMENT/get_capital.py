import requests
def get_country_capital(country_name):
    requests.packages.urllib3.disable_warnings()
    api_url = f"https://restcountries.com/v3.1/name/{country_name}?fields=capital"
    response = requests.get(api_url,verify=False)
    if response.status_code == 200:
        data = response.json()
        capital = data[0].get("capital")
        if capital:
            return capital
        else:
            return "Capital not found for this country."
    else:
        return "Failed to fetch data from the API."

# Input the country name from the user
country_name = input("Enter a country name: ")
# Get the capital of the specified country
capital = get_country_capital(country_name)
print(f"The capital of {country_name} is {capital}")



    def build_api_url(self, endpoint):
        return f"{self.API_URL}/{endpoint}"
     # region & subregions
    def fetch_and_display_info(self, endpoint_name):
        api_url = self.build_api_url(endpoint_name)
        response = self.http_request.get_request(api_url)
        count = 0
        countries_info = []
        for country_data in response:
            common_name = country_data.get("name", {}).get("common")
            capital = country_data.get("capital", ["N/A"])[0]
            if common_name:
                countries_info.append((common_name, capital))
                count += 1

        if count > 0:
            print(f"Number of countries: {count}")
            print("\nCommon Names and Capitals:")
            for common_name, capital in countries_info:
                print(f"Common Name: {common_name}, Capital: {capital}")