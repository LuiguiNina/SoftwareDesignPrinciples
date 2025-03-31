import unittest
from PaymentOrder import Order, CreditCardPayment, EmailNotification, OrderProcessor

class TestOrderProcessing(unittest.TestCase):
    def test_order_processing(self):
        order = Order(["Item1", "Item2"], 100)
        payment = CreditCardPayment()
        notifier = EmailNotification()
        processor = OrderProcessor(payment, notifier)
        
        try:
            processor.process_order(order)
            success = True
        except Exception as e:
            success = False

        self.assertTrue(success, "Order processing failed!")

if __name__ == "__main__":
    unittest.main()
