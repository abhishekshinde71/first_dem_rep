from productinfo import Product
from productservices import ProductServices


class ProductServicesImpl(ProductServices):  #ProductServicesImpl --HDFC,SBI,ICICI
    PRODUCT_INVENTORY = []
      # list ---> class level variable    --> Using class name

    def add_product(self,item):  # encapsulated values --> PRODUCT      # INSTANCE METHOD
        ProductServicesImpl.PRODUCT_INVENTORY.append(item)
        print('Product Successfully Added...!')

    def delete_product(self,pid):       # which product to be deleted --> ID
        pass

    def update_product(self,pid,item):  # pid, PRODUCT
        pass

    def search_for_a_product(self,criteria,value):      # search_for_a_product('ACC',"77777")
        pass

    def list_products(self,kashane=None,tyachivalue=None):
        return ProductServicesImpl.PRODUCT_INVENTORY

    def products_in_price_range(self,startprice,endprice):
        pass

    def product_with_aggregate_functions(self,value="COUNT"):  # min,max,avg,sum,count etc...
        pass



#product_with_aggregate_functions() --> num of products
#product_with_aggregate_functions("AVG") -->
