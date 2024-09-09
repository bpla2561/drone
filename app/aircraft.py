from abc import ABC, abstractmethod

class Aircraft(ABC):
    @abstractmethod  
    def __init__(self, drone_id) -> None:
        self.drone_id = drone_id 
        self.latitude: 'latitude'
        self.longitude: 'longitude'
        self.altitude: 'altitude'
        self.is_flying: False

    @abstractmethod  
    def takeoff(self):
        pass

    @abstractmethod  
    def take_off(self):
        pass

    @abstractmethod  
    def change_course(self, new_course):
        pass

    @abstractmethod  
    def land(self):
        pass
    