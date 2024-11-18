import json
import time
import random
import RPi.GPIO as GPIO



# Running indicator
print(f"I/O Handler Running....")

# Specify file being used for IO
IO_STATE_FILE = "io_state.json"

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
   
# Read data from JSON file
def read_io_state():
    try:
        with open(IO_STATE_FILE, "r") as file:
            state = json.load(file)
            return state
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file is missing or invalid, return default state
        return {"inputs": IO_Inputs, "outputs": IO_Outputs}
    
# Write inputs to JSON file
def write_io_state(state):
    with open(IO_STATE_FILE, "w") as file:
        json.dump(state, file, indent=4)


        
# Run main function on inf loop until keyboard interrupt (ctrl-c0.
# )
def main():
    try:
        while True:
            print(f'inputs ----------------')
            read_inputs()
            time.sleep(2)
            
            # Read outputs from frontend
            state = read_io_state()
            state['inputs'] = IO_Inputs
            
            write_io_state(state)
            
            
    except KeyboardInterrupt:
        print("")
        print("Exiting I/O Handler and cleaning up")
        GPIO.cleanup() #Cleanup GPIO on exit
        
main()





