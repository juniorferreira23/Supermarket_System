from Model import Category, Product, Stock, Sale, SaleItem, Customer, Person, Employee, Supplier


def category_validator(category) -> str|None:
    if type(category) != str:
        return 'Category input is not string'
    if len(category) < 4:
        return 'Category input less than 4 characters'
    return None

def product_validator(name_product, category=None, price=None, quantity=None):
    if name_product:
        if type(name_product) != str:
            return 'Name input is not string'
        elif len(name_product) < 3:
            return 'Name input less than 4 caracters'
    
    if category:
        validator = category_validator(category)
        if validator:
            return validator
    
    if price:
        if type(price) != float:
            return 'Price input is not float'
    
    if quantity:
        if type(quantity) != int:
            return 'Quantity input is not int'
    
    return None

