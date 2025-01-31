from main import GLOBAL_BALANCE
from utilitaries import distance
from globals import *

class Truck:
    def __init__(self, id, x_init, y_init, capacity, client_list):
        self.id = id
        self.position = (x_init, y_init)
        self.capacity = capacity
        self.filled_amt = capacity
        self.empty_amt = 0
        self.client = client_list # list of clients IDs
        self.assigned_plant = ... # plant ID
        self.route = []
    
    def available_free_space(self):
        return self.capacity - self.filled_amt - self.empty_amt

    def sell_filled(self, amount):
        self.filled_amt -= amount
        GLOBAL_BALANCE += amount * BOTTLE_PRICE

    def travel(self, destination):
        GLOBAL_BALANCE -= distance(self.position, destination) * KILOMETRIC_COST
        self.position = destination
    
    def take_bottles(self, amount) :
        self.empty_amt += amount
    
    def refill(self) :
        GLOBAL_BALANCE -= REFILL_COST
        ## Initier le remplissage ##
        self.empty_amt = 0