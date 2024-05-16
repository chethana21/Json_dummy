import requests
import json

requests.packages.urllib3.disable_warnings()            # Disable SSL certificate verification

def delete_request(api_url):
    try:
        response = requests.delete(api_url, verify=False)
        response.raise_for_status()
        #if response.text:
        #result = response.json()
        #return result
        # else:
        print("Delete Request Successful")
        #     return None
    except requests.exceptions.RequestException as e:
        print("DELETE request error:", e)
        return None
def main():
        api_url = input("Please enter the API URL: ")
        key_to_data = int(input("Please enter the data to be Deleted from JSON dictionary: "))
        print(type(key_to_data))
        # try:
        #     key_to_data = int(key_to_data)
        # except ValueError:
        #     print("Invalid key, Please enter Integer")
        #     return 

        del_url = f'{api_url}/{key_to_data}'
        result = delete_request(del_url)
        if result is not None:
            print("Response:", result)
        else:
            print("Invalid method.")
            result = None
        if result is not None:
            print("Response:", result)
if __name__ == "__main__":
    main()