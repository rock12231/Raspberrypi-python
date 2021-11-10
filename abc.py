import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(38,GPIO.HIGH)
    print("Trun ON")
    sleep(0.051)
    GPIO.output(38,GPIO.LOW)
    print("Trun OFF")
    sleep(0.051)
    GPIO.output(38,GPIO.HIGH)
    print("Trun ON")
    sleep(0.051)
    GPIO.output(38,GPIO.LOW)
    print("Trun OFF")
    sleep(0.051)
    GPIO.output(38,GPIO.LOW)
    print("OFF 2sec")
    sleep(2)