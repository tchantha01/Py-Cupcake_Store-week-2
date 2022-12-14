from abc import ABC, abstractmethod
import csv
from pprint import pprint

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)
            
read_csv("sample.csv")            


# Cupcake classes
class Cupcake(ABC):
    
    size = "regular"
    
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
        self.tops = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    def add_tops(self, *args):
        for top in args:   
            self.tops.append(top)
    
    @abstractmethod        
    def calculate_prices(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    
    size = "mini"   
    
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.tops = []
    
    def calculate_prices(self, quantity):
        return quantity * self.price
   
        
class Regular(Cupcake):
    
    size = "regular" 
    
    def calculate_prices(self, quantity):
        return quantity * self.price
    
class Large(Cupcake):
    
    size = "large"    
    
    def calculate_prices(self, quantity):
        return quantity * self.price             

# Cupcake instances 
cupcake1 = Regular("Captain America", 2.99, "vanilla", "vanilla", "chocolate")
cupcake1.add_sprinkles("red", "white", "blue")
cupcake1.add_tops("miniature Captain America shield ring")
cupcake2 = Mini("Black Panther", 0.99, "chocolate", "cookies and cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Regular("Iron Man", 2.99, "red velvet", "yellow colored cream cheese", None)
cupcake3.add_tops("miniature Iron man helmet ring")
cupcake4 = Large("Incredible Hulk", 3.99, "vanilla", "green colored chocolate", None)
cupcake4.add_sprinkles("chocolate")
cupcake5 = Regular("Thor", 2.99, "vanilla", "blue and yellow swirl vanilla", None)
cupcake5.add_sprinkles("blue pop rocks")
cupcake5.add_tops("miniature Thor hammer ring")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
    ]

# Functions to add cupcake classes to file
def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling", "sprinkles", "tops"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles, "tops": cupcake.tops})
        else: 
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "tops": cupcake.tops})   
            
    

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling", "sprinkles", "tops"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles, "tops": cupcake.tops})
            else: 
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "tops": cupcake.tops})   
            
write_new_csv("cupcakes.csv", cupcake_list)  

# Functions to add the cupcake dictionaries to file          
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling", "sprinkles", "tops"]    
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
        writer.writerow(cupcake)
        
def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pprint(row)        





        
# f = open('file_one.txt','w+')
# f.write('This is my first txt file!')   
# f.close()         