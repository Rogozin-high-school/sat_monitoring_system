from Modules.Runtime.environment import SAT

if SAT:
    from Modules.Magnetometer import magnetometer_factory
    from Modules.Magnetorquer.hBridge import hBridge

from Modules.DataHub.remote import DataHub

import time
import math
import threading

if SAT:
    sensor = magnetometer_factory.initialize()
    actuator = hBridge(21, 5, 16, 20)

hub = DataHub("http://rogozin.space/varserver/")

print("Trying to achieve ground station address...")
req = hub.get(["lab_ip", "lab_port"])
lab_addr = "http://" + req[0]["content"] + ":" + str(req[1]["content"])

hub = DataHub(lab_addr)
hub.set_endpoints("/get", "/set")

def readMagnet():
    if SAT:
        global senor
        axes = sensor.readMagnet()
        axes = [axes["x"], axes["y"], axes["z"]]
        return [axes, 0]
    else:
        return [[0, 0, 0], 0]

magnetometer_value, magnetorquer_value, _working = None, None, True

def network_thread():
    global _working, magnetometer_value, magnetorquer_value
    while _working:
        try:
            print("Updating the server with magnetometer value")
            hub.set({"sat_mag": magnetometer_value})
        except:
            print("An error occured while updating the server")

        try:
            print("Querying the server for magnetorquer commands")
            magnetorquer_value = hub.get(["sat_magnetorquer"])[0]["content"]
        except:
            print("An error occured while querying the server")

t = threading.Thread(target=network_thread)
t.start()

while True:
    try:
        if magnetorquer_value:
            actuator.SetDirection(magnetorquer_value)
            time.sleep(0.5)
            actuator.SetDirection(0)
            time.sleep(0.05)
        
        magnetometer_value = readMagnet()
        if not magnetorquer_value:
            time.sleep(0.15)

    except KeyboardInterrupt:
        actuator.SetDirection(0)
        break

_working = False