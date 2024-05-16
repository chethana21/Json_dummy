def find_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None

def find_keys_by_value(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return keys

# def find_value_by_key(dictionary, key):
#     if key in dictionary:
#         return dictionary[key]

#     for value in dictionary.values():
#         if isinstance(value, dict):         # checks the current value in the dict 
#             nested_value = find_value_by_key(value, key)        # value is itself a nested dict
#             if nested_value is not None:
#                 return nested_value

#     return None

def find_value_by_key(container, key):
    if isinstance(container, dict):
        if key in container:
            return container[key]
        for value in container.values():
            if isinstance(value, (dict, list)):
                nested_value = find_value_by_key(value, key)
                if nested_value is not None:
                    return nested_value
    elif isinstance(container, list):
        for item in container:
            if isinstance(item, (dict, list)):
                nested_value = find_value_by_key(item, key)
                if nested_value is not None:
                    return nested_value
    return None

 


my_dict = {
    'ID': 1,
    'NAME': 'Chethana',
    'ROLE': "Project Engineer",
    'Location': "CDC2",
    'Base_Location': "CDC2",
    'Person': {
        'ID': 1,
        'NAME': 'Chethana',
        'Office': {'ROLE': "Project Engineer", "Location": "CDC2"}
    }
}
my_nested_dict = {
    
    "Total countries" : 250,

    
    "Countries by region": {
        
        "Oceania": ["French Polynesia", "Marshall Islands", "Kiribati", "Nauru", "Micronesia", "Norfolk Island", "Samoa", "Fiji", "Cocos (Keeling) Islands", "Cook Islands", "Niue", "Tuvalu", "Pitcairn Islands", "Tokelau", "Vanuatu", "Wallis and Futuna", "Tonga", "Australia", "New Caledonia", "Christmas Island", "Palau", "Papua New Guinea", "American Samoa", "Northern Mariana Islands", "New Zealand", "Guam", "Solomon Islands"],
        
        "Asia": ["China", "Lebanon", "Sri Lanka", "Georgia", "Turkmenistan", "Maldives", "United Arab Emirates", "Mongolia", "Kuwait", "Yemen", "Myanmar", "Laos", "Turkey", "Pakistan", "Iran", "India", "Indonesia", "Afghanistan", "Azerbaijan", "Uzbekistan", "Bangladesh", "Armenia", "Brunei", "Macau", "North Korea", "Israel", "Timor-Leste", "Saudi Arabia", "Cambodia", "Nepal", "Palestine", "Malaysia", "Thailand", "Kyrgyzstan", "Syria", "Bhutan", "Jordan", "Kazakhstan", "Oman", "Philippines", "Iraq", "South Korea", "Hong Kong", "Tajikistan", "Bahrain", "Taiwan", "Qatar", "Vietnam", "Japan", "Singapore"]} ,       
    
    "Unique Common Name by region" : {
      "region":  ["Africa", "Americas", "Antarctic", "Asia", "Europe", "Oceania"]},
      "Unique Common Name by Subregion":{
      "subregion":["Australia and New Zealand", "Caribbean", "Central America", "Central Asia", "Central Europe", "Eastern Africa", "Eastern Asia", "Eastern Europe", "Melanesia", "Micronesia", "Middle Africa", "North America", "Northern Africa", "Northern Europe", "Polynesia", "South America", "South-Eastern Asia", "Southeast Europe", "Southern Africa", "Southern Asia", "Southern Europe", "Western Africa", "Western Asia", "Western Europe"]
    },
"Get Country Capital": {
    "Palestine": ["Ramallah", "Jerusalem"]
}

}

# {

#         "name": {
    
#           "common": "Latvia",
    
#           "official": "Republic of Latvia",
    
#           "nativeName": {
    
#             "lav": {
    
#               "official": "Latvijas Republikas",
    
#               "common": "Latvija"
    
#             }
    
#           }
    
#         },
    
#         "tld": [
    
#           ".lv"
    
#         ],
    
#         "cca2": "LV",
    
#         "ccn3": "428",
    
#         "cca3": "LVA",
    
#         "cioc": "LAT",
    
#         "independent": 'true',
    
#         "status": "officially-assigned",
    
#         "unMember": 'true',
    
#         "currencies": 
#     [{
#           "EUR": {
    
#             "name": "Euro",
    
#             "symbol": "€"
    
#           }
    
#  } ]
#         ,
    
#         "idd": {
    
#           "root": "+3",
    
#           "suffixes": [
    
#             "71"
    
#           ]
    
#         },
    
#         "capital": [
    
#           "Riga"
    
#         ],
    
#         "altSpellings": [
    
#           "LV",
    
#           "Republic of Latvia",
    
#           "Latvijas Republika"
    
#         ],
    
#         "region": "Europe",
    
#         "subregion": "Northern Europe",
    
#         "languages": {
    
#           "lav": "Latvian"
    
#         }
    
# }
# Test find_value function
# NAME_value = find_value(my_dict, 'NAME')
# print(NAME_value)
# ROLE_value = find_value(my_dict, 'ROLE')
# print(ROLE_value)
# Place_value = find_value(my_dict, 'Place')
# print(Place_value)

# # Test find_keys_by_value function
# value_to_find = "CDC2"
# keys_for_value = find_keys_by_value(my_dict, value_to_find)
# print(f"The keys for value '{value_to_find}' are: {keys_for_value}")

# Test find_value_by_key function
region_value = find_value_by_key(my_nested_dict, 'Asia')
print(region_value)