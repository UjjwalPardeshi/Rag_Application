from dotenv import load_dotenv
import os
import pandas as pd

population_path = os.path.join("data", "Population.csv") 
population_df = pd.read_csv(population_path)

print(population_df.head())



load_dotenv