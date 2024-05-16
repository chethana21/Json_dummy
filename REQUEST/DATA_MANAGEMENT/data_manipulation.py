#from Find_Key_Val import find_value_by_key


class Dictionary:
    @staticmethod
    def find_value(dictionary, key):
        if key in dictionary:
            return dictionary[key]
        else:
            return None

    @staticmethod
    def find_keys_by_value(dictionary, value):
        keys = []
        for key, val in dictionary.items():
            if val == value:
                keys.append(key)
        return keys

    @staticmethod
    def find_value_by_key(container, key):
      if isinstance(container, dict):
        if key in container:
            return container[key]
        for value in container.values():
            if isinstance(value, (dict, list)):
                nested_value = Dictionary.find_value_by_key(value, key)
                if nested_value is not None:
                    return nested_value
      elif isinstance(container, list):
        for item in container:
            if isinstance(item, (dict, list)):
                nested_value = Dictionary.find_value_by_key(item, key)
                if nested_value is not None:
                    return nested_value
      return None

# Sample dictionaries

#"common":"[Palestine key "
#"capital":["Ramallah","Jerusalem" value ]
{
    "Palestine" : ["Ramallah","Jerusalem"]
 # count of countries
}


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

        "name": {
    
          "common": "Latvia",
    
          "official": "Republic of Latvia",
    
          "nativeName": {
    
            "lav": {
    
              "official": "Latvijas Republikas",
    
              "common": "Latvija"
    
            }
    
          }
    
        },
    
        "tld": [
    
          ".lv"
    
        ],
    
        "cca2": "LV",
    
        "ccn3": "428",
    
        "cca3": "LVA",
    
        "cioc": "LAT",
    
        "independent": 'true',
    
        "status": "officially-assigned",
    
        "unMember": 'true',
    
        "currencies": {
    
          "EUR": {
    
            "name": "Euro",
    
            "symbol": "€"
    
          }
    
        },
    
        "idd": {
    
          "root": "+3",
    
          "suffixes": [
    
            "71"
    
          ]
    
        },
    
        "capital": [
    
          "Riga"
    
        ],
    
        "altSpellings": [
    
          "LV",
    
          "Republic of Latvia",
    
          "Latvijas Republika"
    
        ],
    
        "region": "Europe",
    
        "subregion": "Northern Europe",
    
        "languages": {
    
          "lav": "Latvian"
    
        }
    
}
# Test the static methods of the class
NAME_value = Dictionary.find_value(my_dict, 'NAME')
print(NAME_value)

ROLE_value = Dictionary.find_value(my_dict, 'ROLE')
print(ROLE_value)

value_to_find = "CDC2"
keys_for_value = Dictionary.find_keys_by_value(my_dict, value_to_find)
print(f"The keys for value '{value_to_find}' are: {keys_for_value}")

region_value = Dictionary.find_value_by_key(my_nested_dict, 'tld')
print(region_value)
