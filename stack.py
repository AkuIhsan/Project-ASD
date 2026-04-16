class Stack :
    def __init__(self):      
        self.data = []

    def push(self, item) :      
        self.data.append(item) 
        return
    
    def pop(self) :
        item = self.data.pop()
        return item
    
    def peek(self) :
        item = self.data[-1]
        return item

    def isEmpty(self) :
        if not len(self.data) : return True
        return False
    
    def Size(self) :
        if self.isEmpty() : 
            print("Stack dalam kondisi kosong")
            return
        
        return len(self.data)






    
