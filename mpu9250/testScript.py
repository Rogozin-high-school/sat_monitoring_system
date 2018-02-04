import mpu9250 as mpu
import time

magnetometer = mpu.mpu9250()

while True:
    print "Magnetometer" + str(magnetometer.mag)
    print "Aceleromter" + str(magnetometer.accel)
    print "Gyro" + str(magnetometer.gyro)
    print " ------------------- "
    time.sleep(0.1)
