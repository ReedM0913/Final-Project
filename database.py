from ai.py import day_counter
from ai.py import night_counter
from ai.py import day_dictionary
from ai.py import night_dictionary

def printDatabase(counter, dictionary):
    day = dictionary["day"]
    night = dictionary["night"]
    x = (f"Count of day: {counter}\n") + (f"Count of night: {night}\n")
    return x
  
 
dvn = printDatabase(day_counter, night_counter, day dictionary, night_dictionary)
dvn()
