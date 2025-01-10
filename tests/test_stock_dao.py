import unittest
from DAO import StockDao, Config, Dao, FileUtils
from Model import Product, Stock
import os

class TestStockDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Dao.create_table(Config.PATH_DB, Config.DB_STOCK)
        
    def setUp(self):
        with open(Config.DB_STOCK, 'w') as arq:
            arq.write('')
            self.dao = StockDao()
            
    def tearDown(self):
        if os.path.exists(Config.DB_STOCK):
            os.remove(Config.DB_STOCK)
            
    def test_save_stock(self):
        stock = Stock(Product('Espaguete', 'Massa', 2.49), 100)
        self.dao.save_stock(stock)
        
        data = FileUtils.read_file(Config.DB_STOCK)
        self.assertEqual(len(data), 1)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}',
            f'{stock.product.name}|{stock.product.category}|{stock.product.price}|{stock.quantity}'
        )
        
    def test_get_all_stock(self):
        stocks = [
            Stock(Product('Espaguete', 'Massa', 2.49), 100), 
            Stock(Product('Café', 'Bebida', 2.49), 100)
        ]
        for stock in stocks:
            self.dao.save_stock(stock)
        
        data = self.dao.get_all_stocks()
        self.assertEqual(len(data), 2)
        self.assertEqual(
            f'{data[0].product.name}|{data[0].product.category}|{data[0].product.price}|{data[0].quantity}',
            f'{stocks[0].product.name}|{stocks[0].product.category}|{stocks[0].product.price}|{stocks[0].quantity}'
        )
        self.assertEqual(
            f'{data[1].product.name}|{data[1].product.category}|{data[1].product.price}|{data[1].quantity}',
            f'{stocks[1].product.name}|{stocks[1].product.category}|{stocks[1].product.price}|{stocks[1].quantity}'
        )
        
    def test_find_by_product(self):
        stocks = [
            Stock(Product('Espaguete', 'Massa', 2.49), 100), 
            Stock(Product('Café', 'Bebida', 2.49), 100)
        ]
        for stock in stocks:
            self.dao.save_stock(stock)
        data = self.dao.find_by_product(stocks[0].product.name)
        self.assertEqual(data.product.name, stocks[0].product.name)
        
        
    def test_delete_stock(self):
        stocks = [
            Stock(Product('Espaguete', 'Massa', 2.49), 100), 
            Stock(Product('Café', 'Bebida', 2.49), 100)
        ]
        for stock in stocks:
            self.dao.save_stock(stock)
            
        self.dao.delete_stock(stocks[0].product.name)
        
        data = FileUtils.read_file(Config.DB_STOCK)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}',
            f'{stocks[1].product.name}|{stocks[1].product.category}|{stocks[1].product.price}|{stocks[1].quantity}'
        )
        
    def test_update_stock(self):
        stocks = [
            Stock(Product('Desinfetante', 'Limpeza', 2.49), 100), 
            Stock(Product('Café', 'Bebida', 2.49), 100)
        ]
        for stock in stocks:
            self.dao.save_stock(stock)
        
        new_stock = Stock(Product('Energético', 'Bebida', 2.49), 100)
        self.dao.update_stock('Desinfetante', new_stock)
        
        data = FileUtils.read_file(Config.DB_STOCK)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}',
            f'{new_stock.product.name}|{new_stock.product.category}|{new_stock.product.price}|{new_stock.quantity}'
        )
        
        
if __name__ == "__main__":
    unittest.main()