from abc import ABC, abstractmethod

# SRP: Separate classes for order, payment, and notifications
class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class NotificationService(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailNotification(NotificationService):
    def notify(self, message):
        print(f"Email Notification: {message}")

# DIP: OrderProcessor depends on abstractions
class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor, notifier: NotificationService):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def process_order(self, order):
        self.payment_processor.pay(order.total)
        self.notifier.notify("Order processed successfully!")

# Example Usage
order = Order(["Item1", "Item2"], 100)
payment = CreditCardPayment()
notifier = EmailNotification()
processor = OrderProcessor(payment, notifier)
processor.process_order(order)