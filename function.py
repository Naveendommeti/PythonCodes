# def hello():
    # print("hello preetham")
# hello()
# 
# 
# 
# def hello(fname):
    # print(fname +" "+ "preetham")
# hello("dommeti")
# hello("pree")
# hello("preeee")
# 
# 
# 
# def hello(fname, lname):
    # print(fname +" "+ lname)
# 
# hello("dommeti","preetham")
# hello("dommeti","pree")
# 
# 
# args(*)
# def hello(*names):
    # print("the name of last one "+ names[3])
# 
# hello("dommeti","preetham","pree","mikey")
# 
# 
# 
# def hello(**names):
    # print("the lname of 3rd is "+ names["lname"])
# 
#hello(fname="dommeti",lname="preetham")
# 
# 
# 
# def my_function(food):
#   for x in food:
    # print(x)
# 
# food = ["apple", "banana", "cherry"]
# 
# (my_function(food))
# 
# 
# 
# 
# def my_function(x):
#   return(5 * x)
# 
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# 
# 
# recursion 
# from re import X
# 
# 
# def fact(n):
    # if n==1:
        # return n
    # else:
        # return n*fact(n-1)        
# print (fact(6))




from re import X
from tkinter import N


double = lambda x : x*2
print (double(5)) 



def double (n):
    return n*2
print (double(5))



# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

newlist = list(filter(lambda x: x%2==0, my_list       ))
print (newlist)


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

newlist = list(map(lambda x : x*2 , my_list       ))
print (newlist)


def add(n1,n2):
    sum= n1+n2
    return sum
n1=4
n2=5
result= add(n1,n2)
print ("sum = " , result)




#5 and -5 is 5
def get_absolute(n):
    if n>=0 :
        return (n)
    elif n<=0:
        return (-n)
    else:
        return("over")

print (get_absolute(5))
print (get_absolute(-5))
    


def myfunc(x):
    x=10
    return x
print (myfunc(10)) 
#name error beacause we should call inside the func it will be local to the myfunc



def greet(msg = "Good morning!", name= "preetham"):
    return ("heelloo", msg + name )



st= "python"
print (st[2:-2])



