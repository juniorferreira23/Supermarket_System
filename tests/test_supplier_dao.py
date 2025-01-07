import unittest
from DAO import SupplierDao, Config, Dao, FileUtils
from Model import Category, Supplier
import os

class TestSupplierDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Dao.create_table(Config.PATH_DB, Config.DB_SUPPLIER)
        
    def setUp(self):
        with open(Config.DB_SUPPLIER, 'w') as arq:
            arq.write('')
            self.dao = SupplierDao()
            
    def tearDown(self):
        if os.path.exists(Config.DB_SUPPLIER):
            os.remove(Config.DB_SUPPLIER)
            
    def test_save_supplier(self):
        supplier = Supplier('123123123', 'razao social ltda', Category('Carne'))
        
        self.dao.save_supplier(supplier)
        
        data = FileUtils.read_file(Config.DB_SUPPLIER)
        self.assertEqual(len(data), 1)
        