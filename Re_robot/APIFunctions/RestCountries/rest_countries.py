import os,sys
path_to_find = __file__
paths = path_to_find.split('\\RE_Robot\\')
dynamic_path = os.path.join(paths[0],"RE_Robot")
constant_path =""
sys.path.append(dynamic_path)
print(dynamic_path)
from Lib.rest_call import RestCall
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