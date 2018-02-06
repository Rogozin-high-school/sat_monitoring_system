import mpu9250
import time

magnetometer = mpu9250.mpu9250()

while True:
    print "Magnetometer" + str(magnetometer.mag)
    print "Aceleromter" + str(magnetometer.accel)
    print "Gyro" + str(magnetometer.gyro)
    print " ------------------- "
    time.sleep(0.1)
