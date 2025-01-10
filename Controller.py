from Model import Category, Stock, Product, Sale, SaleItem
from DAO import CategoryDao, StockDao, SaleDao
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
        self.dao = StockDao()
        
    def register_stock(self, name_product: str, category: str, price: float, quality: int) -> None:
        validator = Validators.product_validator(name_product, category, price, quality)
        if validator:
            print(validator)
            return None
        exist_product = self.dao.find_by_product(name_product)
        if exist_product:
            print('Product already registered')
            return None
        dao_category = CategoryDao()
        exist_category = dao_category.find_by_name(category)
        if not exist_category:
            print('Category not found')
            return None
        self.dao.save_stock(Stock(Product(name_product, category, price), quality))
        print('Stock registed sucessfully')
    
    def show_stock(self):
        stocks = self.dao.get_all_stocks()
        
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
        exist_product = self.dao.find_by_product(name_product)
        if not exist_product:
            print('Stock not found')
            return None
        self.dao.delete_stock(name_product)
        print('Stock removed sucessfully')
        
    def change_stock(self, current_product: str, new_product: str, new_category: str, new_price: float, new_quantity: int):
        current_validator = Validators.product_validator(current_product)
        new_validator = Validators.product_validator(new_category, new_category, new_price, new_quantity)
        if current_validator:
            print(f'The value of change {current_product}')
            return None
        elif new_validator:
            print(f'The new change value {current_product}')
            return None
        exist_current_product = self.dao.find_by_product(current_product)
        if not exist_current_product:
            print('Stock not found')
            return None
        exist_new_product = self.dao.find_by_product(new_product)
        if exist_new_product:
            print('Stock already registered')
            return None
        dao_category = CategoryDao()
        exist_category = dao_category.find_by_name(new_category)
        if not exist_category:
            print('Category not found')
            return None
        self.dao.update_stock(current_product, Stock(Product(new_product, new_category, new_price), new_quantity))


class SaleController:
    def __init__(self):
        self.dao_stock = StockDao()
        self.dao_sale = SaleDao()
        self.list_product: list[SaleItem] = []
        
    def register_sale(self, name_product: str, quantity: int):
        validator = Validators.product_validator(name_product, quantity=quantity)
        if validator:
            print(validator)
            return None
        stock = self.dao_stock.find_by_product(name_product)
        if not stock:
            print('Product not found')
            return None
        if stock.quantity < quantity:
            print('Quantity unavailable')
            print(f'Available stock of [{stock.product.name}] is [{stock.quantity}]')
            return None
        self.list_product.append(SaleItem(stock.product, quantity))
        print('Product registed upon purchase')
        
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
            
    # def 

controller = SaleController()
controller.register_sale('teste', 90)
controller.register_sale('test3', 90)
print(controller.list_product[0].product.name)
controller.show_current_sale()
        