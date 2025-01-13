from Model import Category, Product, Stock, Sale, SaleItem, Customer, Person, Employee, Supplier
import re


def category_validator(category) -> str|None:
    if type(category) != str:
        return 'Category input is not string'
    if len(category) < 4:
        return 'Category input less than 4 characters'
    return None

def product_validator(name_product, category=None, price=None, quantity=None) -> str|None:
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


def person_validator(cpf, name, telephone=None) -> str|None:
    if type(cpf) != str:
        return 'Invalid CPF type'
    elif len(cpf) != 11:
        return 'Invalid CPF'
    
    if type(name) != str:
        return 'Invalid name type'
    elif len(name) < 8:
        return 'Invalid name'
    elif '' not in name:
        return 'First and last name required'

    if telephone:
        if type(telephone) != str:
            return 'Invalid telephone type'
        if len(telephone) != 11:
            return 'Invalid telephone'

def employee_validator(cpf=None, name=None, telephone=None, clt=None, postion=None) -> str|None:
    if cpf and name:
        validator = person_validator(cpf, name, telephone)
        if validator:
            return validator
    if clt:
        if type(clt) != str:
            return 'Invalid clt type'
        elif len(clt) != 11:
            return 'Invalid clt'
    if postion:
        if type(postion) != str:
            return 'Invalid position type'
    return None


def customer_validator(cpf, name, telephone, email=None, address=None):
    def email_validator(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def telephone_validator(telephone):
        regex = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        return re.match(regex, telephone) is not None
    
    validator = person_validator(cpf, name, telephone)
    if validator:
        return validator
    if email:
        if type(email) != str:
            return 'Invalid email type'
        elif not email_validator(email):
            return 'Invalid email'
    if type(address) != str:
        return 'Invalid address type'
    
    return None

