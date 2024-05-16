import requests
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()            # Disable SSL certificate verification
def GET_data(api_url):
    try:
        response = requests.get(api_url,verify= False)
        response.raise_for_status()  # Raise an exception for unsuccessful responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error GET data:", e)
        return None
# Get the API URL from the user
api_url = input("Please enter the API URL: ")

data = GET_data(api_url)
if data is not None:
    print("Received data:", data)