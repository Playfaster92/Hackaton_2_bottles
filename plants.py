from trucks import Truck
import numpy as np

distance = lambda PointA, PointB: np.sqrt((PointA[0] - PointB[0])**2 + (PointA[1] - PointB[1])**2)

class Plant :
    def __init__(self, id, x_coordinates, y_coordinates, capacity, init, filling_rate, clients) :
        self.id = id
        self.filling_rate = filling_rate
        self.x_coordinate = x_coordinates 
        self.y_coordinate = y_coordinates
        self.capacity = capacity    
        self.filled_amount = init
        self.empty_amount = 0
        self.trucks_waiting = 0
        self.last_updated_time = 0
        self.client_list = clients

    def truck_arrives(self, truck: Truck, time: float):
        difference = time - self.last_updated_time
        curr_filled_amt = self.filled_amount + max(int(difference * self.filling_rate), self.empty_amount)
        curr_empty_amt = self.empty_amount - max(int(difference * self.filling_rate), self.empty_amount)
        amount_taken= min(truck.empty_amt, curr_filled_amt)
        
        self.filled_amount = curr_filled_amt - amount_taken
        self.empty_amount = curr_empty_amt + amount_taken
        truck.filled_amt += amount_taken 
        truck.empty_amt -= amount_taken
        
        
        amount_taken2 = min(truck.available_free_space(), self.filled_amount)
        self.filled_amount -= amount_taken2
        truck.filled_amt += amount_taken2

        self.last_updated_time = time

    def best_client(self, truck):
        radius = 100
        near_clients = self.clients_df[
            ((self.x_coordinate - self.clients_df["coord_x"])**2 + 
             (self.y_coordinate - self.clients_df["coord_y"])**2) < radius**2
        ]
        profits = []
        for _, client in near_clients.iterrows():
            client_position = (client["coord_x"], client["coord_y"])
            distance_to_client = np.sqrt((self.x_coordinate - client["coord_x"])**2 + 
                                         (self.y_coordinate - client["coord_y"])**2)
            
            demand = client["capacity"] - client["init"]  
            potential_supply = min(demand, truck.filled_amt)  
            revenue = potential_supply * 100  
            cost = distance_to_client * 0.1 
            
            profit = revenue - (2 * cost)  
            profits.append((client["id"], profit))

        best_client_id, best_profit = max(profits, key=lambda x: x[1])

        return self.clients_df[self.clients_df["id"] == best_client_id].iloc[0] 