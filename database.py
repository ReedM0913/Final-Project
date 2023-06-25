from ai.py import pet_counter
from ai.py import pet_dictionary

def printDatabase(counter, dictionary):
    dog = dictionary["dog"]
    cat = dictionary["cat"]
    x = (f"Count of total pets: {counter}\n") + (f"Count of dogs: {dogs}\n") + (f"Count of cats: {cats}")
    return x
  
 
pet = printDatabase(pet_counter, pet_dictionary)
pet()
