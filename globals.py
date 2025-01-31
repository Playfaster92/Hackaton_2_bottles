import pandas as pd
BOTTLE_PRICE = 100
KILOMETRIC_COST = 0.1
REFILL_COST = 40

NCLIENTS = pd.read_csv("clients.csv").shape[0]
NPLANTS = pd.read_csv("plants.csv").shape[0]