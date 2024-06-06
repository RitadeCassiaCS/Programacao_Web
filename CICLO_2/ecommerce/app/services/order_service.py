from ..repositories.order_repository import OrderRepository
from ..models import Order

class OrderService:
    @staticmethod
    def create_order(user_id, total_price):
        order = Order(user_id=user_id, total_price=total_price)
        OrderRepository.save(order)
        return order

    @staticmethod
    def get_all_orders():
        return OrderRepository.get_all()

    @staticmethod
    def get_order_by_id(order_id):
        return OrderRepository.get_by_id(order_id)

    @staticmethod
    def update_order(order_id, total_price):
        order = OrderRepository.get_by_id(order_id)
        if order:
            order.total_price = total_price
            OrderRepository.save(order)
            return order
        return None
