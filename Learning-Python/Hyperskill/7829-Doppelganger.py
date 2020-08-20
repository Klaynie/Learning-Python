from collections.abc import Hashable
object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]

hash_list = [hash(item) for item in object_list if isinstance(item, Hashable)]
hash_count_dict = {hash_: hash_list.count(hash_) for hash_ in hash_list}
print(sum(count for count in hash_count_dict.values() if count > 1))