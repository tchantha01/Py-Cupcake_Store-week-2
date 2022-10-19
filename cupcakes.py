from abc import ABC, abstractmethod
import csv
from pprint import pprint

def read_csv(file):
    with open("sample.csv") as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)
            
read_csv("sample.csv")            



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

# my_cupcake_large = Large("Chocolate Silk", 4.50, "Chocolate", "chocolate", "chocolate")
# print(my_cupcake_large.name)


# my_cupcake_mini = Mini("Chocolate", 1.50, "Chocolate", "white")
# print(my_cupcake_mini.name)
# print(my_cupcake_mini.price)
# print(my_cupcake_mini.size)

# my_cupcake = Cupcake("Strawberry Shortcake", 2.50, "vanilla", "strawberry", "strawberry") 

# my_cupcake.add_sprinkles("Oreo crumbs", "strawberry", "chocolate")

# my_cupcake.add_tops("decoder ring", "princess figure", "Marvel figures")

# print(my_cupcake.tops)

# print(my_cupcake.sprinkles)

# print(my_cupcake.name)


# my_cupcake.name = "Triple Chocolate"
# my_cupcake.frosting = "chocolate"   
# my_cupcake.filling =  "chocolate"  
# my_cupcake.sprinkles = True   

# print(my_cupcake.name)


# f = open('file_one.txt','w+')
# f.write('This is my first txt file!')   
# f.close() 

 
cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake1.add_tops("Miniature American Flag Ring")
cupcake2 = Mini("Oreo", 0.99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)
cupcake3.add_tops("Single strawberry slice")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]


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
            
write_new_csv("sample.csv", cupcake_list)            
        
        