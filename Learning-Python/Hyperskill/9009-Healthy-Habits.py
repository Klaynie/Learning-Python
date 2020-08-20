walks = [
    {"day": "Monday", "distance": 2000},
    {"day": "Tuesday", "distance": 3000},
    {"day": "Wednesday", "distance": 3500},
    {"day": "Thursday", "distance": 2500},
    {"day": "Friday", "distance": 2500},
    {"day": "Saturday", "distance": 1000},
    {"day": "Sunday", "distance": 5600}]

distance_total = 0
for item in walks:
    distance_total += item['distance']

print(round(distance_total / len(walks)))