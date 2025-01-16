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
        supplier = Supplier('123123123', 'razao social ltda', Category('Carne'), '81966664444')
        
        self.dao.save_supplier(supplier)
        
        data = FileUtils.read_file(Config.DB_SUPPLIER)
        self.assertEqual(len(data), 1)
    
    def test_get_all_supplier(self):
        suppliers = [
            Supplier('123123123', 'razao social ltda', Category('Carne'), '81988884444'),
            Supplier('123123145', 'teste ltda', Category('Limpeza'), '81977776666')
        ]
        
        for supplier in suppliers:
            self.dao.save_supplier(supplier)
            
        data = self.dao.get_all_supplier()
        self.assertEqual(
            f'{suppliers[0].cnpj}|{suppliers[0].company_name}|{suppliers[0].category.name}',
            f'{data[0].cnpj}|{data[0].company_name}|{data[0].category}'
        )
        self.assertEqual(
            f'{suppliers[1].cnpj}|{suppliers[1].company_name}|{suppliers[1].category.name}',
            f'{data[1].cnpj}|{data[1].company_name}|{data[1].category}'
        )
        
    def test_find_by_cnpj_supplier(self):
        suppliers = [
            Supplier('123123123', 'razao social ltda', Category('Carne'), '81988884444'),
            Supplier('123123145', 'teste ltda', Category('Limpeza'), '81977776666')
        ]
        
        for supplier in suppliers:
            self.dao.save_supplier(supplier)
            
        data = self.dao.find_by_cnpj(suppliers[0].cnpj)
        self.assertEqual(
            f'{suppliers[0].cnpj}|{suppliers[0].company_name}|{suppliers[0].category.name}',
            f'{data.cnpj}|{data.company_name}|{data.category}'
        )

        
    def test_delete_supplier(self):
        suppliers = [
            Supplier('123123123', 'razao social ltda', Category('Carne'), '81988884444'),
            Supplier('123123145', 'teste ltda', Category('Limpeza'), '81977776666')
        ]
        
        for supplier in suppliers:
            self.dao.save_supplier(supplier)
            
        self.dao.delete_supplier(suppliers[0].cnpj)
        
        data = FileUtils().read_file(Config.DB_SUPPLIER)
        self.assertEqual(
            f'{suppliers[1].cnpj}|{suppliers[1].company_name}|{suppliers[1].category.name}',
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}'
        )