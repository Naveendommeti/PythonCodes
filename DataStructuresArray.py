import array as arr

a= arr.array ('d',[1.1,2,3.2,5.5,6.9])
a.append(2.3)
print ("the appended value arr is {} then ".format([2.3]),a)

a.extend([3,8,9])

print ("the appended value arr is {} then ".format([3,8,9]),a)

print (a.pop(2))
