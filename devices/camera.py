from app.command import Command
from models.drone import Drone
import logging
import cv2

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

class Camera(Command): 
    def __init__(self, drone: Drone, target):
        self._drone = drone
        self._zoom_lvl = 1.0
        self.filename = target

    def set_zoom(self, zoom_lvl: float):
        self._zoom_lvl = zoom_lvl

    def execute(self):
        caption = cv2.VideoCapture(0)
        ret, frame = caption.read()
        if ret:
            filename = self.filename + ".jpg"
            cv2.imwrite(filename, frame)
        logging.info("Фото сделано")
        caption.release()

    def undo(self):
        print("Отмена невозможна")
