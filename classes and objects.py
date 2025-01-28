




class student:
    def check_passorfail(self):
        if self.marks <=39:
            return False
        else: 
            return True
    
student1 = student()
student1.name="harry"
student1.marks=99  

didpassorfail = student1.check_passorfail()  
print (didpassorfail)

student2 = student()
student2.name = ("itadori")
student2.marks= 39
didpassorfail2 = student2.check_passorfail()
print (didpassorfail2)



#using constructor creating class

class student :
    def checkpassorfail(self):  #self (parameter) self represents student1
                            #object and also student1 attribute(variable)
                            #marks in object i.e student1, same goes for student2
        if self.marks >=39:
            return True
        else:
            return False

#consrtructor __init__ to pass variables also known as attribues 
    def __init__(self,name,marks ):
        self.name = name 
        self.marks = marks

#objject creation 
#objjectname= classname(arguments_values)
student1= student("scout",28)
student2= student("mortal",99)
didpass1=student1.checkpassorfail()
didpass2=student2.checkpassorfail()
print (didpass1)
print (didpass2)



#adding complex numbers

class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    def add(self,num):
        real= self.real+num.real
        imag= self.imag+num.imag
        result = Complex(real,imag)
        return (result)


n1 = Complex(3,4)
n2 = Complex(5,6) 
result = n1.add(n2)
print (result.real)
print (result.imag)


#creating class triangle problem

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def perimeter (self):
        add= self.a+ self.b +self.c
        return (add)

t1= Triangle(3,4,5)
result=t1.perimeter()
print (result)



#add and mul two num

class maths:
    def __init__(self,a,b):
        self.a=a
        self.b = b

    def addandmul(self):
        add= self.a +self.b
        mul= self.a*self.b
        return add,mul
        
    

ob= maths(5,6)
result= ob.addandmul()
print (result)








  




        
    




        
