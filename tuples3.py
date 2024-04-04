
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-01", 220.0),
    
    # More data...
]

target_symbol=input("Introduce the name of the target: ")
def calculate_average_closing_price(stock_data, target_symbol):
    total_closing_price = 0
    count = 0

    for symbol, _, closing_price in stock_data:
        if symbol == target_symbol:
            total_closing_price += closing_price
            count += 1
    print(count)
    if count == 0:
        return None
    average_closing_price = total_closing_price / count
    print(average_closing_price)
calculate_average_closing_price(stock_data, target_symbol)



# Task 2:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]
def list_attendees_for_event(attendees, event):
    for i, attendee in enumerate(attendees, start=1):
        name, attendee_event = attendee
        if attendee_event == event:
            print(f"{i}. {name} is attending {event}")

def count_attendees_per_event(attendees):
    event_counts = {}
    for name, event in attendees:
        if event not in event_counts:
            event_counts[event] = 0
        event_counts[event] += 1
    return event_counts
        

    
print(list_attendees_for_event(attendees, "Python Conference"))
print(count_attendees_per_event(attendees))
        


