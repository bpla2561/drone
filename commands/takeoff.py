from app.command import Command
from models.drone import Drone
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

class TakeOff(Command):
    def __init__(self, drone: Drone):
        self._drone = drone

    def execute(self):
        self._drone.take_off()
        logging.info("Взлет выполнен")

    def undo(self):
        self._drone.land()

