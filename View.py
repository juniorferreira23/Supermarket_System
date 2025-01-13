from Controller import CategoryController, StockController, EmployeeController

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
        controller = EmployeeController()
        match int(option):
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
        match int(option):
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
            case _:
                break
                
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
        match int(option):
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
            case _:
                break
        
            
def main_system():
    while True:
        print('')
        print(
            '[1] Category\n'
            '[2] Stock\n'
            '[3] Sale\n'
            '[4] Customer\n'
            '[5] Employee\n'
            '[6] Exit'
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
                print('sale')
            case 4:
                print('customer')
            case 5:
                print('employee')
            case 6:
                break
            case _:
                continue
        

def main():
    if system_acess():
        main_system()
        
            
        
if __name__ == "__main__":
    main()