from Model import CategoryProduct, Product, Stock, Sale, SaleItem, Customer, Person
import os
from ast import literal_eval
from datetime import datetime

class Config:
    PATH_DB = 'db'
    DB_CATEGORY = os.path.join(PATH_DB, 'categories.txt')
    DB_STOCK = os.path.join(PATH_DB, 'stocks.txt')
    DB_SALE = os.path.join(PATH_DB, 'sales.txt')
    DB_CUSTOMER = os.path.join(PATH_DB, 'customers.txt')


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

    def save_category(self, category: CategoryProduct) -> None:
        with open(Config.DB_CATEGORY, 'a') as arq:
            arq.write(category.name + '\n')
        print('Category saved sucessfully')
        
    def get_all_categories(self) -> list[CategoryProduct]:
        with open(Config.DB_CATEGORY, 'r') as arq:
            categories = arq.readlines()
        categories = list(map(lambda x: x.replace('\n', ''), categories))
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        return [CategoryProduct(category) for category in categories]
    
    def delete_category(self, name) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(filter(lambda x: x != name, categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')        
        print('Category deleted sucessfully')
        
    def update_category(self, target_name: str, new_category: CategoryProduct) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(map(lambda x: new_category.name if(x == target_name) else(x), categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')
        print('Category update sucessfully')
        

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
        print('Product saved in stock sucessfully')
        
    def get_all_stocks(self) -> list[Stock]:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        return list(map(lambda x: Stock(Product(x[0], x[1], x[2]), x[3]), stocks))
        
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
        print('Product deleted in stock sucessfully')
    
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
        print('Product updated in stock sucessfully')


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
        print('Sale saved sucessfully')
        
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
            print('Customer saved sucessfully')
    
    def get_all_customer(self) -> list[Customer]:
        customers = FileUtils.read_file(Config.DB_CUSTOMER)
        return list(map(lambda x: Customer(Person(x[0], x[1], x[2]), x[3], x[4]), customers))
    
    def delete_customer(self, cpf):
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
        print('Customer deleted sucessfully')

    def update_customer(self, target_cpf, new_customer: Customer):
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
        print('Customer updated sucessfully')
        
        
    
    