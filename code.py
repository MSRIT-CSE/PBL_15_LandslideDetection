import RPi.GPIO as GPIO
import dht11
import time
from ubidots import ApiClient

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(11,GPIO.IN)
#GPIO.setup(7,GPIO.IN)
GPIO.setup(21,GPIO.IN)

#Create an "API" object
#pin 11 for vibration ,8 for temperature,21 for  moisture
api = ApiClient("46e1a0d7f656a8cbfbbdba47f6f0362e757d4acc")

#Create a "Variable" object
#temperature
test_variable = api.get_variable("5669cafa762542094821a3da")
#humidity
test1_variable = api.get_variable("5669cae676254205debec9d4")
#vibration
test2_variable = api.get_variable("563851ed76254254e37bafb7")
#moisture
test3_variable = api.get_variable("5669cb13762542067f4dfe82")

# read data using pin 8
instance = dht11.DHT11(pin = 8)
result = instance.read()
#result1 has vibration values
result1= GPIO.input(11)
time.sleep(0.1)
#current state has  moisture
current_state = GPIO.input(21)


if result.is_valid():
        test_variable.save_value({'value':result.temperature})
        test1_variable.save_value({'value':result.humidity})

else:
    print("Error: %d" % result.error_code)
test3_variable.save_value({'value':current_state})

while True:

        if GPIO.input(11):
                print("its vibrating")
                test2_variable.save_value({'value':result1})
                time.sleep(1)
        else:
                print("no vibration")
                time.sleep(1)
                                              