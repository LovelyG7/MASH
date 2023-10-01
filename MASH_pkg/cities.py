
import csv
from pprint import pprint
import random 

#pd.read_csv(r"C:/Users/NG/Desktop/NiaNucampFolder/Python/1-Fundamentals/week5/simplemaps_worldcities/worldcities.csv", newline='') 
with open(r"C:/Users/NG/Desktop/NiaNucampFolder/Python/1-Fundamentals/week5/simplemaps_worldcities/worldcities.csv", encoding="utf8", newline='') as f:
    file = open(r"C:/Users/NG/Desktop/NiaNucampFolder/Python/1-Fundamentals/week5/simplemaps_worldcities/worldcities.csv", errors="ignore")
    reader = csv.reader(f)
    cities_list = list(reader)
    

city_selction= random.choice(cities_list)