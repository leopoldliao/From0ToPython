"""
Author: FaDr_YL (_YL_)
"""


print("---int---")

a_int = 10
print(type(a_int))

print("---string---")

a_string = "string"
print(type(a_string))
print(a_string.upper())
print(a_string.index("s"))
# you can try other functions by your own.

print("---format string---")

string_2 = "price: {0}, desc: {1}"
print(string_2.format(10, "Description"))

print("---boolean---")

a_bool = True
print(type(a_bool))

print("---tuple---")

a_tuple = (1, 2)
print(type(a_tuple))

print("---list---")

a_list = [1, 2, 3, 4, 5]
print(type(a_list))

print("---set---")

a_set = {"item1", "item2", "item3", "item1"}
print(type(a_set))
print(a_set)

print("---list to set---")

set_2 = set(a_list)
print(type(set_2))

print("---dictionary---")

a_dict = {'name': "the_item", 'price': 9.95, 'stock': 10}
print(type(a_dict))
print(a_dict["name"])
a_dict["desc"] = "just an item"
a_dict['price'] = 8.5
print(a_dict)
print(a_dict.keys())
print(a_dict.values())

print("---dictionary creation 2---")

dict_2 = {x: x+2 for x in range(3)}
print(dict_2)

