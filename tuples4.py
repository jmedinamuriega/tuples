# 4.
# Task 1: 


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

for name, item, quantity in orders:
    print(f"{name} ordered {quantity} {item}")

# Task 2:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]
contacts.sort()


print("Sorted contacts:")
for contact in contacts:
    print(contact)

letter=input("Please introduce the letter")
print(f"\nContacts whose names start with '{letter}':")
for name, email, phone in contacts:
    if name.startswith(f'{letter}'):
        print((name, email, phone))