from app.command import Command
from models.drone import Drone
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

class Land(Command):

    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.land()
        logging.info("Посадка выполнена")

    def undo(self):
        print("Отмена посадки невозможна")
        
