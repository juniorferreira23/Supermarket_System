import re

def name_product_validator(product: str) -> str|None:
    if type(product) != str:
            return 'Name input is not string'
    elif len(product) < 3:
        return 'Name input less than 3 caracters' 
    

def name_validator(name: str) -> str|None:
    if type(name) != str:
            return 'Invalid name type'
    elif len(name) < 8:
        return 'Invalid name'
    elif '' not in name:
        return 'First and last name required'


def category_validator(category: str) -> str|None:
    if type(category) != str:
        return 'Category input is not string'
    if len(category) < 4:
        return 'Category input less than 4 characters'


def telephone_validator(telephone: str) -> str|None:
    if type(telephone) != str:
        return 'Invalid telephone type'
    if len(telephone) != 11:
        return 'Invalid telephone'


def clt_validator(clt: str) -> str|None:
    if type(clt) != str:
        return 'Invalid clt type'
    elif len(clt) != 11:
        return 'Invalid clt'
    

def cpf_validator(cpf: str) -> str|None:
    if type(cpf) != str:
        return 'Invalid CPF type'
    elif len(cpf) != 11:
        return 'Invalid CPF'


def cnpj_validator(cnpj: str) -> str|None:
    if type(cnpj) != str:
        return 'Invalid CNPJ type'
    elif len(cnpj) != 14:
        return 'Invalid CNPJ'
    

def email_validator(email:str) -> bool:
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None


def product_validator(name_product:str, category:str, price:float, quantity:int) -> str|None:
    validator = name_product_validator(name_product)
    if validator:
        return validator
    
    validator = category_validator(category)
    if validator:
        return validator
    
    if type(price) != float:
        return 'Price input is not float'
    
    if type(quantity) != int:
        return 'Quantity input is not int'
        

def sale_validator(name_product: str, quantity: int) -> str|None:
    validator = name_product_validator(name_product)
    if validator:
        return validator
    
    if type(quantity) != int:
        return 'Quantity input is not int'
    
    

def person_validator(cpf:str, name:str, telephone:str) -> str|None:
    validator = cpf_validator(cpf)
    if validator:
        return validator
    
    validator = name_validator(name)
    if validator:
        return validator
    
    validator = telephone_validator(telephone)
    if validator:
        return validator
        

def employee_validator(cpf:str, name:str, telephone:str, clt:str, postion:str) -> str|None:
    validator = person_validator(cpf, name, telephone)
    if validator:
        return validator
    
    validator = clt_validator(clt)
    if validator:
        return validator
    
    if type(postion) != str:
        return 'Invalid position type'



def customer_validator(cpf:str, name:str, telephone:str, email:str, address:str) -> str|None:
    validator = person_validator(cpf, name, telephone)
    if validator:
        return validator

    if type(email) != str:
        return 'Invalid email type'
    elif not email_validator(email):
        return 'Invalid email'
    
    if type(address) != str:
        return 'Invalid address type'


def supplier_validator(cnpj: str, company_name:str, category:str, telephone:str) -> str|None:
    validator = cnpj_validator(cnpj)
    if validator:
        return validator
    
    if type(company_name) != str:
        return 'Invalid Razão social type'
    
    validator = category_validator(category)
    if validator:
        return validator
    
    validator = telephone_validator(telephone)
    if validator:
        return validator


def view_float_validator(prompt):
    while True:
        try:
            value = input(prompt)
            if not value:
                return None
            return float(value)
        except ValueError as e:
            print(f'Invalid input: {e}. Please enter a valid number float.')


def view_int_validator(prompt):
    while True:
        try:
            value = input(prompt)
            if not value:
                return None
            return int(value)
        except ValueError as e:
            print(f'Invalid input: {e}. Please enter a valid number.')
