import json
import time
import random
import RPi.GPIO as GPIO



# Running indicator
print(f"I/O Handler Running....")

# Specify file being used for IO
IO_STATE_FILE = "io_sate.json"

#IO variable Initialization
IO_Inputs = [0, 0, 0] # 3 PLC Inputs
IO_Outputs = [0, 0, 0, 0, 0, 0, 0, 0] # 8 Channel Relay

# Set up IO pins
## Specify we are using BOARD Numbering system for IO Pins and clean up GPIO in case it's still running

GPIO.setmode(GPIO.BCM)

inputChanList = [16, 20, 21]

GPIO.setup(inputChanList, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Initialize to inputs with pulldown resistor

# Function to read inputs from PLC
def read_inputs():
    for i, pin in enumerate(inputChanList):
        IO_Inputs[i] = GPIO.input(pin)
        print(f"Input {i+1}: {IO_Inputs[i]}")
        

def main():
    try:
        while True:
            print(f'inputs ----------------')
            read_inputs()
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Exiting I/O Handler and cleaning up")
        GPIO.cleanup() #Cleanup GPIO on exit
        
main()





