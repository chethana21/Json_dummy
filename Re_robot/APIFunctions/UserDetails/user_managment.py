import os,sys
path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0],"URL_TEST")
constant_path =""
sys.path.append(dynamic_path)

from Lib.rest_call import RestCall
class RestFunctions: 
    def __init__(self, api_url):
        self.http_request = RestCall()  # Use the imported instance
        self.API_URL = api_url
    
    def get_user_data(self,user_id:int)-> dict: # i/p int & o/p dict
        """_summary_

        Args:
            user_id (int): _description_

        Returns:
            dict: _description_
        """
        endpoint = f"users/{user_id}"
        #api_url = f"{self.http_request.API_URL}/{endpoint}" # https://regress.in/users/8
        api_url = f"{self.API_URL}/{endpoint}"
        response,status_code = self.http_request.get_request(api_url)
        return response,status_code == 200
    
    def get_all_user_data(self): # no i/p & o/p list 
        page =1
        total_pages = 0
        all_user_data = []
        while True:
            endpoint = f"users?page={page}"
            #api_url = f"{self.http_request.API_URL}/{endpoint}"
            api_url = f"{self.API_URL}/{endpoint}"
            response,status_code = self.http_request.get_request(api_url)
            if "data" not in response or not response["data"]:
                break
            if total_pages == 0:
                total_pages = response["total_pages"]
            all_user_data.extend(response["data"])
            # for user in response["data"]:
            #     all_user_data.append(user) ## extend
            if page >= total_pages:
                break
            page +=1
        return len(all_user_data),status_code == 200
    
    def create_user(self, name, job):
        endpoint = "users"
        api_url = f"{self.API_URL}/{endpoint}"
        data = {"name": name, "job": job}
        response, status_code = self.http_request.post_request(api_url, data)
        return response, status_code == 201
    
    def update_user(self,user_id,name,job):
        endpoint = f"users/{user_id}"
        api_url = f"{self.API_URL}/{endpoint}"
        #api_url = f"{self.http_request.API_URL}/{endpoint}"
        data = {"name": name, "job": job}
        response,status_code = self.http_request.put_request(api_url, data)
        return response,status_code == 200
    
    def delete_user(self,user_id):
        endpoint = f"users/{user_id}"
        api_url = f"{self.API_URL}/{endpoint}"
        #api_url = f"{self.http_request.API_URL}/{endpoint}"
        response,status_code = self.http_request.delete_request(api_url)
        return response,status_code == 204

    def find_user_by_email(self,email_to_check):
        page = 1
        total_pages = 0
        matching_users = {} # returndict
        while True:
            endpoint = f"users?page={page}"
            #api_url = f"{self.http_request.API_URL}/{endpoint}"
            api_url = f"{self.API_URL}/{endpoint}"      
            response,status_code = self.http_request.get_request(api_url)
            if "data" not in response or not response["data"]:
                break
            if total_pages == 0:
                total_pages = response["total_pages"]

            for user in response["data"]: ## need to end loop
                if user.get("email") == email_to_check:
                    user_data = {
                    
                    "id": user["id"],
                    "first_name": user["first_name"],
                    "last_name": user["last_name"]
                    }
                    matching_users[user['id']] = user_data

                    #return matching_users
            if page >= total_pages:
                break
            page +=1

        return user_data,status_code == 200 # empty dict
