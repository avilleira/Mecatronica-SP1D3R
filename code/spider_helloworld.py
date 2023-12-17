import RPi.GPIO as GPIO
import time

# File: spider_helloworld.py

# CONSTANTS
FREQUENCE = 50
MAXANGLES = 180
SLEEPTIME = 0.003

# Leg ports dictionary
leg_ports = {
    'front_right': [3, 5, 7]
}

class SpiderLeg:
    # Constructor method
    def __init__(self, coxa, femur, tibia):
        self.coxa = coxa
        self.femur = femur
        self.tibia = tibia

        # Stablish as output ports:
        GPIO.setup(self.coxa, GPIO.OUT)
        GPIO.setup(self.femur, GPIO.OUT)
        GPIO.setup(self.tibia, GPIO.OUT)

        # PWM modulation
        self.coxa = GPIO.PWM(self.coxa, FREQUENCE)
        self.femur = GPIO.PWM(self.femur, FREQUENCE)
        self.tibia = GPIO.PWM(self.tibia, FREQUENCE)

        #Initial angles
        self.coxa.start(angle_to_percent(90))
        self.femur.start(angle_to_percent(150))
        self.tibia.start(angle_to_percent(160))

    # To greet method
    def greet(self):
        for times in range(2):
            # Wave down
            for angle in range(160, -1, -1):
                self.tibia.ChangeDutyCycle(angle_to_percent(angle))
                time.sleep(SLEEPTIME)
            # Wave up
            for angle in range(161):
                self.tibia.ChangeDutyCycle(angle_to_percent(angle))
                time.sleep(SLEEPTIME)

    def kill(self):
        self.coxa.stop()
        self.femur.stop()
        self.tibia.stop()

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calculate ratio from angle to percent
    angle_as_percent = angle * ratio

    return start + angle_as_percent

def main ():

    print("SPIDER SAYS HELLO!")
    GPIO.setmode(GPIO.BOARD)
    front_right_leg = SpiderLeg(*leg_ports['front_right'])
    time.sleep(1)
    front_right_leg.greet()
    GPIO.cleanup()

if  __name__ == "__main__":
    main()