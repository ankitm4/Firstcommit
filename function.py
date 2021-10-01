#creating functions

def sum(*args): #here the *args is a tuple
   rel=0
   for i in args:
      rel+=i
   x=str(rel)
   print("the sum of the numbers is "+ x )

sum(1,2,3,4,5)

def key(**key):#**kwargs for passing of dictionary
   for key,value in key.items():
      print(" {} of is {} ".format(key,value))
  

key(name1="ankit",name="Sam")

def name(name="ankit"): #if no argument is passed it will the deafult argument
    if type(name)==list:
        for i in name:
           return i
    else:
        print(name)

name("rahul")
name()
alp= ["a","n","k"]
print(name(alp))#this will print only "a" as return will end the function


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
print(fact(5))


#lambda functions
#an function with many arguments but with one expression
s=lambda x:x**2
print(s(5))
mlist = [1, 5, 4, 6, 8, 11, 3, 12]

square=lambda x:x**2
nlist=list(map(square,mlist))
print(nlist)

even=lambda x:x%2==0
evennum=list(filter(even,mlist))
print(evennum)

x= 2
def find():
    global x
    x=x*2
    print(x)
find()
print(x)