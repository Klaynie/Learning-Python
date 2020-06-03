import collections
some_object = ['some_object']

print("Hashable" if isinstance(some_object, collections.Hashable) else "Not hashable")