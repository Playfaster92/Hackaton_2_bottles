import numpy as np
from client import Client

class State:
    def __init__(self, client, plant, truck):
        self.client = client
        self.plant = plant
        self.truck = truck
        self.time = 0
    def update_event(self):
        
    
    