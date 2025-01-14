from Model import Category, Product, Stock, Sale, SaleItem, Customer, Person, Employee, Supplier
import os
from ast import literal_eval
from datetime import datetime

class Config:
    PATH_DB = 'db'
    DB_CATEGORY = os.path.join(PATH_DB, 'categories.txt')
    DB_STOCK = os.path.join(PATH_DB, 'stocks.txt')
    DB_SALE = os.path.join(PATH_DB, 'sales.txt')
    DB_CUSTOMER = os.path.join(PATH_DB, 'customers.txt')
    DB_EMPLOYEE = os.path.join(PATH_DB, 'employees.txt')
    DB_SUPPLIER = os.path.join(PATH_DB, 'suppliers.txt')


class FileUtils:
    @staticmethod
    def read_file(path: str) -> list[str]:
        with open(path, 'r') as arq:
            return [line.replace('\n', '').split('|') if('|' in line) else(line.replace('\n', '')) for line in arq.readlines()]
             
        
class Dao:
    @staticmethod
    def create_table(path_db, path_table):
        if not os.path.exists(path_db):
            os.makedirs(path_db)
            print(f'database path ({path_db}) created sucessfully')
        if not os.path.exists(path_table):
            with open(path_table, 'w') as arq:
                arq.write('')
            print(f'table path ({path_table}) created sucessfully')


class CategoryDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_CATEGORY)
        super().create_table(Config.PATH_DB, Config.DB_STOCK)
        super().create_table(Config.PATH_DB, Config.DB_SUPPLIER)

    def save_category(self, category: Category) -> None:
        with open(Config.DB_CATEGORY, 'a') as arq:
            arq.write(category.name + '\n')
        
    def get_all_categories(self) -> list[Category]:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        return [Category(category) for category in categories]
    
    def find_by_name(self, name) -> Category:
        categories = FileUtils.read_file(Config.DB_CATEGORY)  
        exist_category = any(category == name for category in categories)
        if not exist_category:
            return None
        category = list(filter(lambda x: x == name, categories))
        return Category(category[0])
    
    def delete_category(self, name) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(filter(lambda x: x != name, categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')
        
        stocks = FileUtils.read_file(Config.DB_STOCK)
        stocks = list(map(lambda x: [x[0], 'Empty', x[2], x[3]] if(x[1] == name) else(x), stocks))
        with open(Config.DB_STOCK, 'w') as arq:
            for stock in stocks:
                arq.write(
                    stock[0] + '|' +
                    stock[1] + '|' +
                    stock[2] + '|' +
                    stock[3]
                )
                arq.write('\n')
        
        suppliers = FileUtils.read_file(Config.DB_SUPPLIER)
        suppliers = list(map(lambda x: [x[0], x[1], 'Empty'] if(x[2] == name) else(x), suppliers))
        with open(Config.DB_STOCK, 'w') as arq:
            for stock in stocks:
                arq.write(
                    stock[0] + '|' +
                    stock[1] + '|' +
                    stock[2]
                )
                arq.write('\n')
        
    def update_category(self, target_name: str, new_category: Category) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(map(lambda x: new_category.name if(x == target_name) else(x), categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')  
                
        stocks = FileUtils.read_file(Config.DB_STOCK)
        stocks = list(map(lambda x: [x[0], new_category, x[2], x[3]] if(x[1] == target_name) else(x), stocks))
        with open(Config.DB_STOCK, 'w') as arq:
            for stock in stocks:
                arq.write(
                    stock[0] + '|' +
                    stock[1] + '|' +
                    stock[2] + '|' +
                    stock[3]
                )
                arq.write('\n')


class StockDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_STOCK)
        
    def save_stock(self, stock: Stock) -> None:
        with open(Config.DB_STOCK, 'a') as arq:
            arq.write(
                stock.product.name + '|' +
                stock.product.category + '|' +
                str(stock.product.price) + '|' +
                str(stock.quantity)
            )
            arq.write('\n')
        
    def get_all_stocks(self) -> list[Stock]:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        return list(map(lambda x: Stock(Product(x[0], x[1], float(x[2])), int(x[3])), stocks))
    
    def find_by_product(self, product: str) -> Stock|None:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        exist_product = any(stock[0] == product for stock in stocks)
        if not exist_product:
            return None
        stock = list(filter(lambda x: x[0] == product, stocks))[0]
        return Stock(Product(stock[0], stock[1], float(stock[2])), int(stock[3]))
        
    def delete_stock(self, name) -> None:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        stocks = list(filter(lambda x: x[0] != name, stocks))
        
        with open(Config.DB_STOCK, 'w') as arq:
            for stock in stocks:
                arq.write(
                    stock[0] + '|' +
                    stock[1] + '|' +
                    stock[2] + '|' +
                    stock[3]
                )
                arq.write('\n')
    
    def update_stock(self, target_name, new_stock:Stock) -> None:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        stocks = list(map(lambda x: [new_stock.product.name,
                                     new_stock.product.category,
                                     str(new_stock.product.price),
                                     str(new_stock.quantity)] if(x[0] == target_name) else(x), stocks))
        with open(Config.DB_STOCK, 'w') as arq:
            for stock in stocks:
                arq.write(
                    stock[0] + '|' +
                    stock[1] + '|' +
                    stock[2] + '|' +
                    stock[3]
                )
                arq.write('\n')

class SaleDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_SALE)
    
    def save_sale(self, sale: Sale) -> None:
        with open(Config.DB_SALE, 'a') as arq:
            arq.write(
                sale.registration + '|' +
                str([ [saleItem.product.name, saleItem.product.category, str(saleItem.product.price), str(saleItem.quantity)] for saleItem in sale.sold_products]) + '|' +
                sale.operator + '|' +
                sale.customer + '|' +
                str(sale.date) + '|' +
                str(sale.total)
            )
            arq.write('\n')
        
    def get_all_sales(self) -> list[Sale]:
        sales = FileUtils.read_file(Config.DB_SALE)
        sales = list(map(lambda x: [x[0], literal_eval(x[1]), x[2], x[3], x[4], x[5]], sales))
        sales = list(map(lambda x: Sale(x[0], 
                                        list(map(lambda y: SaleItem(Product(y[0], y[1], float(y[2])), int(y[3])), x[1])),
                                        x[2],
                                        x[3],
                                        datetime.strptime(x[4], "%Y-%m-%d %H:%M:%S.%f"),
                                        float(x[5])), sales))
        return sales


class CustomerDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_CUSTOMER)
        
    def save_customer(self, customer: Customer) -> None:
        with open(Config.DB_CUSTOMER, 'a') as arq:
            arq.write(
                customer.cpf + '|' +
                customer.name + '|' +
                customer.telephone + '|' +
                customer.email + '|' +
                customer.address
            )
            arq.write('\n')
    
    def get_all_customer(self) -> list[Customer]:
        customers = FileUtils.read_file(Config.DB_CUSTOMER)
        return list(map(lambda x: Customer(Person(x[0], x[1], x[2]), x[3], x[4]), customers))
    
    def find_by_cpf(self, cpf) -> Customer:
        customers = FileUtils.read_file(Config.DB_CUSTOMER)
        exist_customer = any(customer[0] == cpf for customer in customers)
        if not exist_customer:
            return None
        customer = list(filter(lambda x: x[0] == cpf, customers))[0]
        return Customer(Person(customer[0], customer[1], customer[2]), customer[3], customer[4])
    
    def delete_customer(self, cpf) -> None:
        customers = FileUtils.read_file(Config.DB_CUSTOMER)
        customers = list(filter(lambda x: x[0] != cpf, customers))
        
        with open(Config.DB_CUSTOMER, 'w') as arq:
            for customer in customers:
                arq.write(
                    customer[0] + '|' +
                    customer[1] + '|' +
                    customer[2] + '|' +
                    customer[3] + '|' +
                    customer[4]
                )
                arq.write('\n')

    def update_customer(self, target_cpf, new_customer: Customer) -> None:
        customers = FileUtils.read_file(Config.DB_CUSTOMER)
        customers = list(map(lambda x:
            [
                new_customer.cpf,
                new_customer.name,
                new_customer.telephone,
                new_customer.email,
                new_customer.address
            ]
            if(x[0] == target_cpf) else(x), customers
        ))
        
        with open(Config.DB_CUSTOMER, 'w') as arq:
            for customer in customers:
                arq.write(
                    customer[0] + '|' +
                    customer[1] + '|' +
                    customer[2] + '|' +
                    customer[3] + '|' +
                    customer[4]
                )
                arq.write('\n')        
        
class EmployeeDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB,Config.DB_EMPLOYEE)
        
    def save_employee(self, employee: Employee) -> None:        
        with open(Config.DB_EMPLOYEE, 'a') as arq:
            arq.write(
                employee.cpf + "|" +
                employee.name + "|" +
                employee.telephone + "|" +
                employee.clt + "|" +
                employee.position 
            )
            arq.write('\n')
        
    def get_all_employee(self) -> list[Employee]:
        employees = FileUtils.read_file(Config.DB_EMPLOYEE)
        return list(map(lambda x: Employee(Person(x[0], x[1], x[2]), x[3], x[4]), employees))
    
    def find_by_clt(self, clt) -> Employee:
        employees = FileUtils.read_file(Config.DB_EMPLOYEE)
        exist_employee = any(employee[3] == clt for employee in employees)
        if not exist_employee:
            return None
        employee = list(filter(lambda x: x[3 == clt], employees))[0]
        return Employee(Person(employee[0], employee[1], employee[2]), employee[3], employee[4])
    
    def delete_employee(self, clt) -> None:
        employees = FileUtils.read_file(Config.DB_EMPLOYEE)
        employees = list(filter(lambda x: x[3] != clt, employees))
        
        with open(Config.DB_EMPLOYEE, 'w') as arq:
            for employee in employees:
                arq.write(
                    employee[0] + "|" +
                    employee[1] + "|" +
                    employee[2] + "|" +
                    employee[3] + "|" +
                    employee[4] 
                )
                arq.write('\n')
    
    def update_employee(self, clt, new_employee: Employee) -> None:
        employees = FileUtils.read_file(Config.DB_EMPLOYEE)
        employees = list(map(lambda x: [new_employee.cpf,
                                        new_employee.name,
                                        new_employee.telephone,
                                        new_employee.clt,
                                        new_employee.position] if(x[3] == clt) else(x), employees))
        
        with open(Config.DB_EMPLOYEE, 'w') as arq:
            for employee in employees:
                arq.write(
                    employee[0] + "|" +
                    employee[1] + "|" +
                    employee[2] + "|" +
                    employee[3] + "|" +
                    employee[4] 
                )
                arq.write('\n')

class SupplierDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_SUPPLIER)
        
    def save_supplier(self, supplier: Supplier) -> None:
        with open(Config.DB_SUPPLIER, 'a') as arq:
            arq.write(
                supplier.cnpj + '|' +
                supplier.razao_social + '|' + 
                supplier.category.name + '|' +
                supplier.telephone
            )
            arq.write('\n')
            
    def get_all_supplier(self) -> list[Supplier]:
        suppliers = FileUtils.read_file(Config.DB_SUPPLIER)
        return list(map(lambda x: Supplier(x[0], x[1], x[2], x[3]), suppliers))
    
    def delete_supplier(self, cnpj) -> None:
        suppliers = FileUtils.read_file(Config.DB_SUPPLIER)
        supplier = list(filter(lambda x: x[0] != cnpj, suppliers))
        
        with open(Config.DB_SUPPLIER, 'w') as arq:
            for supplier in suppliers:
                arq.write(
                    supplier[0] + '|' +
                    supplier[1] + '|' + 
                    supplier[2] + '|' +
                    supplier[3]
                )
                arq.write('\n')
        
    def update_supplier(self, cnpj, new_supplier: Supplier) -> None:
        suppliers = FileUtils.read_file(Config.DB_SUPPLIER)
        supplier = list(map(lambda x: [new_supplier.cnpj,
                                       new_supplier.razao_social,
                                       new_supplier.category,
                                       new_supplier.telephone] if(x[0] == cnpj) else(x), suppliers))
        
        with open(Config.DB_SUPPLIER, 'w') as arq:
            for supplier in suppliers:
                arq.write(
                    supplier[0] + '|' +
                    supplier[1] + '|' + 
                    supplier[2] + '|' + 
                    supplier[3]
                )
                arq.write('\n')    
            