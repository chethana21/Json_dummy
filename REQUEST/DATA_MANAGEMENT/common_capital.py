from rest_call import RestCall

class CommonCapital:
    def __init__(self, api_url):
        self.http_request = RestCall()
        self.API_URL = api_url
    
    def get_common_keys_and_capitals(self):
        endpoint = f"all?fields=name,capital"
        api_url = f"{self.API_URL}/{endpoint}"
        all_countries_data = self.http_request.get_request(api_url)
        common_data = {}   # creating an empty dict for country & capital
        for country_data in all_countries_data:   # iterating the list of country /
            # getting the data from name--common
            country_name = country_data.get("name", {}).get("common")
            # gets the value from country data -- name - common - capital 
            # created an empty list to avoid an error there 3 name-common doesn't have the capital
            capitals = country_data.get("capital", [])
            #checks the country name exits , it uses set default method on the common_keys_and_capitals dict 
            currencies = country_data.get("currencies",[])
            if country_name:
                common_data.setdefault(country_name,[]).extend(capitals)
            #if any([country_name,currencies]):
            # creates a new entry with country name as key & empty list as default value or 
            # extends the existing list of captials for that country name with capitals list
                common_data.setdefault(country_name,{"capitals":capitals,"currencies":currencies})
        #print(len(common_keys_and_capitals))
        return common_data, len(common_data)
  
   # fields name,country,curriencies
    def get_countries_data(self, user_fields):
        allowed_fields = ["name", "capital", "currencies"]
        response = ""
        # Split the user input into fields
        fields = [field.strip() for field in user_fields.split(",")]
        # Check if the input fields are all valid
        if all(field in allowed_fields for field in fields):
            # Combine the valid fields into a single string
            combined_fields = ",".join(fields)
            endpoint = f"all?fields={combined_fields}"
            api_url = f"{self.API_URL}/{endpoint}"
            all_countries_data = self.http_request.get_request(api_url)
            if all_countries_data:
                response += f"Data for Fields: {combined_fields}\n"
                for country_data in all_countries_data:
                    for field in fields:
                        value = country_data.get(field)
                        if value:
                            response += f"{field}: {value}\n"
                        else:
                            response += f"{field}: N/A\n"
            else:
                response = "Failed to fetch data from the API."
        else:
            response = "Invalid field(s) provided. Please choose from name, capital, or currencies."
        return response
# building the api for region & subregions
    def build_api_url(self, endpoint):
        return f"{self.API_URL}/{endpoint}"
     # region & subregions
    def fetch_and_display_info(self, endpoint_name):
        api_url = self.build_api_url(endpoint_name)
        response = self.http_request.get_request(api_url)
        count = 0
        countries_info = []
        common_names = [country['name']['common'] for country in response]
        return common_names,len(common_names)
        # for country_data in response:
        #     common_name = country_data.get("name", {}).get("common")
        #     #capital = country_data.get("capital", ["N/A"])[0]
        #     if common_name:
        #         countries_info.append((common_name))
        #         return countries_info, len(countries_info)
           #     count += 1

        # if count > 0:
        #     print(f"Number of countries: {count}")
        #     print("\nCommon Names and Capitals:")
        #     #for common_name, capital in countries_info:
        #     print(f"Common Name: {common_name}, Capital: {capital}")
        # else:
        #     print("No data available for the specified region/subregion.")

    def get_countries_in_region(self,region_name):
        region_endpoint = f"region/{region_name}"
        a = self.fetch_and_display_info(region_endpoint)
        return a
        
    def get_countries_in_subregion(self,subregion_name):
        subregion_endpoint = f"subregion/{subregion_name}"
        b = self.fetch_and_display_info(subregion_endpoint)
        return b
    def get_unique_region_subregion(self):
        endpoint = f"all?fields=region,subregion"
        api_url = f"{self.API_URL}/{endpoint}"
        data = self.http_request.get_request(api_url)         
        
        region_data = set()#{}#list
        subregion_data = set()
        for country_data in data:
            region = country_data.get("region")
            subregion = country_data.get("subregion")

            if region:
                region_data.add(region)
            if subregion:
                subregion_data.add(subregion)

        return sorted(region_data), sorted(subregion_data)
    
# When  we give country name the output will be the list of capital
    def get_country_capital(self,country_name):
        capital = []
        endpoint = f"/name/{country_name}?fields=capital" # https://restcountries.com/v3.1/name/Palestine?fields=capital
        api_url = f"{self.API_URL}/{endpoint}"
        data = self.http_request.get_request(api_url)  
        capital = data[0].get("capital")
        #if capital: # remove
        return capital


  



        
    