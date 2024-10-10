from datetime import datetime

class Lane:
    def __init__(self, lane_type, max_capacity):
        self.lane_type = lane_type
        self.status = 'closed'
        self.customers = []
        self.max_capacity = max_capacity
        self.timestamp = datetime.now()

    def open_lane(self):
        self.status = 'open'

    def close_lane(self):
        self.status = 'closed'
        self.customers = []

    def add_customer(self, customer):
        if self.status == 'open' and len(self.customers) < self.max_capacity:
            self.customers.append(customer)
            return True
        return False

    def remove_customer(self):
        if self.customers:
            return self.customers.pop(0)
        return None

    def display_status(self):
        status = f"{self.lane_type} -> {'* ' * len(self.customers)}" if self.status == 'open' else 'closed'
        return status