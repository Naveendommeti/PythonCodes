#sum of first n natural nums
num= int (input("enter a num: "))
sum= num*(num+1)//2
print (sum)
#or 
num= int (input("enter a num: "))
sum=0
for i in range (num+1):
    sum=i+sum
print(sum)


def getsum(num):
    if num==1:
        return 1
    return num + getsum(num-1)

num=5
print (getsum(num))