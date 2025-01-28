from email import message
from unittest import expectedFailure, result



try:
    f= open ("message.txt" )
    
    content = f.read(3)
    print(content)
    
    morecontent = f.read(8)
    print(morecontent)
    f.close()
finally:
    f.close() 


with open("message.txt") as f :
    #  print (f.read())
    #  print (f.tell())
     f.seek(0)
     print (f.readline())

   # f.write("myself preetham\n")
    #  for line in f:
      #  print (line , end="")

with open("message.txt", "w") as f:
  f.write(" iloveprogramming")


import os #to know the locatin of the file
current_working_dir = os.getcwd
print(current_working_dir)


# import os 
# os.mkdir("test.py")


# import os 
# os.rename("loop","pythonfiles")

print (os.listdir())

#to remove flie os.remove(filename)
#to remove folder or directory of empty floder  os.rmdir(directory or folder name)
#to remove folder or directory of non empty floder  shutil.rmtree(directory or folder name)
#import shutil
#shutil.rmtree()


try:
  nume= int(input("enter a number: "))
  den= int(input("enter a number: "))
  result= (nume/den)
  print (result)
except:
  print("the den cnnot be 0. please try again")
print ("program ends")







    

    

