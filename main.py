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

while True:

    if SAT:
        axes = sensor.readMagnet()
        magnitude = math.sqrt(sum([x ** 2 for x in axes]))

    else:
        axes = [0, 0, 0]
        magnitude = 0

    print("Updating DataHub")
    hub.set({"sat_mag": [axes, magnitude]})
    print("Updated DataHub")

    time.sleep(0.1)