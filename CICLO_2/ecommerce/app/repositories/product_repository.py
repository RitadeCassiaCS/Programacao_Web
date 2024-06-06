from ..models import Product
from .. import db

class ProductRepository:
    @staticmethod
    def save(product):
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def find_all():
        return Product.query.all()

    @staticmethod
    def find_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def delete(product):
        db.session.delete(product)
        db.session.commit()
