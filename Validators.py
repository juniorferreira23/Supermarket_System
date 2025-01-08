from Model import Category, Product, Stock, Sale, SaleItem, Customer, Person, Employee, Supplier


def category_validator(category: Category) -> str|None:
    if type(category.name) != str:
        return 'Category input is not string'
    if len(category.name) < 4:
        return 'Category input less than 4 characters'
    return None

def stock_validator(stock: Stock):
    if type(stock.product.name) != str:
        return 'Name input is not string'
    elif len(stock.product.name) < 4:
        return 'Name input less than 4 caracters'
    
    validator = category_validator(stock.product.category)
    if validator:
        return validator
    
    if type(stock.product.price) != float:
        return 'Price input is not float'
    
    if type(stock.quantity) != int:
        return 'Quantity input is not int'
    
    return None


