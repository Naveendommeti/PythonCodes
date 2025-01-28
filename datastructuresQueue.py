class Queue(object):
    def __init__(self):
        self.queue=[]

    def isempty (self):
        return self.queue==[]
    
    def enqueue(self,data):
        self.queue.insert(0,data)
        return data
    
    def dequeue(self):
       data= self.queue.pop()
       return data
    
if __name__=='__main__':
    ans= Queue()
    print (ans.enqueue(2))
    print (ans.enqueue(25))
    print (ans.enqueue(22))

    print (ans.dequeue())
    print (ans.dequeue())
    
    print (ans.isempty())



    