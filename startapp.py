from productinfo import Product  # all properties of products
from productserviceimpl import ProductServicesImpl  # all services.. methods -- business logic

services = ProductServicesImpl()

while True:

    try:
        pid = int(input('Enter Product Id : '))
        name = input('Enter Product Name : ')
        qty = int(input('Enter Product Qty : '))
        price = float(input('Enter Product Price : '))
        vendor = input('Enter Product Vendor : ')
        category = input('Enter Product Category : ')
    except ValueError as v:
        print('Invalid Input...re-enter values...!')
    else:   #SAFE CODE
        p1 = Product(prid=pid,prnm=name,prc=price,ven=vendor,categ=category,qty=qty)
        services.add_product(p1)

    choice = input('Do you want to Add more Products : No/N')
    if choice.lower() in ['n','no']:
        break

print('--------------------------')
print(services.list_products())

'''
# p1 = Product(prid=101,prnm='Mobile',prc=37673.34,ven='Motorola',categ="ET",qty=23)  #p1 -- product--> who defined this
# print(p1)

'''

