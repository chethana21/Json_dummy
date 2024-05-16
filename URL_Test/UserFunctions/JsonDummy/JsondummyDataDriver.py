import os,sys,json,logging
path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0],"URL_TEST")
constant_path =""
sys.path.append(dynamic_path)

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


from APIFunctions.JsonDummy.dummy_products import json_dummy

class JsondummyDataDriver:
    def __init__(self, api_url="https://dummyjson.com", json_file_path = dynamic_path+"/TestExecutables/JsonDummy/jsondummy.json"):
        self.api_url = api_url
        self.json_file_path = json_file_path
        self.class_name = json_dummy(api_url)
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
    
    def compare_category_by_product_details(self):
        product_details,Status = self.class_name.get_category_and_brand_info()
        Output = False
        if Status is True:
            try:
                expected_data = self.json_data.get("Product Details")
                
                assert product_details == expected_data, f"Category based on product of API {product_details} didn't match with JSON data {expected_data}"
                logger.info(f"Category based on product of API {product_details} and JSON data {expected_data} are matching")         
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")   
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_categoryname_for_product_details_by_product(self,category_name):
        product_details,Status = self.class_name.get_categoryname_for_products_by_user(category_name)
        Output = False
        if Status is True:
            try:
                expected_data = self.json_data.get("Product Details by user")
                assert product_details == expected_data, f"Category based on product of the product of API {product_details} didn't match with JSON data {expected_data}"
                logger.info(f"Category based on product of API {product_details} and JSON data {expected_data} are matching")         
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")   
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output
    
    def compare_data_by_keywords(self,keyword_name):
        product_details,Status = self.class_name.get_data_by_keywords(keyword_name)
        Output = False
        if Status is True:
            try:
                expected_data = self.json_data.get("Keyword name for getting data").get(keyword_name)
                assert product_details == expected_data, f"Category based on product of the product of API {product_details} didn't match with JSON data {expected_data}"
                logger.info(f"Category based on product of API {product_details} and JSON data {expected_data} are matching")         
                Output = True
            except AssertionError as e:
                logger.error(f"AssertionError: {e}")   
                Output = False
        else:
            logger.warning("API function did not succeed, so the comparison is skipped.")
            Output = False
        return Output        
        
    def compare_create_product_data(self, title):
        create_product_response, status_code = self.class_name.add_products(title)
        Output = False
        try:
            assert status_code, "Response status code is not 201 (Created)."
            create_json_response = self.json_data.get("Check details of Created product")
            product_id = create_product_response["id"]
            data_title_from_json = create_json_response.get("title")

            assert create_product_response.get("title") == data_title_from_json, f"Name does not match: {create_product_response.get('title')} and {data_title_from_json}"
            
            product_data = self.class_name.get_data_for_products_by_userid(product_id)
            assert product_data.get("title") == data_title_from_json, f"product name does not match: {product_data.get('title')} and {data_title_from_json}"

            logger.info(f"Following data in the backend: {product_data.get('title')}")
            Output= True
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            Output= False
        return Output

    def compare_update_user_data(self, user_id, title):
  
        user_data, status_code = self.class_name.get_data_for_products_by_userid(user_id)
        logger(user_data,status_code)
  
        user_updated = False
        try:

            assert isinstance(user_data, dict) and status_code , f"User data for ID {user_id} is empty or not a valid dictionary"
        
            b = self.class_name.update_products(user_id, title)
            
            user_updated = True  # end
            logger.info(f"Updated user data in the API for ID {user_id}")
        
            update_user_response = self.json_data.get("Check details of Updated product User")
            data_title_from_json = update_user_response.get("title")

        
            assert data_title_from_json == b.get(title), "User data matches between update and JSON data"
       
            user_product_after_update = self.class_name.get_data_for_products_by_userid(user_id)
            assert isinstance(user_product_after_update, dict), f"User data for ID {user_id} is not available after update"
            assert user_product_after_update["title"] == data_title_from_json, "Backend data matches JSON data"
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            user_updated= False  
        return user_updated 

    def compare_delete_product_data(self,user_id):
        data, status = self.class_name.get_data_for_products_by_userid(user_id)
        Output = False
        try:
       
            assert isinstance(data, dict) and status , f"User data for ID {user_id} is empty or not a valid dictionary"
            data_delete,delete_status = self.class_name.delete_product(user_id)
            Output = False
            logger.info(f"Deleted user data from API the ID is {user_id} and the status {delete_status}")
            check_again_api = self.class_name.get_data_for_products_by_userid(user_id)
            
            assert check_again_api,"API does'nt exits in the backend"
            logger.debug(f"Still the User ID is in the API of {user_id} and data in the API {check_again_api}")
            Output = False
        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            Output = False
        return Output

def main():

    action = JsondummyDataDriver()
    # a = action.compare_category_by_product_details()
    # print(a)
    b = action.compare_categoryname_for_product_details_by_product("laptops")
    print(b)
    # c = action.compare_data_by_keywords("Apple")
    # print(c)
    # d = action.compare_create_product_data("BMW Pencil")
    # print(d)
    

if __name__ == "__main__":
    main()