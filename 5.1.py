#Set : A collection of unique items
#It is unordered data structure, hence sometimes the items will be shuffeled
#Sets are mutable (or mutable depending on conditions)
a = {1,2,2,4,3,5,5}
print(a)
b = {'apple','banana','papaya','apple','pomegranate','watermelon'}
print(b)
print(len(a))
print(len(b))
print(dir(set))

#Operations that can be performed on sets
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update'

#Add : Specific
a.add(6)
print(a)

#Remove : Specific
a.remove(6)
print(a)

#Pop : Removes 1st element from the set
a.pop()
print(a)

#Union
print(a.union(b))

#Difference
print(a.difference(b))

#Update : Need to update and return
print(a.update(b))
print(a)

#You can also perform mathematical operations directly
print(a+b)