from os import system

p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW"]
total = len(p)
free = p.count(None)

car_name = []

system('cls')

print("On this parking we have:")
print("N\t Name\t Q\n")

# Collect unique car names
for car in p:
    if car and car not in car_name:
        car_name.append(car)

# Print car models and their counts
for i, car in enumerate(car_name, start=1):
    count = p.count(car)
    print(f"{i}\t {car}\t {count}")

print("Parking (free/total):", free, "/", total, "places.")
