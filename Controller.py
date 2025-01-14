from Model import Category, Stock, Product, Sale, SaleItem, Employee, Person, Customer, Supplier
from DAO import CategoryDao, StockDao, SaleDao, EmployeeDao, CustomerDao, SupplierDao
import Validators

class CategoryController:
    def __init__(self):
        self.dao = CategoryDao()
    
    def register_category(self, category: str) -> None:
        validator = Validators.category_validator(category)
        if validator:
            print(validator)
            return None
        exist_category = self.dao.find_by_name(category)
        if exist_category:
            print('Category already registered')
            return None
        self.dao.save_category(Category(category))
        print('Category registered successfully')
    
    def show_categories(self) -> None:
        categories = self.dao.get_all_categories()
        print('')
        for index, category in enumerate(categories):
            print(f'[{index}] {category.name}')
    
    def remove_category(self, category: str) -> None:
        validator = Validators.category_validator(category)
        if validator:
            print(validator)
            return None
        exist_category = self.dao.find_by_name(category)
        if not exist_category:
            print('Category not found')
            return None
        self.dao.delete_category(category)
        print('Category removed sucessfully')
    
    def change_category(self, current_category: str, new_category: str) -> None:
        current_validator = Validators.category_validator(current_category)
        change_validator = Validators.category_validator(new_category)        
        if current_validator:
            print(f'The value of change {current_category}')
            return None
        elif change_validator:
            print(f'The new change value {change_validator}')
            return None
        exist_current_category = self.dao.find_by_name(current_category)
        if not exist_current_category:
            print('Current category not found')
            return None
        exist_new_category = self.dao.find_by_name(new_category)
        if exist_new_category:
            print('Category already registered')
            return None
        self.dao.update_category(current_category, Category(new_category))
        print('Category changed sucessfully')

class StockController:
    def __init__(self):
        self.dao_stock = StockDao()
        self.dao_category = CategoryDao()
        
    def register_stock(self, name_product: str, category: str, price: float, quality: int) -> None:
        validator = Validators.product_validator(name_product, category, price, quality)
        if validator:
            print(validator)
            return None
        exist_product = self.dao_stock.find_by_product(name_product)
        if exist_product:
            print('Product already registered')
            return None
        exist_category = self.dao_category.find_by_name(category)
        if not exist_category:
            print('Category not found')
            return None
        self.dao_stock.save_stock(Stock(Product(name_product, category, price), quality))
        print('Stock registered sucessfully')
    
    def show_stock(self):
        stocks = self.dao_stock.get_all_stocks()
        
        for index, stock in enumerate(stocks):
            print(f'{5*'='} [{index}] {5*'='}')
            print(
                f'Product Name: {stock.product.name}\n'
                f'Category: {stock.product.category}\n'
                f'Price: {stock.product.price}\n'
                f'Quantity: {stock.quantity}'
            )
            
    def remove_stock(self, name_product: str):
        validator = Validators.product_validator(name_product)
        if validator:
            print(validator)
            return None
        exist_product = self.dao_stock.find_by_product(name_product)
        if not exist_product:
            print('Stock not found')
            return None
        self.dao_stock.delete_stock(name_product)
        print('Stock removed sucessfully')
        
    def change_stock(self, target_product: str, new_product:str=None, new_category:str=None, new_price:float=None, new_quantity:int=None):
        current_validator = Validators.product_validator(target_product)
        if current_validator:
            print(f'The value of change {target_product}')
            return None
        
        new_validator = Validators.product_validator(new_category, new_category, new_price, new_quantity)
        if new_validator:
            print(f'The new change value {target_product}')
            return None
        
        exist_curret_product = self.dao_stock.find_by_product(target_product)
        if not exist_curret_product:
            print('Stock not found')
            return None
        
        exist_new_product = self.dao_stock.find_by_product(new_product)
        if exist_new_product:
            print('Stock already registered')
            return None
        
        exist_category = self.dao_category.find_by_name(new_category)
        if not exist_category:
            print('Category not found')
            return None
    
        self.dao_stock.update_stock(target_product, Stock(
            Product(
                new_product,
                new_category,
                new_price
            ),
            new_quantity
        ))
        print('Stock changed sucessfully')


class SaleController:
    def __init__(self):
        self.dao_stock = StockDao()
        self.dao_sale = SaleDao()
        self.list_product: list[SaleItem] = []
        self.total = 0
        
    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.list_product)
        self.total = round(total, 2)
        
    def register_sale(self, name_product: str, quantity: int):
        validator = Validators.product_validator(name_product, quantity=quantity)
        if validator:
            print(validator)
            return None
        data_product = self.dao_stock.find_by_product(name_product)
        if not data_product:
            print('Product not found')
            return None
        if data_product.quantity < quantity:
            print('Quantity unavailable')
            print(f'Available stock of [{data_product.product.name}] is [{data_product.quantity}]')
            return None
        self.list_product.append(SaleItem(data_product.product, quantity))
        print('Product registered upon purchase')
        self.calculate_total()
        print(f'Current value sale [{self.total}]')
        
        
    def show_current_sale(self):
        for index, product in enumerate(self.list_product):
            print(f'{5*'='} [{index}] {5*'='}')
            print(
                f'Product: {product.product.name}\n'
                f'Price: {product.product.price}\n'
                f'Quantity: {product.quantity}'
            )

    def show_sales(self):
        sales = self.dao_sale.get_all_sales()
        
        for index, sale in enumerate(sales):
            print(f'{5*'='} [{index}] {5*'='}')
            print(f'Registration: {sale.registration}')
            for i, product in enumerate(sale.sold_products):
                print(f'{5*'-'} [{i}] {5*'-'}')
                print(
                    f'Product: {product.product.name}\n'
                    f'Price: {product.product.price}'
                )
            print(
                f'Operator: {sale.operator}\n'
                f'Customer: {sale.customer}\n'
                f'Date: {sale.date}\n'
                f'Total: {sale.total}'
            )
            
    def finish_sale(self, operator: str, customer: str):
        self.dao_sale.save_sale(Sale(
            sold_products=self.list_product, operator=operator, customer=customer, total=self.total
        ))
        for item in self.list_product:
            current_product = self.dao_stock.find_by_product(item.product.name)
            self.dao_stock.update_stock(current_product.product.name, Stock(Product(current_product.product.name, current_product.product.category, current_product.product.price), current_product.quantity - item.quantity))
        self.list_product = []
        self.total = 0
        print('Sale finalized')
        
    def cancel_sale(self):
        self.list_product = []
        self.total = 0
        print('Sale cancelled')
        
    def remove_product_sale(self, name_product: str):
        if not self.list_product:
            print('The product list is empty')
            return None
        exist_product = any(product.product.name == name_product for product in self.list_product)
        if not exist_product:
            print('Product not found')
            return None
        self.list_product = list(filter(lambda x: x.product.name != name_product, self.list_product))
        self.calculate_total()
        print('Product removed sucessfully')
        
    def change_product_sale(self, name_product: str, new_quantity: str):
        if not self.list_product:
            print('The product list is empty')
            return None
        exist_product = any(product.product.name == name_product for product in self.list_product)
        if not exist_product:
            print('Product not found')
            return None
        self.list_product = list(map(lambda x: 
            SaleItem(Product(x.product.name, x.product.category, x.product.price), new_quantity)
            if(x.product.name == name_product) else(x),
            self.list_product
        ))
        self.calculate_total()
        print('Changed product quantity')

        
class EmployeeController:
    def __init__(self):
        self.dao = EmployeeDao()
        
    def check_employee(self, clt) -> Employee|None:
        employee = self.dao.find_by_clt(clt)
        if not employee:
            return None
        return employee
        
    def register_employee(self, cpf: str, name: str, telephone: str, clt: str, position: str) -> str|None:
        validator = Validators.employee_validator(cpf, name, telephone, clt, position)
        if validator:
            print(validator)
            return None
        employee = self.dao.find_by_clt(clt)
        if employee:
            print('Employee already registered')
            return None
        self.dao.save_employee(Employee(Person(cpf, name, telephone), clt, position))
        print('Employee registered sucessfully')
        
    def show_employee(self) -> None:
        employees = self.dao.get_all_employee()
        for index, employee in enumerate(employees):
            print(f'{5*'='} [{index}] {5*'='}')
            print(
                f'CLT: {employee.clt}\n'
                f'Name: {employee.name}\n'
                f'CPF: {employee.cpf}\n'
                f'Telefone: {employee.telephone}\n'
                f'Position: {employee.position}'
            )
        
    def remove_employee(self, clt) -> None:
        validator = Validators.employee_validator(clt=clt)
        if validator:
            print(validator)
            return None
        employee = self.dao.find_by_clt(clt)
        if not employee:
            print('Employee not found')
            return None
        self.dao.delete_employee(clt)
        print('Employee removed sucessfully')
    
    def change_employee(self, target_clt, new_cpf=None, new_name=None, new_telephone=None, new_clt=None, new_position=None):
        target_validator = Validators.employee_validator(target_clt)
        if target_validator:
            print(target_validator)
            return None
        new_validator = Validators.employee_validator(new_cpf, new_name, new_telephone, new_clt, new_position)
        if new_validator:
            print(new_validator)
            return None
        current_employee = self.dao.find_by_clt(target_clt)
        if not current_employee:
            print('Employee not found')
            return None
        new_employee = self.dao.find_by_clt(new_clt)
        if new_employee:
            print('Employee already registered')
            return None
        
        self.dao.update_employee(target_clt, Employee(
            Person(
                new_cpf or current_employee.cpf, 
                new_name or current_employee.name,
                new_telephone or current_employee.telephone
            ), 
            new_clt or current_employee.clt,
            new_position or current_employee.position
        ))
        print('Employee changed sucessfully')
        

class CustomerController:
    def __init__(self):
        self.dao = CustomerDao()
        
    def register_customer(self, cpf: str, name: str, telephone: str, email: str, address: str) -> None:
        validator = Validators.customer_validator(cpf, name, telephone, email, address)
        if validator:
            print(validator)
            return None
        exist_customer = self.dao.find_by_cpf(cpf)
        if exist_customer:
            print('Customer already registered')
            return None
        self.dao.save_customer(Customer(Person(cpf, name, telephone), email, address))
        print('Customer registered sucessfully')
        
    def show_customers(self) -> None:
        customers = self.dao.get_all_customer()
        for index, customer in enumerate(customers):
            print(f'{5*'='} [{index}] {5*'='}')
            print(
                f'CPF: {customer.cpf}\n'
                f'Name: {customer.name}\n'
                f'telephone: {customer.telephone}\n'
                f'Email: {customer.email}\n'
                f'Address: {customer.address}'
            )
    
    def remove_customer(self, cpf: str) -> None:
        validator = Validators.customer_validator(cpf)
        if validator:
            print(validator)
            return None
        exist_customer = self.dao.find_by_cpf(cpf)
        if not exist_customer:
            print('Customer not found')
            return None
        self.dao.delete_customer(cpf)
        print('Customer removed sucessfully')
    
    def change_customer(self, target_cpf:str, new_cpf:str=None, new_name:str=None, new_telephone:str=None, new_email:str=None, new_address:str=None) -> None:
        target_cpf_validator = Validators.customer_validator(target_cpf)
        if target_cpf_validator:
            print(target_cpf_validator)
            return None
        
        new_customer_validator = Validators.customer_validator(new_cpf or target_cpf, new_name, new_telephone, new_email, new_address)
        if new_customer_validator:
            print(new_customer_validator)
            return None
        
        exist_customer = self.dao.find_by_cpf(target_cpf)
        if not exist_customer:
            print('Customer not found')
            return None
        
        if new_cpf:
            exist_new_customer = self.dao.find_by_cpf(new_cpf)
            if exist_new_customer:
                print('Customer already registered')
                return None
        
        self.dao.update_customer(
            target_cpf,
            Customer(
                Person(
                    new_cpf or exist_customer.cpf,
                    new_name or exist_customer.name,
                    new_telephone or exist_customer.telephone
                ), 
                new_email or exist_customer.email,
                new_address or exist_customer.address
            )
        )
        print('Customer changed sucessfully')
        
        
class SupplierController:
    def __init__(self):
        self.dao = SupplierDao()
        
    def register_supplier(self, cnpj: str, razao_social: str, category: str, telephone: str) -> None:
        validator = Validators.va
        self.dao.save_supplier(Supplier())