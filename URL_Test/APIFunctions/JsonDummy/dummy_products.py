import os
import sys

path_to_find = __file__
paths = path_to_find.split('\\URL_Test\\')
dynamic_path = os.path.join(paths[0], "URL_TEST")
constant_path = ""
sys.path.append(dynamic_path)

from Lib.rest_call import RestCall


class json_dummy:
    def __init__(self, api_url):
        self.http_request = RestCall()  # Use the imported instance
        self.API_URL = api_url
    
    def get_data_for_products_by_userid(self,User_id):
        endpoint = f"products/{User_id}" #https://dummyjson.com/products/1
        api_url = f"{self.API_URL}/{endpoint}"
        product_info,status_code= self.http_request.get_request(api_url)
        #product_info = request.get("products", {})
        return { 'product details':{'brand': product_info.get("brand"),
        'title': product_info.get("title"),
        'category': product_info.get("category")},
        'status_code':status_code == 200}
    
    def get_category_and_brand_info(self):
        endpoint = "products"
        a = self.get_product_data(endpoint)
        return a
    
    def get_categoryname_for_products_by_user(self,category_name):
        endpoint = f"products/category/{category_name}" 
        b = self.get_product_data(endpoint)
        return b
    
    def get_product_data(self,endpoint):    
        api_url = f"{self.API_URL}/{endpoint}"
        response, status_code = self.http_request.get_request(api_url)
        products = response.get("products", [])
        category_info = {}
        for product in products:
                category = product.get("category")
                brand = product.get("brand")
                if category not in category_info:
                    category_info[category] = {"count": 0, "brands": []}
                category_info[category]["count"] += 1
                category_info[category]["brands"].append(brand)
        return category_info,status_code == 200
    
    def add_products(self,title):
        endpoint = "products/add"
        api_url = f"{self.API_URL}/{endpoint}"
        data = {"title": title}
        response, status_code = self.http_request.post_request(api_url, data)
        return response, status_code == 201
    
    def update_products(self, user_id, title):
        endpoint = f"carts/{user_id}"
        api_url = f"{self.API_URL}/{endpoint}"
        data = {"title": title}
        response, status_code = self.http_request.put_request(api_url, data)
        return response, status_code == 200
   
    def delete_product(self,user_id):
        endpoint = f"carts/{user_id}"
        api_url = f"{self.API_URL}/{endpoint}"
        response,status_code = self.http_request.delete_request(api_url)
        return response,status_code == 204
    
#     def get_data_for_carts_by_userid(self,User_id):
#         endpoint = f"carts/user/{User_id}" #https://dummyjson.com/carts/user/5
#         api_url = f"{self.API_URL}/{endpoint}"
#         request,status_code= self.http_request.get_request(api_url)
#         return request,status_code==200
    
#     def add_items_to_cart(self, products):
#         endpoint = "carts/add"
#         api_url = f"{self.API_URL}/{endpoint}"
#         data = {"products": products}

#         response, status_code = self.http_request.post_request(api_url, data)
#         return response, status_code == 201
    
#     def update_items_in_cart(self, user_id, product_name, quantity):
#         endpoint = f"carts/{user_id}"
#         api_url = f"{self.API_URL}/{endpoint}"
#         data = {"product_name": product_name,"quantity":quantity}
#         response, status_code = self.http_request.put_request(api_url, data)
#         return response, status_code == 200
   
#     def delete_items_in_cart(self,user_id):
#         endpoint = f"carts/{user_id}"
#         api_url = f"{self.API_URL}/{endpoint}"
#         response,status_code = self.http_request.delete_request(api_url)
#         return response,status_code == 204    

# Example usage within the class itself:
api_url = "https://dummyjson.com" #https://dummyjson.com/products
json_dummy_instance = json_dummy(api_url)
# a = json_dummy_instance.get_categoryname_for_products_by_user("laptops")
# print(a)
a = json_dummy_instance.get_category_and_brand_info()
print(a)
# b = json_dummy_instance.get_data_for_products_by_userid(1)
# print(b)