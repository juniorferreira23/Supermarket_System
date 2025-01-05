from datetime import datetime
from uuid import uuid4

class CategoryProduct:
    def __init__(self, name: str):
        self.name = name
        

class Product:
    def __init__(self, name: str, category: CategoryProduct, price: float):
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
    def __init__(self, registration,  sold_products: list[SaleItem], operator, customer='Not Registered',  date=None, total=None):
        self.registration = registration or str(uuid4())
        self.sold_products = sold_products
        self.operator = operator
        self.customer = customer
        self.date = date or datetime.now()
        self.total = total or self.calculate_total()
        
    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.sold_products)
        return round(total, 2)


class Person:
    def __init__(self, cpf, name, telephone):
        self.cpf = cpf
        self.name = name
        self.telephone = telephone
    

class Customer(Person):
    def __init__(self, cpf: str, name: str, telephone: str, email='', address=''):
        super().__init__(cpf, name, telephone)
        self.email = email
        self.address = address
      
           
class Employee(Person):
    def __init__(self, clt: str, position: str, name: str, cpf: str, telephone: str):
        super().__init__(cpf, name, telephone)
        self.clt = clt
        self.position = position