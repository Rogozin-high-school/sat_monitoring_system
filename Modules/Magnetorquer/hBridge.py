from .. import config

GPIO_LOADED = False

if config.X_AXIS_H_BRIDGE_CONNECTED or config.Y_AXIS_H_BRIDGE_CONNECTED or config.Z_AXIS_H_BRIDGE_CONNECTED:
    try:
        import RPi.GPIO as GPIO
        GPIO_LOADED = True
    except RuntimeError:
        print("An error occured while importing RaspberryPi.GPIO")

class hBridge:

    def __init__(self, directionPort1, directionPort2, pwmPort1, pwmPort2):
        # Each h-bridge takes 4 ports
        # 2 ports that control the direction (1 port for each direction)
        # 2 ports that control the voltage, because out input is 5 volts and out output is
        #   constant 5 volts (or none) then these pins would always be turned on
        
        self.directionPort1 = directionPort1
        self.directionPort2 = directionPort2

        self.pwmPort1 = pwmPort1
        self.pwmPort2 = pwmPort2

        if GPIO_LOADED:
            if GPIO.getmode() != GPIO.BOARD:
                GPIO.setmode(GPIO.BOARD)
        
            GPIO.setup(directionPort1, GPIO.OUT)
            GPIO.setup(directionPort2, GPIO.OUT)
            GPIO.setup(pwmPort1, GPIO.OUT)
            GPIO.setup(pwmPort2, GPIO.OUT)

    def __del__(self):
        if GPIO_LOADED:
            GPIO.cleanup()


    def SetDirection(self, direction):
        # 0 - no voltage at all
        # 1 - positive voltage
        # -1 - negative voltage

        if GPIO_LOADED:
            if direction == 0:
                GPIO.output([self.directionPort1, self.directionPort2,
                    self.pwmPort1, self.pwmPort2], GPIO.LOW)

            elif direction == 1:
                GPIO.output([self.directionPort2, self.pwmPort1, self.pwmPort2], GPIO.HIGH)
                GPIO.output(self.directionPort1, GPIO.LOW)
            elif direction == -1:
                GPIO.output([self.directionPort1, self.pwmPort1, self.pwmPort2], GPIO.HIGH)
                GPIO.output(self.directionPort2, GPIO.LOW)
