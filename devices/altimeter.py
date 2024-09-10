from app.device import Device

class Altimeter(Device):
    def __init__(self, id = "0"):
        super().__init__()
        self.id = id
        self.name = self.__class__.__name__
    
    def register(self):
        return (f"{super().register()}{self.device_name()}") 
    
    def notify(self):
        return (f"{super().notify()}{self.device_name()}")  
 
    def device_name(self):
        return f"{super().device_name()}{self.name} {self.id}"
