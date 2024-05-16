import os,sys,json,logging
path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0],"URL_TEST")
constant_path =""
sys.path.append(dynamic_path)

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from APIFunctions.RestCountries.rest_countries import CommonCapital

class RestCountriesDataDriver:
    def __init__(self, api_url="https://restcountries.com/v3.1", json_file_path = dynamic_path+"/TestExecutables/RestCountries/restcountry.json"):
        self.api_url = api_url
        self.json_file_path = json_file_path
        self.class_name = CommonCapital(api_url)
        self.read_json_file()

    def read_json_file(self):
        try:
            with open(self.json_file_path, 'r') as json_file:
                self.json_data = json.load(json_file)
        except FileNotFoundError:
            logger.error(f"File not found: {self.json_file_path}")
            raise

    def get_json_data(self):
        return self.json_data

    def compare_common_name_count_with_json(self): #C:\Users\Administrator\OneDrive - Wipro\Fujitsu\URL_Test\TestExecutables\RestCountries
        common_name_count,Status = self.class_name.get_common_keys_and_capitals()
        Output = False
        if Status is True:
            try:
                expected_count = self.json_data.get("Total countries")
                assert common_name_count == expected_count, f"Total number of countries in Json data {expected_count} and in API {common_name_count} count are not matching"
                logger.info(f"Total number of countries in Json data {expected_count} and in API {common_name_count} count are matching")         
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")   
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_with_regions(self,region_name):    
        common_names, Status = self.class_name.get_name_in_region(region_name)
        Output = False
        if Status is True:
            try:
                expected_common_names = self.json_data.get("Countries by region").get(region_name)
    # Call the function to get the common names for the specified region
                assert common_names == expected_common_names, f"Country names of {region_name} are not matching in API {common_names} and JSON {expected_common_names}"
                logger.info(f"Country names of {region_name} are matching in API {common_names} and JSON {expected_common_names}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_with_subregions(self,subregion_name):    
        common_names,Status = self.class_name.get_name_in_region(subregion_name)
        Output = False
        if Status is True:
            try:
                expected_common_names = self.json_data.get("Countries by Sub-region").get(subregion_name)
                assert common_names == expected_common_names, f"Country names of {subregion_name} are not matching in API {common_names} and JSON {expected_common_names}"
                logger.info(f"Country names of {subregion_name} are matching in API {common_names} and JSON {expected_common_names}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_unique_regions(self):
        unique_name, Status = self.class_name.get_unique_region()
        Output = False
        if Status is True:
            try:
                expected_output = self.json_data.get("Unique Common Name by region")
                assert expected_output == unique_name, f"Unique names of the regions are not matching with the API {unique_name} and JSON data {expected_output}"
                logger.info(f"Unique names of the regions are matching with the API {unique_name} and JSON data {expected_output}")
                Output =  True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_unique_subregions(self):
        unique_name,Status = self.class_name.get_unique_subregion()
        Output = False
        if Status is True:
            try:
                expected_output = self.json_data.get("Unique Common Name by Subregion")
                assert expected_output == unique_name, f"Unique names of the subregions are not matching with the API {unique_name} and JSON data {expected_output}"
                logger.info(f"Unique names of the subregions are matching with the API {unique_name} and JSON data {expected_output}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_common_name_country(self,country_name):
        name_of_country, Status = self.class_name.get_country_capital(country_name)
        Output = False
        if Status is True:
            try:
                expected_output = self.json_data.get("Get Country Capital").get(country_name)
                assert expected_output == name_of_country, f"Capitals of {country_name} are not matching with the API {name_of_country} and JSON data {expected_output}"
                logger.info(f"Capitals of {country_name} are matching with the API {name_of_country} and JSON data {expected_output}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output

def Main():
# #     api_url = "https://restcountries.com/v3.1"
# #     json_file_path = "TestExecutables/RestCountries/restcountry.json"
    data_driven = RestCountriesDataDriver()
    # a = data_driven.compare_common_name_count_with_json()
    # print(a)
    b = data_driven.compare_with_regions("Asia")
    print(b)
if __name__ == "__main__":
    Main()

    # b = data_driven.compare_with_regions("Asia")
    # print(b)

    # c = data_driven.compare_with_regions("Oceania")
    # print(c)

    # d = data_driven.compare_unique_regions()
    # print(d)

    # e = data_driven.compare_unique_subregions()
    # print(e)

    # f = data_driven.compare_common_name_country('Palestine')
    # print(f)

    # g = data_driven.compare_common_name_country('North Macedoni')
    # print(g)

    # h = data_driven.compare_common_name_country('Lebanon')
    # print(h)

    # i = data_driven.compare_with_subregions('Central America')
    # print(i)

    # j = data_driven.compare_with_subregions('Micronesia')
    # print(j)

# if __name__ == "__main__":
#     Main()