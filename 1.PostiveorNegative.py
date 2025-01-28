#1 brute force
i= -22
if i<0:
    if i==0:
        print ("zero")
    else:
        print("n")
  
elif i>0:
    print('p')

#2 even or odd
num= int (input("enter a num: "))
if num%2==0:
    print("even")
else :
    print ("odd")

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


def getsum():
    if num==1:
        return 1
    return num + getsum(num-1)
print (getsum(num))



    


