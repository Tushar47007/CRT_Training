'''print("Tushar\nMagare")
print('''"hello"''')
print("#hello#")
print("''hello''")
print("hello "+" dawg")
print("hello","dawg")
print(4+7+0+0+7)
print("2"+"3")
print("Addition is ",(3*2))
__hej__ = 1
__heej__ = 2
print("addition",__hej__+__heej__)
print("Substraction",__hej__-__heej__)
print("Multiply",__hej__*__heej__)
print("Division",__hej__/__heej__)
__p__ = input("Enter text here ")
__o__ = input("Enter text here ")
print(int(__p__+__o__))
print(5//2)
age = int(input("Enter the age"))
if(age>=18):
    print("Can Vote")
else:
    print("Nope")
grade = input("Enter the Grade")
if(grade == 'A'):
    print("Excellent")
elif(grade == 'B'):
    print("Very Good")
elif(grade == 'C'):
    print("Okay")
else:
    print("Fail")'''
marks = int(input("Enter the marks"))
if(marks <0 or marks >100):
    print("Invalid Input")
else:
    if(marks < 99 and marks >79):
        print("A Grade")
    else:
        print("Fail")
a = [5,6,7]
print(max(a))