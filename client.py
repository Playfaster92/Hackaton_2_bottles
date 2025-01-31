from trucks import Truck


class Client:
    def __init__(self, id, x_coordinate, y_coordinate, consumption_rate, init, capacity):
        self.id = id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.consumption_rate = consumption_rate
        
        self.capacity = capacity
        self.filled_amt = init
        self.empty_amt = 0
        
        self.last_updated_time = 0
        
    def truck_arrives(self, truck: Truck, time: float):
        difference = time - self.last_updated_time
        curr_filled_amt = max(0, self.filled_amt - difference * self.consumption_rate)
        curr_empty_amt = self.empty_amt + difference * self.consumption_rate
        
        amount_exchanged = min(truck.filled_amt, curr_empty_amt)
        truck.filled_amt -= amount_exchanged
        truck.empty_amt += amount_exchanged
        
        self.empty_amt = curr_empty_amt - amount_exchanged
        self.filled_amt = curr_filled_amt + amount_exchanged
        
        self.last_updated_time = time
