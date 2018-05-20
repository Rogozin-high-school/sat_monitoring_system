from Modules.Runtime.environment import SAT

if SAT:
    from Modules.Magnetometer import magnetometer_factory
    from Modules.Magnetorquer.hBridge import hBridge

from Modules.DataHub.remote import DataHub

import time
import math

if SAT:
    sensor = magnetometer_factory.initialize()
    actuator = hBridge(23, 24, 14, 15)

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

def setMagnetorquer(axis):
    actuator.SetDirection(axis)
    time.sleep(0.5)
    actuator.SetDirection(0)
    time.sleep(0.05)

while True:

    print("Trying to read magnetorquer commands")
    mag = hub.get(["sat_magnetorquer"])[0]
    print("Received magnetorquer command: " + str(mag))
    if mag["success"] and mag["content"]:
        print("Activating magnetorquer")
        setMagnetorquer(mag["content"])

    
    print("Reading magnetometer info")
    hub.set({"sat_mag": readMagnet()})
    print("Sent magnetometer info to DataHub")

    time.sleep(0.125)