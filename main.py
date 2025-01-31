from globals import *
from plants import Plant
from client import Client
from trucks import Truck
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


############################################## DECLARATIONS ##############################################

df_clients = pd.read_csv("clients.csv")
df_plants = pd.read_csv("plants.csv")

CLIENTS, PLANTS = [], []

for i in range(NCLIENTS) :
    c = df_clients.iloc[i]
    CLIENTS.append(Client(c.id, c.coord_x, c.coord_y, c.consumption, c.init, c.capacity))

for i in range(NPLANTS) :
    p = df_plants.iloc[i]
    nearby_clients = df_clients[((p.coord_x - df_clients["coord_x"])**2 + (p.coord_y - df_clients["coord_y"])**2 < 100**2)]
    NPLANTS.append(Plant(p.id, p.coord_x, p.coord_y, p.capacity, p.refill, nearby_clients.index))

class Event:
    def __init__(self, time):
        self.time = time
        
    def execute(self):
        pass
    
    def __lt__(self, other):
        return self.time < other.time

class TruckArriveToPlant(Event):
    def __init__(self, time, truck, plant):
        super().__init__(time)
        self.truck = truck
        self.plant = plant
    
    def execute(self) -> Event:
        return self.plant.truck_arrive(self.truck, self.time)
        
class TruckArriveToClient(Event):
    def __init__(self, time, truck, client):
        super().__init__(time)
        self.truck = truck
        self.client = client
    
    def execute(self) -> Event:
        return self.client.truck_arrive(self.truck, self.time)
        
class TruckSendToPlant(Event):
    def __init__(self, time, truck, plant):
        super().__init__(time)
        self.truck = truck
        self.plant = plant
        
    def execute(self) -> Event:
        return self.plant.truck_send(self.truck, self.time)
        
class TruckSendToClient(Event):
    def __init__(self, time, truck, client):
        super().__init__(time)
        self.truck = truck
        self.client = client
        
    def execute(self) -> Event:
        return self.client.truck_send(self.truck, self.time)
        
        
class State :
    def __init__(self, trucks, plants):
        self.plants = plants
        self.trucks = trucks
        
    def update_state(self, event: Event):
        next_event: Event = event.execute()
        return next_event



if __name__ == "__main__":
    pass
    

