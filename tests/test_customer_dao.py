import unittest
from DAO import CustomerDao, Config, Dao, FileUtils
from Model import Person, Customer
import os

class TestCustomerDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Dao.create_table(Config.PATH_DB, Config.DB_CUSTOMER)
        
    def setUp(self):
        with open(Config.DB_CUSTOMER, 'w') as arq:
            arq.write('')
            self.dao = CustomerDao()
            
    def tearDown(self):
        if os.path.exists(Config.DB_CUSTOMER):
            os.remove(Config.DB_CUSTOMER)
            
    def test_save_customer(self):
        person = Person('12312312312', 'junior ferreira', '81988887777')
        customer = Customer(person, 'junior@email.com', 'Av. Major')
        self.dao.save_customer(customer)
        
        data = FileUtils.read_file(Config.DB_CUSTOMER)
        self.assertEqual(len(data), 1)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}|{data[0][4]}',
            f'{customer.cpf}|{customer.name}|{customer.telephone}|{customer.email}|{customer.address}'
        )
        
    def test_get_all_customer(self):
        customers = [
            Customer(Person('12312312312', 'junior ferreira', '81988887777'), 'junior@email.com', 'Av. Major'),
            Customer(Person('45645645656', 'joao ferreira', '81988886666'), 'joao@email.com', 'Av. Almirante')
        ]
        for customer in customers:
            self.dao.save_customer(customer)
            
        data = self.dao.get_all_customer()
        self.assertEqual(len(data), 2)
        self.assertEqual(
            f'{data[0].cpf}|{data[0].name}|{data[0].telephone}|{data[0].email}|{data[0].address}',
            f'{customers[0].cpf}|{customers[0].name}|{customers[0].telephone}|{customers[0].email}|{customers[0].address}'
        )
        self.assertEqual(
            f'{data[1].cpf}|{data[1].name}|{data[1].telephone}|{data[1].email}|{data[1].address}',
            f'{customers[1].cpf}|{customers[1].name}|{customers[1].telephone}|{customers[1].email}|{customers[1].address}',
        )
        
    def test_find_by_cpf_customer(self):
        customers = [
            Customer(Person('12312312312', 'junior ferreira', '81988887777'), 'junior@email.com', 'Av. Major'),
            Customer(Person('45645645656', 'joao ferreira', '81988886666'), 'joao@email.com', 'Av. Almirante')
        ]
        for customer in customers:
            self.dao.save_customer(customer)
            
        data = self.dao.find_by_cpf(customers[0].cpf)
        self.assertEqual(
            f'{data.cpf}|{data.name}|{data.telephone}|{data.email}|{data.address}',
            f'{customers[0].cpf}|{customers[0].name}|{customers[0].telephone}|{customers[0].email}|{customers[0].address}'
        )

        
    def test_delete_customer(self):
        customers = [
            Customer(Person('12312312312', 'junior ferreira', '81988887777'), 'junior@email.com', 'Av. Major'),
            Customer(Person('45645645656', 'joao ferreira', '81988886666'), 'joao@email.com', 'Av. Almirante')
        ]
        for customer in customers:
            self.dao.save_customer(customer)
            
        self.dao.delete_customer(customers[0].cpf)
        
        data = FileUtils.read_file(Config.DB_CUSTOMER)
        self.assertEqual(len(data), 1)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}|{data[0][4]}',
            f'{customers[1].cpf}|{customers[1].name}|{customers[1].telephone}|{customers[1].email}|{customers[1].address}'
        )
        
    def test_update_customer(self):
        customers = [
            Customer(Person('12312312312', 'junior ferreira', '81988887777'), 'junior@email.com', 'Av. Major'),
            Customer(Person('45645645656', 'joao ferreira', '81988886666'), 'joao@email.com', 'Av. Almirante')
        ]
        for customer in customers:
            self.dao.save_customer(customer)
        
        new_customer = Customer(Person('78978978978','larissa alves', '81988885555'), 'larissa@email.com', 'Av. Major')
        self.dao.update_customer(customers[1].cpf, new_customer)
        
        data = FileUtils.read_file(Config.DB_CUSTOMER)
        self.assertEqual(len(data), 2)
        self.assertEqual(
            f'{data[1][0]}|{data[1][1]}|{data[1][2]}|{data[1][3]}|{data[1][4]}',
            f'{new_customer.cpf}|{new_customer.name}|{new_customer.telephone}|{new_customer.email}|{new_customer.address}'
        )
    

if __name__ == "__main__":
    unittest.main()