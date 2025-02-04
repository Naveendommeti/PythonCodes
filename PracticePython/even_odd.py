#Even or Odd = Number divisible by 2 and returns 0 as remainder

def even_odd(n):
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"
num = int(input("Enter the num"))
print(even_odd(num))