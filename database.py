from bearAI.py import bear_counter
from bearAI.py import bear_dictionary

def printDatabase(counter, dictionary):
    black_bears = dictionary["black bear"]
    brown_bears = dictionary["brown bear"]
    x = (f"Count of total bears: {counter}\n") + (f"Count of brown bears: {brown_bears}\n") + (f"Count of black bears: {black_bears}")
    return x
  
 
bear = printDatabase(bear_counter, bear_dictionary)
bear()
