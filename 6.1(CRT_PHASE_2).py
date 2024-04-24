'''a = 10
def fun():
    nonlocal a #Use global instead of nonlocal the nit works
    a+=1
    return a
print(fun())'''

class ABC:
    @staticmethod
    def fun(): #self is not used when using static method
              #Static method creates memory
        print('CSE')
obj = ABC()
obj.fun()

#Inheritence : Acquiring properties from base class
#1-> Single Inheritance
class A:
    def a1(self):
        print('A')
class B(A):
    def b1(self):
        print('B')

obj = B()
obj.a1(); obj.b1()

#2-> Multiple Inheritance
class nase1: #You need to use self keyword here
    def n1(self):
        print('nase1')
class nase2:
    def n2(self):
        print('nase2')
class serived(nase1, nase2):
    def n3(self):
        return 'Serived'
obj = serived()
obj.n2()
print(obj.n1()) #All these two will give output NONE because function does not return anything
print(obj.n2())
print(obj.n3())#This will work just fine

#3-> Multi-Level Inheritance : Goes level after level
class base1:
    def b1(self):
        print('base1')
class base2(base1):
    def b2(self):
        print('base2')
class base3(base2):
    def b3(self):
        print('base3')
class derived(base3):
    def sub(self):
        print('sub')
obj = derived()
obj.b1

#hierarchical Inherotence
class base:
    def b1(self):
        print('Base')
class sub1(base):
    def s1(self):
        print('sub1')
class sub2(base):
    def s2(self):
        print('sub2')
obj1 = sub1()
obj2 = sub2()
obj1.b1()
obj2.b1()