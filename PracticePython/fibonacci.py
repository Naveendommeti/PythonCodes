#fibonacci series formula f(n) = f(n-1) +  f(n-2)

def fib_series(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib_series(a-1) + fib_series(a-2)
num = int(input("Enter the number: "))
for i in range(num):
    print(fib_series(i), end=" ")