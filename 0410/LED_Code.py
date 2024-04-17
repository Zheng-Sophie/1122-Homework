import RPi.GPIO as GPIO
import time

# 一個閃五次
LED_PIN = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

a=5
while a>0:
  print("HIGH")
  GPIO.output(LED_PIN,GPIO.HIGH)
  time.sleep(0.2)
  print("LOW")
  GPIO.output(LED_PIN,GPIO.LOW)
  time.sleep(0.2)
  a-=1
GPIO.cleanup()

# 四個閃五次
LED_PIN = [2,3,5,6]
GPIO.setmode(GPIO.BCM)
for i in LED_PIN:
 GPIO.setup(i, GPIO.OUT)
 GPIO.output(i,GPIO.HIGH)
# 閃指定次數
# N = eval(input('LOOP NUMBER = '))
# a = N
# while a > 0:
a=1
while a<6:
  print("LOOP %d"%a)
  for i in LED_PIN:
   print ('LED %d is ON'%i,end = ', ')
   GPIO.output(i,GPIO.LOW)
   time.sleep(0.2)
   print ("LED %d is OFF"%i)
   GPIO.output(i,GPIO.HIGH)
  a+=1
GPIO.cleanup()

