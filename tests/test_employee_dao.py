import unittest
from DAO import EmployeeDao, Config, Dao, FileUtils
from Model import Person, Employee
import os

class TestEmployeeDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Dao.create_table(Config.PATH_DB, Config.DB_EMPLOYEE)
        
    def setUp(self):
        with open(Config.DB_EMPLOYEE, 'w') as arq:
            arq.write('')
            self.dao = EmployeeDao()
            
    def tearDown(self):
        if os.path.exists(Config.DB_EMPLOYEE):
            os.remove(Config.DB_EMPLOYEE)
            
    def test_save_employee(self):
        employee = Employee(Person('12312312312', 'Junior ferreira', '81988884444'), '123', 'teste')
        
        self.dao.save_employee(employee)
        
        data = FileUtils.read_file(Config.DB_EMPLOYEE)
        self.assertEqual(len(data), 1)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}|{data[0][4]}',
            f'{employee.cpf}|{employee.name}|{employee.telephone}|{employee.clt}|{employee.position}'
        )
    
    def test_get_all_employee(self):
        employees = [
            Employee(Person('12312312312', 'Junior ferreira', '81988884444'), '123', 'teste'),
            Employee(Person('12312345621', 'lucas ferreira', '81988883333'), '456', 'teste')
        ]
        
        for employee in employees:
            self.dao.save_employee(employee)
            
        data = self.dao.get_all_employee()
        self.assertEqual(employees[0].name, data[0].name)
        self.assertEqual(
            f'{data[0].cpf}|{data[0].name}|{data[0].telephone}|{data[0].clt}|{data[0].position}',
            f'{employees[0].cpf}|{employees[0].name}|{employees[0].telephone}|{employees[0].clt}|{employees[0].position}'
        )
        self.assertEqual(
            f'{data[1].cpf}|{data[1].name}|{data[1].telephone}|{data[1].clt}|{data[1].position}',
            f'{employees[1].cpf}|{employees[1].name}|{employees[1].telephone}|{employees[1].clt}|{employees[1].position}'
        )
    
    def test_delete_employee(self):
        employees = [
            Employee(Person('12312312312', 'Junior ferreira', '81988884444'), '123', 'teste'),
            Employee(Person('12312345621', 'lucas ferreira', '81988883333'), '456', 'teste')
        ]
        
        for employee in employees:
            self.dao.save_employee(employee)
            
        self.dao.delete_employee('123')
        
        data = FileUtils.read_file(Config.DB_EMPLOYEE)
        self.assertEqual(len(data), 1)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}|{data[0][4]}',
            f'{employees[1].cpf}|{employees[1].name}|{employees[1].telephone}|{employees[1].clt}|{employees[1].position}'
        )
        
    def test_update_employee(self):
        employees = [
            Employee(Person('12312312312', 'Junior ferreira', '81988884444'), '123', 'teste'),
            Employee(Person('12312345621', 'lucas ferreira', '81988883333'), '456', 'teste')
        ]
        
        for employee in employees:
            self.dao.save_employee(employee)
            
        new_employee = Employee(Person('12312312312', 'Junior ferreira', '81988884444'), '123', 'teste')
        self.dao.update_employee('456', new_employee)
        
        data = FileUtils.read_file(Config.DB_EMPLOYEE)
        self.assertEqual(
            f'{data[0][0]}|{data[0][1]}|{data[0][2]}|{data[0][3]}|{data[0][4]}',
            f'{employees[0].cpf}|{employees[0].name}|{employees[0].telephone}|{employees[0].clt}|{employees[0].position}'
        )

if __name__ == "__main__":
    unittest.main()