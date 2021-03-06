from . import config

# Checking if Rpi.GPIO is loaded to avoid using it
# without it being loaded
GPIO_LOADED = False

# Try import raspberry pi's gpio library
try:
    import RPi.GPIO as GPIO
    GPIO_LOADED = True
except RuntimeError:
    print("An error occured while importing RaspberryPi.GPIO")

class hBridge:
    '''
    This class is used to create voltage on the magnetorquers that will change the current and thus will change the magnetic field
    '''

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
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
        
            GPIO.setup(directionPort1, GPIO.OUT)
            GPIO.setup(directionPort2, GPIO.OUT)
            GPIO.setup(pwmPort1, GPIO.OUT)
            GPIO.setup(pwmPort2, GPIO.OUT)

    def __del__(self):
        """ Releasing GPIO pins when the program ends """
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
