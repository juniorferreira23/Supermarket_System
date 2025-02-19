import unittest
from DAO import CategoryDao, Config, Dao, FileUtils
from Model import Category
import os

class TestCategoryDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Dao.create_table(Config.PATH_DB, Config.DB_CATEGORY)
        Dao.create_table(Config.PATH_DB, Config.DB_STOCK)
        Dao.create_table(Config.PATH_DB, Config.DB_SUPPLIER)
        
    def setUp(self):
        with open(Config.DB_CATEGORY, 'w') as arq:
            arq.write('')
            self.dao = CategoryDao()
            
    def tearDown(self):
        if os.path.exists(Config.DB_CATEGORY):
            os.remove(Config.DB_CATEGORY)
            
    def test_save_category(self):
        category = Category('Bebida')
        self.dao.save_category(category)
        
        data = FileUtils.read_file(Config.DB_CATEGORY)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].strip(), category.name)
    
    def test_get_all_categories(self):
        categories = [Category('Fruta'), Category('Legume')]
        for category in categories:
            self.dao.save_category(category)
            
        retrieved = self.dao.get_all_categories()
        self.assertEqual(len(retrieved), 2)
        self.assertEqual(retrieved[0].name, categories[0].name)
        self.assertEqual(retrieved[1].name, categories[1].name)
        
    def test_find_by_name_category(self):
        categories = [Category('Fruta'), Category('Legume')]
        for category in categories:
            self.dao.save_category(category)
            
        retrieved = self.dao.find_by_name(categories[0].name)
        self.assertEqual(retrieved.name, categories[0].name)
        
    def test_delete_category(self):
        categories = [Category('Carne'), Category('Massa')]
        for category in categories:
            self.dao.save_category(category)
        
        self.dao.delete_category(categories[0].name)
        
        data = FileUtils.read_file(Config.DB_CATEGORY)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].strip(), categories[1].name)
        
    def test_update_category(self):
        categories = [Category('Grãos'), Category('Frios')]
        for category in categories:
            self.dao.save_category(category)
        
        new_category = Category('Laticínios')
        self.dao.update_category('Frios', new_category)
        
        data = FileUtils.read_file(Config.DB_CATEGORY)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0].strip(), categories[0].name)
        self.assertEqual(data[1].strip(), new_category.name)
            
if __name__ == "__main__":
    unittest.main()