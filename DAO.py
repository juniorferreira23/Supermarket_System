from Model import CategoryProduct, Product, Stock, Sale, SaleItem, Customer
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

    def save(self, category: CategoryProduct) -> None:
        with open(Config.DB_CATEGORY, 'a') as arq:
            arq.write(category.name + '\n')
        print('Category saved sucessfully')
        
    def get_all(self) -> list[CategoryProduct]:
        with open(Config.DB_CATEGORY, 'r') as arq:
            categories = arq.readlines()
        categories = list(map(lambda x: x.replace('\n', ''), categories))
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        return [CategoryProduct(category) for category in categories]
    
    def delete(self, name) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(filter(lambda x: x != name, categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')
        print('Category deleted sucessfully')
        
    def update(self, target_name: str, new_category: CategoryProduct) -> None:
        categories = FileUtils.read_file(Config.DB_CATEGORY)
        categories = list(map(lambda x: new_category.name if(x == target_name) else(x), categories))
                
        with open(Config.DB_CATEGORY, 'w') as arq:
            for category in categories:
                arq.write(category + '\n')
        print('Category update sucessfully')
        
# c1 = CategoryDao()
# c1.save(CategoryProduct('Cereal'))
# c1.save(CategoryProduct('Massa'))
# c1.save(CategoryProduct('Teste'))
# print(c1.get_all())
# c1.delete('Cereal')
# c1.update('Teste', CategoryProduct('Suco'))

class StockDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_STOCK)
        
    def save(self, stock: Stock) -> None:
        with open(Config.DB_STOCK, 'a') as arq:
            arq.write(
                stock.product.name + '|' +
                stock.product.category + '|' +
                str(stock.product.price) + '|' +
                str(stock.quantity)
            )
            arq.write('\n')
        print('Product saved in stock sucessfully')
        
    def get_all(self) -> list[Stock]:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        return list(map(lambda x: Stock(Product(x[0], x[1], x[2]), x[3]), stocks))
        
    def delete(self, name) -> None:
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
    
    def update(self, current_name, new_stock:Stock) -> None:
        stocks = FileUtils.read_file(Config.DB_STOCK)
        stocks = list(map(lambda x: [new_stock.product.name,
                                     new_stock.product.category,
                                     str(new_stock.product.price),
                                     str(new_stock.quantity)] if(x[0] == current_name) else(x), stocks))

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

# p = Product('Teste', 'Fruta', 6.59)
s1 = StockDao()
# s1.save(Stock(p, 100))
# print(s1.get_all())
s1.update('Teste', Stock(Product('Abacaxi', 'Fruta', 8.79), 100))
# s1.delete('Teste')

class SaleDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_SALE)
    
    def save(self, sale: Sale) -> None:
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
        
    def get_all(self) -> list[Sale]:
        sales = FileUtils.read_file(Config.DB_SALE)
        sales = list(map(lambda x: [x[0], literal_eval(x[1]), x[2], x[3], x[4], x[5]], sales))
        sales = list(map(lambda x: Sale(x[0], 
                                        list(map(lambda y: SaleItem(Product(y[0], y[1], float(y[2])), int(y[3])), x[1])),
                                        x[2],
                                        x[3],
                                        datetime.strptime(x[4], "%Y-%m-%d %H:%M:%S.%f"),
                                        float(x[5])), sales))
        return sales

# p1 = Product('Banana', 'Fruta', 2.59)
# p2 = Product('Morango', 'Fruta', 5.59)
# p3 = Product('Melancia', 'Fruta', 3.59)
# si1 = SaleItem(p1, 20)
# si2 = SaleItem(p2, 20)
# si3 = SaleItem(p3, 20)
# s1 = Sale('', [si1, si2, si3], 'Junior Ferreira', 'Larissa Alves', '')
# sdao = SaleDao()
# sdao.save(s1)
# print(sdao.get_all())


class CustomerDao(Dao):
    def __init__(self):
        super().create_table(Config.PATH_DB, Config.DB_CUSTOMER)
        
    def save(self, customer: Customer):
        with open(Config.DB_CUSTOMER, 'a') as arq:
            arq.write(
                customer.cpf + '|' +
                customer.name + '|' +
                customer.telephone + '|' +
                customer.email + '|' +
                customer.address
            )
            arq.write('\n')
    
    def get_all(self):
        customers = FileUtils.read_file()
        return customers

c1 = Customer(cpf='123', name='Junior Ferreira', telephone='8199999')
    
    