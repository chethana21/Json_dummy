import os,sys
path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0],"URL_TEST")
constant_path =""
sys.path.append(dynamic_path)
print(dynamic_path)
from Lib.rest_call import RestCall
# from UserFunctions.RestCountries.RestCountriesDataDriver import region
global region_name
class CommonCapital:
    def __init__(self, api_url):
        self.http_request = RestCall()
        self.API_URL = api_url
    
    def get_common_keys_and_capitals(self):
        endpoint = f"all?fields=name,capital"
        api_url = f"{self.API_URL}/{endpoint}"
        all_countries_data,status_code = self.http_request.get_request(api_url)
        common_data = {}   # creating an empty dict for country & capital
        for country_data in all_countries_data:   # iterating the list of country /
            country_name = country_data.get("name", {}).get("common")
            capitals = country_data.get("capital", [])
            currencies = country_data.get("currencies",[])
            if country_name:
                common_data.setdefault(country_name,[]).extend(capitals)
                common_data.setdefault(country_name,{"capitals":capitals,"currencies":currencies})
        return len(common_data),status_code == 200
  
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
            all_countries_data,status_code = self.http_request.get_request(api_url)
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
        return response,status_code == 200

    def get_name_in_region(self,region_name):
        region_endpoint = f"region/{region_name}"
        a = self.fetch_and_display_info(region_endpoint)
        return a
        
    def get_name_in_subregion(self,subregion_name):
        subregion_endpoint = f"subregion/{subregion_name}"
        b = self.fetch_and_display_info(subregion_endpoint)
        return b

# building the api for region & subregions
    def build_api_url(self, endpoint):
        return f"{self.API_URL}/{endpoint}"

    def fetch_and_display_info(self, endpoint_name):
        api_url = self.build_api_url(endpoint_name)
        response,status_code = self.http_request.get_request(api_url)
        common_names = [country['name']['common'] for country in response]
        return common_names,status_code == 200
    
    def get_unique_region(self):
        endpoint = f"all?fields=region"
        a = self.get_unique_common_name(endpoint)
        return a
    def get_unique_subregion(self):
        endpoint = f"all?fields=subregion"
        b = self.get_unique_common_name(endpoint)
        return b
    def get_unique_common_name(self,endpoint):
        api_url = f"{self.API_URL}/{endpoint}"
        request,status_code= self.http_request.get_request(api_url)
        region_data = set()
        name = endpoint.split("=")
        name_reg = (name[1])
        for country_data in request:
            data = country_data.get(name_reg)
            if data:
                region_data.add(data)
        a = sorted(region_data)
        b = {name_reg:a}
        return b,status_code == 200
    
# When  we give country name the output will be the list of capital
    def get_country_capital(self,country_name):
        #capital = []
        endpoint = f"/name/{country_name}?fields=capital" # https://restcountries.com/v3.1/name/Palestine?fields=capital
        api_url = f"{self.API_URL}/{endpoint}"
        data,status_code = self.http_request.get_request(api_url)  
        capital = data[0].get("capital")
        #if capital: # remove
        return capital,status_code == 200

# def Main():
#     action_handler = CommonCapital("https://restcountries.com/v3.1")
    # unique_region = action_handler.get_unique_region()
    # print(unique_region)

    # list_of_capital = action_handler.get_country_capital("Moldova")
    # print(list_of_capital)
# #     #for getting the name & Capitals value
    # common_keys_and_capitals = action_handler.get_common_keys_and_capitals() 
    # print(common_keys_and_capitals)
    # global region_name
    # region_name = "Oceania"
    # a = action_handler.get_name_in_region(region_name)
    
    # print(a)
#     region_name = "Micronesia"
#     b=action_handler.get_name_in_subregion(region_name)
#     print(b)

# if __name__ == "__main__":
#     Main()
  



        
    