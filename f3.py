from f1 import Lane
from f2 import Customer
import random
import time
from datetime import datetime

def setup_lanes():
    lanes = [Lane('Reg', 5) for _ in range(5)] + [Lane('Slf', 15)]
    lanes[0].open_lane()  # Open one regular lane
    lanes[5].open_lane()  # Open one self-service lane
    return lanes

def assign_customers_to_lanes(customers, lanes):
    for customer in customers:
        customer.award_lottery_ticket()
        assigned = False
        for lane in lanes:
            if lane.lane_type == 'Slf' and customer.basket_items < 10 and lane.add_customer(customer):
                assigned = True
                break
            elif lane.lane_type == 'Reg' and lane.add_customer(customer):
                assigned = True
                break

        if not assigned:
            for lane in lanes:
                if lane.status == 'closed':
                    lane.open_lane()
                    lane.add_customer(customer)
                    break

def display_lane_status(lanes, time):
    print(f"### Lane status at {time} ###")
    total_customers = sum(len(lane.customers) for lane in lanes if lane.status == 'open')
    print(f"Total number of customers waiting to check out at {time} is: {total_customers}")
    for i, lane in enumerate(lanes, start=1):
        print(f"L{i} ({lane.lane_type}) -> {lane.display_status()}")

def display_customer_details(lanes):
    print("### Customer details ###")
    for lane in lanes:
        if lane.status == 'open':
            for customer in lane.customers:
                print(customer.display_details())

def run_simulation():
    lanes = setup_lanes()
    start_time = datetime.now()
    total_customers = 0
    simulation_duration = 5 * 60  # Run for 5 minutes

    while True:
        # Generate new customers every 30 seconds
        new_customers = [Customer(f'C{total_customers + i + 1}') for i in range(random.randint(1, 10))]
        total_customers += len(new_customers)

        # Check if total customers exceed 40
        if total_customers > 40:
            print("Maximum customer capacity reached. No more customers can be added.")
            break

        assign_customers_to_lanes(new_customers, lanes)

        # Display the status of lanes
        current_time = datetime.now()
        elapsed_time = (current_time - start_time).seconds
        display_lane_status(lanes, f"{elapsed_time // 60:02}:{elapsed_time % 60:02}")

        # Display customer details
        display_customer_details(lanes)

        # Check if the simulation duration has been reached
        if elapsed_time >= simulation_duration:
            print("Simulation time limit reached.")
            break

        # Wait for 30 seconds before the next interval
        time.sleep(30)

if __name__ == "__main__":
    run_simulation()