def factorial_rec(a):
    if a ==0 or a ==1:
        return 1
    return a*factorial_rec(a-1)
number = int(input("Enter the number: "))
if number<0:
    print("It is not defined: ")
else:
    print(f"Factorial of {number} is {factorial_rec(number)}")