from Controller import CategoryController, StockController, SaleController, CustomerController, EmployeeController

def start_database():
    ...
    

def system_acess() -> bool|None:
    while True:
        print(
            '[1] Acess the system\n'
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
                return True
            case 2:
                print('\n')
                cpf = input('Enter Cpf: ')
                name = input('Enter Name: ')
                telephone = input('Enter Telephone: ')
                clt = input('Enter CLT: ')
                position = input('Enter position: ')
                controller.register_employee(cpf , name, telephone, clt, position)
                print('\n')
            case 3:
                return None
            
            
def category_system():
    dao = CategoryController()
    while True:
        print('')
        print(
            ''
            '[1] Register Category\n'
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
        print('')
        print(
            ''
            '[1] Register Stock\n'
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
                price = float(input('Price: '))
                quantity = int(input('Quantity: '))
                dao.register_stock(product, category, price, quantity)
            case 2:
                dao.show_stock()
            case 3:
                product = input('Product Name: ')
                dao.remove_stock(product)
            case 4:
                target_product = input('Target Product Name: ')
                new_product = input('New product: ')
                new_category = input('New category: ')
                new_price = float(input('New Price: '))
                new_quantity = int(input('New Quantity: ')) 
                dao.change_stock(target_product, new_product, new_category, new_price, new_quantity)
            case 5:
                break
            case _:
                continue
            
            
def sale_system():
    dao = SaleController()
    while True:
        print('')
        print(
            ''
            '[1] Register product upon purchase\n'
            '[2] Show products on purchase\n'
            '[3] Remove product upon purchase\n'
            '[4] Change product quantity when puchasing\n'
            '[5] Back'
        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                product = input('Enter product: ')
                quantity = int(input('Enter quantity: '))
                dao.register_sale(product, quantity)
            case 2:
                dao.show_current_sale()
            case 3:
                product = input('Enter product: ')
                dao.remove_product_sale(product)
            case 4:
                product = input('Enter product: ')
                new_quantity = int(input('Enter new quantity: '))
                dao.change_product_sale(product, new_quantity)
            case 5:
                break
            case _:
                continue


def customer_system():
    dao = CustomerController()
    while True:
        print('')
        print(
            ''
            '[1] Register customer\n'
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
                new_cpf = input('Enter new CPF or empty: ')
                new_name = input('Enter new Name or empty: ')
                new_telephone = input('Enter new Telephone or empty: ')
                new_email = input('Enter new Email or empty: ')
                new_address = input('Enter new Address or empty: ')
                dao.change_customer(cpf, new_cpf, new_name, new_telephone, new_email, new_address)
            case 5:
                break
            case _:
                continue
            

def employee_system():
    dao = EmployeeController()
    while True:
        print('')
        print(
            ''
            '[1] Register Employee\n'
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
                new_cpf = input('Enter new CPF: ')
                new_name = input('Enter new Name: ')
                new_telephone = input('Enter new Telephone: ')
                new_clt = input('Enter new CLT: ')
                new_position = input('Enter new Position: ')
                dao.change_employee(clt, new_cpf, new_name, new_telephone, new_clt, new_position)
            case 5:
                break
            case _:
                continue

            
def main_system():
    while True:
        print('')
        print(
            '[1] Category\n'
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
                sale_system()
            case 4:
                customer_system()
            case 5:
                employee_system()
            case 6:
                ...
            case 7:
                ...
            case 8:
                break
            case _:
                continue
        

def main():
    if system_acess():
        main_system()
        
            
        
if __name__ == "__main__":
    main()