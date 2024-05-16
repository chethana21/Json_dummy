

from rest_call import RestCall

 

class CommonCapital:

    def __init__(self, api_url):

        self.api_url = api_url

        self.http_request = RestCall()

 

    def build_api_url(self, endpoint):

        return f"{self.api_url}/{endpoint}"

 

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

        else:

            print("No data available for the specified region/subregion.")

 

def main():

    # Provide the API URL in the main function

    api_url = "https://restcountries.com/v3.1"

    info_fetcher = CommonCapital(api_url)

 

    # Prompt the user for region and subregion names

    region_name = input("Enter a region name (e.g., Europe): ")

    subregion_name = input("Enter a subregion name (e.g., Northern Europe): ")

 

    # Build endpoints based on user-provided names

    region_endpoint = f"region/{region_name}"

    subregion_endpoint = f"subregion/{subregion_name}"

 

    # Fetch and display data for the specified region and subregion

    info_fetcher.fetch_and_display_info(region_endpoint)

    info_fetcher.fetch_and_display_info(subregion_endpoint)

 

if __name__ == "__main__":

    main()


     
    # when we enter a region it will list out the count and name & capital
#     region = input("Enter a region: ")
#    # Get countries in the specified region and their count
#     countries_info, count = action_handler.get_countries_in_region(region)
#     print(countries_info)
#     print(count)
#     print(f"Number of countries in {region}: {count}")
#     print("\nCountry Names and Capitals:")
#     for common_name, capital in countries_info:
#             print(f"Common Name: {common_name}, Capital: {capital}")
    
#     #when we enter a sub-region it will list out the count and name & capital
#     subregion = input("Enter a Sub-region: ")
#     # Get countries in the specified region and their count
#     countries_info, count = action_handler.get_countries_in_subregion(subregion)
#     print(f"Number of countries in {subregion}: {count}")
#     print("\nCountry Names and Capitals:")
#     for common_name, capital in countries_info:
#             print(f"Common Name: {common_name}, Capital: {capital}")


    # def get_countries_in_region(self,region):
    #     endpoint = f"region/{region}"
    #     api_url = f"{self.API_URL}/{endpoint}"
    #     data = self.http_request.get_request(api_url)
    #     # Initialize a list to store country names and capitals
    #     countries_info = []
    #    # Iterate through the data to extract common names and capitals
    #     for country_data in data:
    #         common_name = country_data.get("name", {}).get("common")
    #         capital = country_data.get("capital", [])  
    #         if common_name:
    #             countries_info.append((common_name, capital)) # dict
    #     return countries_info, len(countries_info)
    
    # def get_countries_in_subregion(self,subregion):
    #     endpoint = f"subregion/{subregion}"
    #     api_url = f"{self.API_URL}/{endpoint}"
    #     data = self.http_request.get_request(api_url)
    #     # Initialize a list to store country names and capitals
    #     countries_info = []
    #     # Iterate through the data to extract common names and capitals
    #     for country_data in data:
    #         common_name = country_data.get("name", {}).get("common")
    #         capital = country_data.get("capital", [])  
    #         if common_name:
    #             countries_info.append((common_name, capital))
    #     return countries_info, len(countries_info)

        # Build endpoints based on user-provided names
    # ### functions ####
    # region_endpoint = f"region/{region_name}"
    # subregion_endpoint = f"subregion/{subregion_name}"
    # # Fetch and display data for the specified region and subregion
    # action_handler.fetch_and_display_info(region_endpoint)
    # action_handler.fetch_and_display_info(subregion_endpoint)
