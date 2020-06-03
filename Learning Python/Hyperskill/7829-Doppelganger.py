from collections.abc import Hashable
object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
objects_dict = dict()
duplicates_counter = 0

for item in object_list:
    if isinstance(item, Hashable):
        objects_dict[hash(item)] = 1 + objects_dict.get(hash(item), 0)

for _key, value in objects_dict.items():
    if value > 1:
        duplicates_counter += value

print(duplicates_counter)