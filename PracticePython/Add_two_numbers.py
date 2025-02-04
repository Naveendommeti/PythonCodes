# def add_numbers(a,b):
#     return a+b
# n1 = float(input("Enter n1: "))
# n2 = float(input("Enter n2: "))
# result = add_numbers(n1,n2)
# print("Sum of two number is: ", result)

def add_numbers(*args):
    return sum(args)
numbers = list(map(float,input("Enter the numbers: ").split()))
result = add_numbers(*numbers)
print("Sum of the num: ", result)