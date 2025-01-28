class stack(object):
    def __init__(self):
        self.stack=[]
        self.numofitems=0

    def isempty(self):
        return self.stack==[]
    
    def push(self,data):
        self.numofitems+=1
        self.stack.insert(self.numofitems,data) 
        # "class"(here it is 'stack') is used when the methods are used or called 
        return ("{} the pushed data ".format(data))
        #return data
    
    def pop(self):
        self.numofitems-=1
        data=self.stack.pop(self.numofitems)
        #data (var) is used to get the data deleted data
        return ("{} poped data".format(data))
        #or 
        #return data
    
    def stacksize(self):
        return len(self.stack)

if __name__=='__main__':
    ans=stack()
    print (ans.push(5))
    print (ans.push(8))
    print (ans.push(9))
    print (ans.push(2))
    print (ans.push(7))

    print (ans.pop())
    print (ans.pop())
    
    print (ans.stacksize())
    
    
         