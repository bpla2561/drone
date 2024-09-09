from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def register(self):
        return dict["registration"] 
    
    @abstractmethod
    def notify(self):
        return dict["notification"]
        
    @abstractmethod
    def device_name(self):
        return dict["device"]
