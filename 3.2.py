#Tuples
abc = (1,3,2,5,4)
print(dir(tuple))
#Only 'count', 'index' these operations are usable on tuples
#Can't modify which means that tuple is immutable

#count operation
print(abc.count(5))

#Index operation
print(abc.index(4))#Give the value,  not the index value as the parameter

#To get the type
print(type(abc))