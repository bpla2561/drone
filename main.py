from flask import Flask, Response, request, jsonify, g, make_response
from commands.move_forward import MoveForward
from commands.land import Land
from commands.takeoff import TakeOff
from devices.altimeter import Altimeter
from devices.camera import  Camera
from devices.lidar import  Lidar
from models.drone import Drone
from pyinstrument import Profiler
from utils.my_observer import MyObserver
from utils.remote_control import RemoteControl
from utils.weather_check import weathercheck
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"index": "All about Drones"}), 200

@app.route("/remote_control/", methods=["GET"])
@weathercheck()
def remote_control():
    route = request.args.get('route')
    targets = route.split('\n')

    drone = Drone()

    my_observer = MyObserver() 
    my_observer.append(Lidar("001"))
    my_observer.append(Altimeter("001"))
    drone.devices_update = my_observer.update()

    land = Land(drone)
    take_off = TakeOff(drone)

    remote_control = RemoteControl()

    remote_control.add_command(take_off)

    for target in targets:
        move_forward = MoveForward(drone, target.strip("'"))
        remote_control.add_command(move_forward)
        camera = Camera(drone, target.strip("'"))
        remote_control.add_command(camera)
    
    remote_control.add_command(land)

    remote_control.execute_commands()
    remote_control.undo_command()
    
    drone_path = drone.drone_path(route)
    total_distance = drone_path.calculate_total_distance()

    drone.result = f"Полет дрона с ID: {drone.drone_id} по маршруту: {route} завершен. Длина маршрута: {total_distance}."
    drone.notifier_update()
    return jsonify({"remote_control": drone.result}), 200

@app.before_request
def before_request():
    g.is_profiling = "profile" in request.args
    if g.is_profiling:
        g.profile = Profiler()
        g.profile.start()

@app.after_request
def after_request(response):
    if g.is_profiling:
        g.profile.stop()
        output_html = g.profile.output_html()
        return make_response(output_html)
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
