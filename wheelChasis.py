import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) #Standby/Enable pin set GPIO 17...
GPIO.output(17, GPIO.HIGH)

class Motor():
    def __init__(self, In1, In2, pwm):
        self.In1 = In1
        self.In2 = In2
        self.pwm = pwm
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        GPIO.setup(self.pwm,GPIO.OUT)
        self.speed = GPIO.PWM(self.pwm, 100)
        self.speed.start(0)
        
    def moveF(self, x=50, t=0):
       
        GPIO.output(self.In1, GPIO.LOW) 
        GPIO.output(self.In2, GPIO.HIGH)
        self.speed.ChangeDutyCycle(x)
        time.sleep(t)

    def moveB(self, x=50, t=0):
        GPIO.output(self.In1, GPIO.HIGH) 
        GPIO.output(self.In2, GPIO.LOW)
        self.speed.ChangeDutyCycle(x)
        time.sleep(t)
        
    def stop(self, t=0):
        self.speed.ChangeDutyCycle(0)
        time.sleep(t)

print("Motor1 and 2 initialisation")
motor1 = Motor(22,27,23)
#motor2 = Motor(5,6,16)

while True:
    print('Loop running')
    
    motor1.moveF(100,1)
    #motor2.moveF(75,1)
    motor1.stop(1)
    #motor2.stop(1)
    motor1.moveB(100,1)
    #motor2.moveB(100,1)
    motor1.stop(1)
    #motor2.stop(1)