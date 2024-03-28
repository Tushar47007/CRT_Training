list = [4,7,0,0,7]
print(dir(list))
#above one gives output
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#these are actually the operations that can be done on lists

#append operation
list.append(12)
for i in range(len(list)):
    print(list[i],end='') #this ability to modify is called as "__Mutability__"
                        #if it lacks the ability then it's "__Immutable__"
print('\n')
#Remove operation
list.remove(0)#If there's multiple similar items in the list then the the first one according to index in ascending order
for i in range(len(list)):
    print(list[i],end='')
print('\n')

#Insert operation
list.insert(6,17)
for i in range(len(list)):
    print(list[i],end='')

#pop operation
list.pop(4)#argument is index from where element is to be removed
for i in range(len(list)):
    print(list[i],end='')
print('\n')

#Index operations
list = [1,2,2,3,3,4]
print(list.index(4))
print(list.index(2))#The same rule applies here as Remove operation like FCFS

''''#Clear Operations
list.clear()
for i in range(len(list)):
    print(list[i],end='')
print('\n')'''

#cCount operation
print(list.count(2))

#Sort operation
list.sort(reverse=  True  )
for i in range(len(list)):
    print(list[i],end='')
print('\n')
#list.sort(key)
for i in range(len(list)):
    print(list[i],end='')
print('\n')

#Extend operation
l1 = [1,2]
l2 = [3,4]
l1.extend(l2)
print(l1)

#To get th  e type
print(type(list))
