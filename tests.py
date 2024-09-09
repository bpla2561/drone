import unittest
from models.drone import Drone

class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone = Drone("111")
    
    def test_take_off_on_True(self):
        res = self.drone.take_off() 
        self.assertEqual(res, "Дрон взлетает")
        
    def test_take_off_on_False(self):
        res = self.drone.take_off() 
        self.assertNotEqual(res, "взлет не разрешен")
       
    def test_landing_on_True(self):
        res = self.drone.land() 
        self.assertEqual(res, "Дрон приземлился")
    
    def test_landing_on_False(self):
        res = self.drone.land() 
        self.assertNotEqual(res, "Drone уже на земле")
 
   
if __name__ == "__main__":
    unittest.main()  