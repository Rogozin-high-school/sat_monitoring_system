import mpu9250
import time

magnetometer = mpu9250.mpu9250()

while True:
    print "Magnetometer" + str(magnetometer.mag)
    time.sleep(0.1)
