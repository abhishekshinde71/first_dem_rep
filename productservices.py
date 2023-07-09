
from abc import ABC,abstractmethod

class ProductServices(ABC):   #RBI      # WHAT services #--> RBI --> kay ahe kay asel..  we cannot instantiate an abstract class
    '''This is abstract class, which tells about which services we are going to offer to the end user'''
    @abstractmethod         # this is method is mandatory for child to provide implementation
    def add_product(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass

    @abstractmethod
    def update_product(self):
        pass

    @abstractmethod
    def search_for_a_product(self):
        pass

    @abstractmethod
    def list_products(self):
        pass

    @abstractmethod
    def products_in_price_range(self):
        pass

    @abstractmethod
    def product_with_aggregate_functions(self):     #min,max,avg,sum,count etc...
        pass