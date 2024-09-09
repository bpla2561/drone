from utils.my_Iterator import MyIterator
import json


class MyObserver:
    
    def __init__(self):
        self._observers = []  
    
    def append(self, observer):
        self._observers.append(observer)

    def update(self):
        result = []
        for observer in MyIterator(self._observers):
            result.append(observer.register())
            result.append(observer.notify())
        #print(observer)
        string_result = json.dumps(result)
        return string_result
