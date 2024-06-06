from ..repositories.product_repository import ProductRepository
from ..models import Product

class ProductService:
    @staticmethod
    def create_product(name, description, price, stock):
        product = Product(name=name, description=description, price=price, stock=stock)
        ProductRepository.save(product)
        return product

    @staticmethod
    def get_all_products():
        return ProductRepository.find_all()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.find_by_id(product_id)

    @staticmethod
    def update_product(product_id, name, description, price, stock):
        product = ProductRepository.find_by_id(product_id)
        if product:
            product.name = name
            product.description = description
            product.price = price
            product.stock = stock
            ProductRepository.save(product)
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.find_by_id(product_id)
        if product:
            ProductRepository.delete(product)
            return True
        return False
