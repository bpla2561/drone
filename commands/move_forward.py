from app.command import Command
from models.drone import Drone
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

class MoveForward(Command):
    def __init__(self, drone: Drone, target: float):
        self.__drone = drone
        self.__target = target

    def execute(self):
        self.__drone.move_forward(self.__target)
        logging.info(f"Движение на точку {self.__target}")

    def undo(self):
        print("Отмена команды невозможна")
