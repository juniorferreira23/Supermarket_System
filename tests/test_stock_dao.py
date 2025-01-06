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
            stocks[0]
        )
        
        
        
if __name__ == "__main__":
    unittest.main()