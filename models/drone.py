from app.aircraft import Aircraft
from utils.drone_path import DronePath
from utils.decorator import SMSNotifier, PhotoNotifierDecorator, WhatsappNotifierDecorator, TelegramNotifierDecorator, RocketNotifierDecorator
import logging
import requests

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

class Drone():
    def __init__(self, drone_path = DronePath, drone_id = "0001") -> None:
        self.drone_id = drone_id 
        self.latitude: 'latitude'
        self.longitude: 'longitude'
        self.altitude: 'altitude'
        self.is_flying: False
        self.result = None
        self.drone_path = drone_path
        self.devices_update = None


    def take_off(self):
        return "Дрон взлетает"

    def move_forward(self, new_target):
        return (f"Дрон движется на точку {new_target}")

    def land(self):
        return "Дрон приземлился"
    
    def camera(self):
        return "Фото сделано"
    

    def notifier_update(self):
        notifier = SMSNotifier(phone="+1232353245")
        notifier = PhotoNotifierDecorator(notifier)
        notifier = WhatsappNotifierDecorator(notifier, whatsapp_id="+1232353245")
        notifier = TelegramNotifierDecorator(notifier, telegram_id="@EgorMv")
        notifier = RocketNotifierDecorator(notifier, number_rocket=1)

        notifier.send(self.result)
        logging.info(f"Notifier: {self.result}"), 200

