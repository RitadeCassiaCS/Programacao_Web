from ..models import Order
from .. import db

class OrderRepository:
    @staticmethod
    def save(order):
        db.session.add(order)
        db.session.commit()

    @staticmethod
    def get_all():
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id):
        return Order.query.get(order_id)
