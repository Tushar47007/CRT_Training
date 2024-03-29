import random

list1 = random.sample(range(1, 100), 6)
list2 = random.sample(range(1, 100), 5)
common_elements = 0

if len(list1) >= len(list2):
    long_list = list1
    short_list = list2
else:
    long_list = list2
    short_list = list1

for element in short_list:
    if element in long_list:
        common_elements += 1

print("Common Elements:", common_elements)
