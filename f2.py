import random

class Customer:
    def __init__(self, identifier):
        self.identifier = identifier
        self.basket_items = random.randint(1, 30)
        self.lottery_ticket = False

    def checkout_time(self, lane_type):
        processing_time = 4 if lane_type == 'Reg' else 6
        return self.basket_items * processing_time

    def award_lottery_ticket(self):
        if self.basket_items >= 10 and random.choice([True, False]):
            self.lottery_ticket = True

    def display_details(self):
        lottery_status = "wins a lottery ticket!" if self.lottery_ticket else "hard luck, no lottery ticket this time!"
        return (f"{self.identifier} -> items in basket: {self.basket_items}, {lottery_status}, "
                f"time to process basket at cashier till: {self.checkout_time('Reg')} Secs, "
                f"time to process basket at self-service till: {self.checkout_time('Slf')} Secs")