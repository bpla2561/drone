class MyIterator:
    
    def __init__(self, list):
        self.list = list
        self.max = len(list) - 1
        self.current = -1
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.current < self.max:
            self.current += 1
            return self.list[self.current]
        else:
            raise StopIteration
