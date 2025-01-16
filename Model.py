from datetime import datetime
from uuid import uuid4

class Category:
    def __init__(self, name: str):
        self.name = name
        

class Product:
    def __init__(self, name: str, category: Category, price: float):
        self.name = name
        self.category = category
        self.price = price
        

class Stock:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    

class SaleItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


class Sale:
    def __init__(self, sold_products: list[SaleItem], operator, total, registration=None, customer='Not Registered',  date=None):
        self.registration = registration or str(uuid4())
        self.sold_products = sold_products
        self.operator = operator
        self.customer = customer
        self.date = date or datetime.now().strftime('%d/%m/%Y')
        self.total = total


class Person:
    def __init__(self, cpf: str, name: str, telephone: str):
        self.cpf = cpf
        self.name = name
        self.telephone = telephone
    

class Customer(Person):
    def __init__(self, person: Person , email='', address=''):
        super().__init__(person.cpf, person.name, person.telephone)
        self.email = email
        self.address = address
      
           
class Employee(Person):
    def __init__(self, person: Person, clt: str, position: str):
        super().__init__(person.cpf, person.name, person.telephone)
        self.clt = clt
        self.position = position
        

class Supplier:
    def __init__(self, cnpj: str, company_name: str, category: Category, telephone: str):
        self.cnpj = cnpj
        self.company_name = company_name
        self.category = category
        self.telephone = telephone