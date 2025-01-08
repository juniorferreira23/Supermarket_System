from Model import Category, Stock, Product
from DAO import CategoryDao, StockDao
import Validators

class CategoryController:
    def __init__(self):
        self.dao = CategoryDao()
    
    def register_category(self, category) -> None:
        category = Category(category)
        validator = Validators.category_validator(category)
        
        if not validator:
            retrieved = self.dao.get_all_categories()
            exist_category = any(data.name == category.name for data in retrieved)
            if not exist_category:
                self.dao.save_category(category)
            print('Category registered successfully')
        else:
            print(validator)
    
    def show_categories(self) -> None:
        categories = self.dao.get_all_categories()
        for index, category in enumerate(categories):
            print(f'[{index}] {category.name}')
    
    def remove_category(self, category) -> None:
        category = Category(category)
        validator = Validators.category_validator(category)
        
        if not validator:
            self.dao.delete_category(category)
            print('Category removed sucessfully')
        else:
            print(validator)
    
    def change_category(self, current_category, new_category) -> None:
        category = Category(category)
        current_validator = Validators.category_validator(current_category)
        change_validator = Validators.category_validator(new_category)
        
        if not current_validator and not change_validator:
            self.dao.update_category(current_category, new_category)
            print('Category changed sucessfully')
        elif current_category:
            print(current_category)
        else:
            print(change_validator)
            

class StockController:
    def __init__(self):
        self.dao = StockDao()
        
    def register_stock(self, name_product, category, price, quality):
        stock = Stock(Product(name_product, category, price), quality)
        validator = Validators.stock_validator(stock)
        
        if not validator:
            self.dao.save_stock(stock)
            print('Stock registed sucessfully')
        else:
            print(validator)
            
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
            
    def remove_stock(self, current_product, new_product, new_category, new_price, new_quality):
        ...
        
