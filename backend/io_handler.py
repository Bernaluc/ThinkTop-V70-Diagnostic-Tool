import json
import time
import random
import RPi.GPIO as GPIO
import smbus2


# Running indicator
print(f"I/O Handler Running....")

# CONSTANT DEFINITIONS
IO_STATE_FILE = "io_state.json" # Specify file being used for IO
I2C_CHANNEL = 1 # pi I2C channel
DEVICE_ADDRESS = 0x27 # Relay board address

#IO variable Initialization
IO_Inputs = [0, 0, 0, 0, 0, 0] # 3 PLC inputs, 3 Valve Inputs
IO_Outputs = [0, 0, 0, 0, 0, 0, 0, 0] # 8 Channel Relay
relayState = 0b00000000 # LSB is relay 8, MSB is relay 1

# Set up IO-----------------------------------

## Specify we are using BOARD Numbering system for IO Pins and clean up GPIO in case it's still running

GPIO.setmode(GPIO.BCM)

inputChanList = [16, 20, 21, 13, 19, 26]

GPIO.setup(inputChanList, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Initialize to inputs with pulldown resistor

## Set up I2C bus
bus = smbus2.SMBus(I2C_CHANNEL)



# Functions ----------------------------------

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

# Function to set relays
def set_relays(state):
    try:
        bus.write_byte(DEVICE_ADDRESS, state)
        print(f"Relays updated: {bin(state)}")
    except Exception as e:
        print(f"Error setting relays: {e}")
        
# Run main function on inf loop until keyboard interrupt (ctrl-c0.
# )
def main():
    try:
        while True:
            print(f'inputs ----------------')
            read_inputs()
            time.sleep(1)
            
            # Read outputs from frontend
            state = read_io_state()
            state['inputs'] = IO_Inputs
            
            write_io_state(state)
            
            relayState = 0b11111111  # All relays off initially (all bits set to 1)

            # Turn on each relay sequentially (only one bit set to 0 at a time)
            for i in range(8):
                relayState = ~(1 << i) & 0b11111111  # Set the i-th bit to 0, ensuring all others are 1
                set_relays(relayState)
                time.sleep(1)

            # Turn off all relays (set all bits back to 1)
            relayState = 0b11111111
            set_relays(relayState)

            
            
    except KeyboardInterrupt:
        print("")
        print("Exiting I/O Handler and cleaning up")
        GPIO.cleanup() #Cleanup GPIO on exit
        
    
        
main()





