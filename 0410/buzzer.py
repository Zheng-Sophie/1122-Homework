import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
def buzzer():
    GPIO.setmode(GPIO.BCM)
    # define the pin we will attach to
    GPIO_PIN = 12
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    # start at 50 hertz
    GPFrequency = 50
    pwm = GPIO.PWM(GPIO_PIN, GPFrequency)
    pwm.start(50)
    pwm.ChangeFrequency(2222)
    time.sleep(0.3)
    pwm.stop()
    GPIO.cleanup()
buzzer()