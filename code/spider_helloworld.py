import RPi.GPIO as GPIO

# File: spider_helloworld.py

# CONSTANTS

class SpiderLeg:
    # Constructor method
    def __init__(self, coxa, femur, tibia):

        self.coxa = coxa
        self.femur = femur
        self.tibia = tibia


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

def main ():
    print("SPIDER SAYS HELLO!")


if  __name__ == "__main__":
    main()