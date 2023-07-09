
class Product:
    '''This Product class is designed to hold the information for product type...!'''   #doctstring

    def __init__(self,prid,prnm,prc,ven,categ,qty):
        '''This is the construtor to initialiaze object properties'''
        self.product_id = prid
        self.product_name = prnm
        self.product_price = prc
        self.product_vendor = ven
        self.product_category = categ
        self.product_qty = qty

    def __str__(self):          #this is product class object represention -->callback (automatically call hote)
        '''This methods represents an object properties'''
        return f'''\n {self.__dict__}'''

    def __repr__(self):
        '''In case list of,set of tuple of,dict of products ale tr '''
        return str(self)

    # def display_prod_properties(self):
    #      return f'''{self.__dict__}'''

# num = 10        # int --> int class
#
# val = []        # type --> list --> class --> list


# p1 = Product(prid=101,prnm='Mobile',prc=37673.34,ven='Motorola',categ="ET",qty=23)  #p1 -- product--> who defined this
# print(p1)
# print('---------------------------------')
# p2 = Product(prid=102,prnm='Laptop',prc=57673.34,ven='Dell',categ="ET",qty=22)
# print(p2)
#
# products_list = [p1,p2]
# print(products_list)