from common_capital import CommonCapital
def Main():
    action_handler = CommonCapital("https://restcountries.com/v3.1")

#     #for getting the name & Capitals value
#     common_keys_and_capitals = action_handler.get_common_keys_and_capitals() 
#     print(common_keys_and_capitals)
# #     #print("\n")
    

   # it list all the regions & subregions 
    unique_regions, unique_subregions = action_handler.get_unique_region_subregion()
    print(unique_regions)
    #print("\n")
    print(unique_subregions)
    #print("\n")


    # Prompt the user for region and subregion names
    # region_name = input("Enter a region name (e.g., Europe): ")
    # subregion_name = input("Enter a subregion name (e.g., Northern Europe): ")
    # a = action_handler.get_countries_in_region("Oceania")
    # print(a)
    # b=action_handler.get_countries_in_region("Asia")
    # print(b)
   # action_handler.get_countries_in_subregion("Eastern Europe")
    #action_handler.get_countries_in_subregion("Eastern Europe")
    # print(a)
    # print(b)
    

   #Input the country name from the user
    # country_name = input("Enter a country name: ")
    # # Get the capital of the specified country
    capital = action_handler.get_country_capital("Fiji")
    print(capital)

    capital = action_handler.get_country_capital("Papua New Guinea")
    print(capital)
    

    #in the api url if we give any field has name,capital or currencies 
    #user_field = input("Enter a field (name, capital, currencies): ")
# Call the get_countries_data function with the user's input
    # result = action_handler.get_countries_data("name")
    # print(result)
    # result = action_handler.get_countries_data("name,currencies")
    # print(result)

if __name__ == "__main__":
    Main()





























# from new_user_management import Newusermanagement
# def Main():
    
#     action_handler = Newusermanagement("https://restcountries.com/v3.1")
#     result = action_handler.get_common_keys_and_capitals()
#     # Print the result in the desired format
#     for country, capitals in result.items():
#         formatted_capitals = capitals if isinstance(capitals, list) else [capitals]
#         formatted_output = f"{country}: {', '.join(formatted_capitals)}"
#         print(formatted_output)
    # a =action_handler.get_all_data()
    # print(a)
    
    # name1 = "eesti"
    # response1 = action_handler.get_data_by_name(name1) 
    # print(response1)
    # name2 = "deutschland"
    # response2 = action_handler.get_data_by_name(name2)
    # print(response2)    

    # full_name1 = "aruba"
    # response1 = action_handler.get_data_by_full_name(full_name1)
    # print(response1)


    # country_code1 = "co"
    # response1 = action_handler.get_data_by_code(country_code1) 
    # print(response1)
    # country_code2 = "col"
    # response2 = action_handler.get_data_by_code(country_code2)
    # print(response2)

    # country_code = ["170","no","est","pe"]
    # response = action_handler.get_countries_by_codes(country_code)
    # print(response)

    # currency = "cop"
    # response = action_handler.get_data_by_currency(currency)
    # print(response)

if __name__ == "__main__":
    Main()