import os,sys,json,logging
path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0],"URL_TEST")
constant_path =""
sys.path.append(dynamic_path)

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from APIFunctions.UserDetails.user_managment import RestFunctions

class UserDetailsDataDriver:
    def __init__(self, api_url =  "https://reqres.in/api" ,
                 json_file_path= dynamic_path+"/TestExecutables/UserDetails/usermanagement.json"):
        self.api_url = api_url
        self.json_file_path = json_file_path
        self.class_name = RestFunctions(api_url)
        self.read_json_file()

    def read_json_file(self):
        with open(self.json_file_path, 'r') as json_file:
            self.json_data = json.load(json_file)

    def get_json_data(self):
        return self.json_data

    def compare_user_count_with_json(self):
        user_data, user_count = self.class_name.get_all_user_data()
        Output = False
        if user_count is True:
            try:
                expected_count = self.json_data.get("Total Number of Users")
                assert user_data == expected_count, f"Total Number of Users mismatch: API count {user_data}, JSON count {expected_count}"
                logger.info(f"Total Number of Users and User data are matching, API count {user_data}, JSON count {expected_count}")
                Output= True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_user_data_with_id(self,User_id):
        data_on_user_id, Status = self.class_name.get_user_data(User_id)
        Output = True
        if Status is True:
            try:
                expected_output = self.json_data.get("Details based on UserID").get(User_id)
                assert expected_output == data_on_user_id, f"There is mismatch on the User data while comparing with the User ID {User_id} this is following data of JSON {expected_output} and the data of API is {data_on_user_id}"
                logger.info(f"There is no mismatch on the User data given by User Id {User_id} this is following data of JSON {expected_output} and the data of API is {data_on_user_id}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output= False
        return Output
    
    def compare_user_data_with_email(self,email):
        data_on_user_id, Status = self.class_name.find_user_by_email(email)
        Output = False
        if Status is True:
            try:
                expected_output = self.json_data.get("Details based on Email").get(email)
                assert expected_output == data_on_user_id,f"There is mismatch on the User data while comparing with the Email ID of {email} this is following data of JSON {expected_output} and the data of API is {data_on_user_id}"
                logger.info(f"There is no mismatch on the User data given by Email Id of {email} this is following data of JSON {expected_output} and the data of API is {data_on_user_id}")
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False       
        return Output

    def compare_create_user_data(self, name, job):
        create_user_response, status_code = self.class_name.create_user(name, job)
        Output = False
        try:
            assert status_code, "Response status code is not 201 (Created)."
            create_json_response = self.json_data.get("Check details of Created User")
            user_id = create_user_response["id"]
            data_name_from_json = create_json_response.get("name")
            data_job_from_json = create_json_response.get("job")
            assert create_user_response.get("name") == data_name_from_json, f"Name does not match: {create_user_response.get('name')} and {data_name_from_json}"
            assert create_user_response.get("job") == data_job_from_json, f"Job does not match: {create_user_response.get('job')} and {data_job_from_json}"
            user_data = self.class_name.get_user_data(user_id)
            assert user_data.get("name") == data_name_from_json, f"User name does not match: {user_data.get('name')} and {data_name_from_json}"
            assert user_data.get("job") == data_job_from_json, f"User job does not match: {user_data.get('job')} and {data_job_from_json}"
            logger.info(f"Following data in the backend: {user_data.get('name')} and {user_data.get('job')}")
            Output= True
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            Output= False
        return Output

    def compare_update_user_data(self, user_id, name, job):
  
        user_data, status_code = self.class_name.get_user_data(user_id)
        logger(user_data,status_code)
  
        user_updated = False
        try:

            assert isinstance(user_data, dict) and status_code , f"User data for ID {user_id} is empty or not a valid dictionary"
        
            self.class_name.update_user(user_id, name, job)
            user_updated = True  # end
            logger.info(f"Updated user data in the API for ID {user_id}")
        
            update_user_response = self.json_data.get("Check details of Updated User")
            data_name_from_json = update_user_response.get("name")
            data_job_from_json = update_user_response.get("job")
        
            assert data_name_from_json == name and data_job_from_json == job, "User data matches between update and JSON data"
       
            user_data_after_update = self.class_name.get_user_data(user_id)
            assert isinstance(user_data_after_update, dict), f"User data for ID {user_id} is not available after update"
            assert user_data_after_update["name"] == data_name_from_json and user_data_after_update["job"] == data_job_from_json, "Backend data matches JSON data"
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            user_updated= False  
        return user_updated 
    
    def compare_delete_user_data(self,user_id):
        data, status = self.class_name.get_user_data(user_id)
        Output = False
        try:
       
            assert isinstance(data, dict) and status , f"User data for ID {user_id} is empty or not a valid dictionary"
            data_delete,delete_status = self.class_name.delete_user(user_id)
            Output = False
            logger.info(f"Deleted user data from API the ID is {user_id} and the status {delete_status}")
            check_again_api = self.class_name.get_user_data(user_id)
            
            assert check_again_api,"API does'nt exits in the backend"
            logger.debug(f"Still the User ID is in the API of {user_id} and data in the API {check_again_api}")
            Output = False
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            Output = False
        return Output

def main():
    a = UserDetailsDataDriver()
    b = a.compare_create_user_data("chethana","h/w")
    print(b)

if __name__ == "__main__":
    main()
