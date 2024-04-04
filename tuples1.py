# 1. 
[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
# the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London"
"Itinerary 2: Bob - From Tokyo to San Francisco"
tuple1=[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_itinerary():
    for i, itinerary in enumerate(tuple1, start=1):
        name, flight, destination = itinerary
        print(f"Itinerary{i}:{name} - From {flight} to {destination}")
format_itinerary()
    