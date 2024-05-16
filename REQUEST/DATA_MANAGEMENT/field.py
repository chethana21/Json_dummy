import requests
from rest_call import RestCall

class CommonCapital:
    def __init__(self, api_url):
        self.http_request = RestCall()
        self.API_URL = api_url
    
    def get_countries_in_region(self,region):
        endpoint = f"region/{region}"
        api_url = f"{self.API_URL}/{endpoint}"
        data = self.http_request.get_request(api_url)

        # Initialize a list to store country names and capitals
        countries_info = []

        # Iterate through the data to extract common names and capitals
        for country_data in data:
            common_name = country_data.get("name", {}).get("common")
            capital = country_data.get("capital", [])  
            if common_name:
                countries_info.append((common_name, capital))
        return countries_info, len(countries_info)
    
    def get_countries_in_subregion(self,subregion):
        endpoint = f"subregion/{subregion}"
        api_url = f"{self.API_URL}/{endpoint}"
        data = self.http_request.get_request(api_url)

        # Initialize a list to store country names and capitals
        countries_info = []

        # Iterate through the data to extract common names and capitals
        for country_data in data:
            common_name = country_data.get("name", {}).get("common")
            capital = country_data.get("capital", [])  
            if common_name:
                countries_info.append((common_name, capital))
        return countries_info, len(countries_info)
 # Return empty list and count 0 if there's an issue with the API request

    def get_unique_region_subregion(self):
        endpoint = f"all"
        api_url = f"{self.API_URL}/{endpoint}"
        data = self.http_request.get_request(api_url)         
        
        region_counts = {}
        subregion_counts = {}
        for country_data in data:
            region = country_data.get("region")
            subregion = country_data.get("subregion")

            if region:
                region_counts[region] = True
            if subregion:
                subregion_counts[subregion] = True

        #return unique_regions_dict, unique_subregions_dict
        # Iterate through the data to extract regions and subregions
        # for country_data in data:
        #     region = country_data.get("region")
        #     subregion = country_data.get("subregion")

        #     if region:
        #         region_counts[region] = region_counts.get(region, 0) + 1
        #     if subregion:
        #         subregion_counts[subregion] = subregion_counts.get(subregion, 0) + 1

        # # Filter unique regions and subregions
        # unique_regions = [region for region, count in region_counts.items() if count == 1]
        # unique_subregions = [subregion for subregion, count in subregion_counts.items() if count == 1]

        return region_counts, subregion_counts


def main():
    action_handler = CommonCapital("https://restcountries.com/v3.1")
    
   # region = input("Enter a region: ")
    # Get countries in the specified region and their count
    # countries_info, count = action_handler.get_countries_in_region(region)
    # print(f"Number of countries in {region}: {count}")
    # print("\nCountry Names and Capitals:")
    # for common_name, capital in countries_info:
    #         print(f"Common Name: {common_name}, Capital: {capital}")
    
    # subregion = input("Enter a Sub-region: ")
    # # Get countries in the specified region and their count
    # countries_info, count = action_handler.get_countries_in_subregion(subregion)
    # print(f"Number of countries in {subregion}: {count}")
    # print("\nCountry Names and Capitals:")
    # for common_name, capital in countries_info:
    #         print(f"Common Name: {common_name}, Capital: {capital}")

    unique_regions, unique_subregions = action_handler.get_unique_region_subregion()
    if unique_regions:
        print("Unique Regions:")
        for region in unique_regions:
            print(region)

    if unique_subregions:
        print("\nUnique Subregions:")
        for subregion in unique_subregions:
            print(subregion)
 

if __name__ == "__main__":
    main()