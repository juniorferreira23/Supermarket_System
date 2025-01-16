from Controller import CategoryController, StockController, SaleController, CustomerController, EmployeeController, SupplierController
from Model import Employee
from Validators import view_float_validator, view_int_validator, view_date_validator

def start_database():
    ...
    

def system_acess() -> bool|None:
    while True:
        print(
            '\n[1] Acess the system\n'
            '[2] Register employee\n'
            '[3] Logout of the system'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        controller = EmployeeController()
        match option:
            case 1:
                operator = input('Enter Operator: ')
                data = controller.check_employee(operator) 
                if not data:
                    print('Unregistered empoloyee\n')
                    continue
                print(f'{data.name} operator access system')
                return data
            case 2:
                cpf = input('\nEnter Cpf: ')
                name = input('Enter Name: ')
                telephone = input('Enter Telephone: ')
                clt = input('Enter CLT: ')
                position = input('Enter position: ')
                controller.register_employee(cpf , name, telephone, clt, position)
            case 3:
                return None
            
            
def category_system():
    dao = CategoryController()
    while True:
        print(
            '\n[1] Register Category\n'
            '[2] Show Category\n'
            '[3] Remove Category\n'
            '[4] Change Category\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                category = input('Category Name: ')
                dao.register_category(category)
            case 2:
                dao.show_categories()
            case 3:
                category = input('Enter the category you want to remove: ')
                dao.remove_category(category)
            case 4:
                category = input('Enter the category you want to change: ')
                new_categoy = input('Enter new category: ')
                dao.change_category(category, new_categoy)
            case 5:
                break
            case _:
                continue
                
                
def stock_system():
    dao = StockController()
    while True:
        print(
            '\n[1] Register Stock\n'
            '[2] Show Stock\n'
            '[3] Remove Stock\n'
            '[4] Change Stock\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                print('')
                product = input('Product Name: ')
                category = input('Category: ')
                price = view_float_validator('Price: ')
                quantity = view_int_validator('Quantity: ')
                dao.register_stock(product, category, price, quantity)
            case 2:
                dao.show_stock()
            case 3:
                product = input('Product Name: ')
                dao.remove_stock(product)
            case 4:
                target_product = input('Target Product Name: ')
                new_product = input('New product or leave it blank to keep the current data: ')
                new_category = input('New category or leave it blank to keep the current data: ')
                new_price = view_float_validator('New Price or leave it blank to keep the current data: ')
                new_quantity = view_int_validator('New Quantity or leave it blank to keep the current data: ')
                dao.change_stock(target_product, new_product, new_category, new_price, new_quantity)
            case 5:
                break
            case _:
                continue
            
            
def finalize_purchase_system(dao_sale: SaleController, operator: Employee):
    dao_customer = CustomerController()
    while True:
        option = input('Do you want to add the CPF? (Y|N): ')
        if not option:
            continue
        match option.upper():
            case 'Y':
                print(
                    '[1] Enter CPF\n'
                    '[2] Register Customer\n'
                )
                cpf_option = input('Select option: ')
                if not cpf_option:
                    continue
                elif cpf_option.isdigit():
                    cpf_option = int(cpf_option)
                match cpf_option:
                    case 1:
                        customer = input('Enter customer CPF: ')
                        dao_sale.finish_sale(operator.clt, customer)
                        break
                    case 2:
                        cpf = input('Enter CPF: ')
                        name = input('Enter Name: ')
                        telephone = input('Enter Telephone: ')
                        email = input('Enter Email: ')
                        address = input('Enter Address: ')
                        dao_customer.register_customer(cpf, name, telephone, email, address)
                        
                        customer = input('Enter customer CPF: ')
                        dao_sale.finish_sale(operator.clt, customer)
                        break
                    case _:
                        continue
            case 'N':
                dao_sale.finish_sale(operator.clt)
                break
            case _:
                continue
   
            
def sale_system(operator: Employee):
    dao = SaleController()
    while True:
        print(
            '\n[1] Register product upon purchase\n'
            '[2] Show products on purchase\n'
            '[3] Finalize product purchase\n'
            '[4] Remove product upon purchase\n'
            '[5] Change product quantity when puchasing\n'
            '[6] Canceled purchase\n'
            '[7] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                product = input('Enter product: ')
                quantity = view_int_validator('Enter quantity: ')
                dao.register_sale(product, quantity)
            case 2:
                dao.show_sale()
            case 3:
                finalize_purchase_system(dao, operator)               
            case 4:
                product = input('Enter product: ')
                dao.remove_product_sale(product)
            case 5:
                product = input('Enter product: ')
                new_quantity = view_int_validator('Enter new quantity: ')
                dao.change_product_sale(product, new_quantity)
            case 6:
                dao.cancel_sale()
            case 7:
                break
            case _:
                continue


def customer_system():
    dao = CustomerController()
    while True:
        print(
            '\n[1] Register customer\n'
            '[2] Show customer\n'
            '[3] Remove customer\n'
            '[4] Change customer\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                cpf = input('Enter CPF: ')
                name = input('Enter Name: ')
                telephone = input('Enter Telephone: ')
                email = input('Enter Email: ')
                address = input('Enter Address: ')
                dao.register_customer(cpf, name, telephone, email, address)
            case 2:
                dao.show_customers()
            case 3:
                cpf = input('Enter CPF to remove: ')
                dao.remove_customer(cpf)
            case 4:
                cpf = input('Enter CPF: ')
                new_cpf = input('Enter new CPF or leave it blank to keep the current data: ')
                new_name = input('Enter new Name or leave it blank to keep the current data: ')
                new_telephone = input('Enter new Telephone or leave it blank to keep the current data: ')
                new_email = input('Enter new Email or leave it blank to keep the current data: ')
                new_address = input('Enter new Address or leave it blank to keep the current data: ')
                dao.change_customer(cpf, new_cpf, new_name, new_telephone, new_email, new_address)
            case 5:
                break
            case _:
                continue
            

def employee_system():
    dao = EmployeeController()
    while True:
        print(
            '\n[1] Register Employee\n'
            '[2] Show Employess\n'
            '[3] Remove Employee\n'
            '[4] Change Employee\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                cpf = input('Enter CPF: ')
                name = input('Enter Name: ')
                telephone = input('Enter Telephone: ')
                clt = input('Enter CLT: ')
                position = input('Enter Position: ')
                dao.register_employee(cpf, name, telephone, clt, position)
                
            case 2:
                dao.show_employee()
            case 3:
                clt = input('Enter CLT you want to remove: ')
                dao.remove_employee(clt)
            case 4:
                clt = input('Enter CLT: ')
                new_cpf = input('Enter new CPF or leave it blank to keep the current data:: ')
                new_name = input('Enter new Name or leave it blank to keep the current data:: ')
                new_telephone = input('Enter new Telephone or leave it blank to keep the current data:: ')
                new_clt = input('Enter new CLT or leave it blank to keep the current data:: ')
                new_position = input('Enter new Position or leave it blank to keep the current data:: ')
                dao.change_employee(clt, new_cpf, new_name, new_telephone, new_clt, new_position)
            case 5:
                break
            case _:
                continue
            
            
def supplier_system():
    dao = SupplierController()
    while True:
        print(
            '\n[1] Register Supplier\n'
            '[2] Show Suppliers\n'
            '[3] Remove Supplier\n'
            '[4] Change Supplier\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                cnpj = input('Enter CNPJ: ')
                company_name = input('Enter Company Name: ')
                category = input('Enter Category: ')
                telephone = input('Enter Telephone: ')
                dao.register_supplier(cnpj, company_name, category, telephone)
            case 2:
                dao.show_supplier()
            case 3:
                cnpj = input('Enter CNPJ of the supplier you want to remove: ')
                dao.remove_supplier(cnpj)
            case 4:
                target_cnpj = input('Enter CNPJ: ')
                new_cnpj = input('Enter new CNPJ or leave it blank to keep the current data: ')
                new_company_name = input('Enter new Company Name or leave it blank to keep the current data: ')
                new_category = input('Enter new Category or leave it blank to keep the current data: ')
                new_telephone = input('Enter new Telephone or leave it blank to keep the current data: ')
                dao.change_supplier(target_cnpj, new_cnpj, new_company_name, new_category, new_telephone)
            case 5:
                break
            case _:
                continue
            
            
def report_system():
    dao = SaleController()
    while True:
        print(
            '\n[1] Show Report Sales\n'
            '[2] Show Best Selling Product Report\n'
            '[3] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                start_date = view_date_validator('Start Date (dd/mm/yyyy): ')
                end_date = view_date_validator('End Date (dd/mm/yyyy): ')
                dao.report_sales(start_date, end_date)
            case 2:
                dao.best_selling_products_report()
            case 3:
                break
            case _:
                continue
                

def main_system(operator: Employee):
    while True:
        print(
            '\n[1] Category\n'
            '[2] Stock\n'
            '[3] Sale\n'
            '[4] Customer\n'
            '[5] Employee\n'
            '[6] Supplier\n'
            '[7] Sales Reports\n'
            '[8] Exit'
        )
        option = input('Select option: ')
        if not option:
            continue
        match int(option):
            case 1:
                category_system()
            case 2:
                stock_system()
            case 3:
                sale_system(operator)
            case 4:
                customer_system()
            case 5:
                employee_system()
            case 6:
                supplier_system()
            case 7:
                report_system()
            case 8:
                break
            case _:
                continue
        

def main():
    operator = system_acess()
    if operator:
        main_system(operator)
        
            
        
if __name__ == "__main__":
    main()