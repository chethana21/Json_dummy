import os,sys,json
path_to_find = __file__
paths = path_to_find.split('\\Re_robot\\')
dynamic_path = os.path.join(paths[0],"Re_robot")
sys.path.append(dynamic_path)
from APIFunctions.RestCountries.rest_countries import CommonCapital
class RestCountriesDataDriver:
    def __init__(self, api_url="https://restcountries.com/v3.1", 
                 json_file_path="C:/Users/Administrator/OneDrive - Wipro/Fujitsu/Re_robot/TestExecutables/RestCountries/restcountry.json"): 
       #"C:\Users\Administrator\OneDrive - Wipro\Fujitsu\Re_robot\TestExecutables\RestCountries\restcountry.json"
        #json_file_path = "restcountry.json"):
        self.api_url = api_url
        self.json_file_path = json_file_path
        self.class_name = CommonCapital(api_url)
        self.json_data = None
        self.read_json_file()

    def read_json_file(self):
        with open(self.json_file_path, 'r') as json_file:
            self.json_data = json.load(json_file)

    def get_json_data(self):
        return self.json_data
    
    def compare_common_name_count_with_json(self): #C:\Users\Administrator\OneDrive - Wipro\Fujitsu\URL_Test\TestExecutables\RestCountries
        common_name_count,Status = self.class_name.get_common_keys_and_capitals()
        Output = False
        if Status is True:
            try:
                expected_count = self.json_data.get("Total countries")
                assert common_name_count == expected_count, f"Total number of countries in Json data {expected_count} and in API {common_name_count} count are not matching"
                #print(f"Total number of countries in Json data {expected_count} and in API {common_name_count} count are matching")         
                print(f"Total number of countries in Json data and in API count are matching")
                Output = True
            except AssertionError as e:
                print(f"AssertionError: {e}")   
                Output = False
        else:
            print("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
def Main():
#     api_url = "https://restcountries.com/v3.1"
#     json_file_path = "TestExecutables/RestCountries/restcountry.json"
    data_driven = RestCountriesDataDriver()
    a = data_driven.compare_common_name_count_with_json()
    print(a)
if __name__ == "__main__":
    Main()