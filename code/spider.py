import RPi.GPIO as GPIO
import pigpio, sys
import time


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent



def main():
    print("INIT FUNCTION")
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    
    #Use pin 12 for PWM signal
    pwm_gpio = 40
    frequence = 50
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    
    #Init at 0°
    pwm.start(angle_to_percent(int(sys.argv[1])))
    time.sleep(1)
    
    #Go at 90°
    #pwm.ChangeDutyCycle(angle_to_percent(90))
    #time.sleep(1)
    
    #Finish at 180°

    time.sleep(1)
    
    #Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()

if  __name__ == "__main__":
    main()