import machine
import utime

# Pin configuration
STEP_PIN = machine.Pin(15, machine.Pin.OUT)
DIR_PIN = machine.Pin(14, machine.Pin.OUT)
ENABLE_PIN = machine.Pin(13, machine.Pin.OUT)  # Enable pin for DRV8825

# Disable the motor driver by default (can be enabled later)
ENABLE_PIN.value(1)

# Initialize stepper motor control
steps_per_revolution = 3200  # Steps for 1 full revolution with 1/16 microstepping
delay = 0.001  # Delay between steps (adjust for speed)

# Function to enable the motor driver
def enable_motor():
    ENABLE_PIN.value(0)

# Function to disable the motor driver
def disable_motor():
    ENABLE_PIN.value(1)

# Function to rotate the motor clockwise
def rotate_clockwise(steps):
    DIR_PIN.value(1)  # Set direction to clockwise
    for _ in range(steps):
        STEP_PIN.value(1)
        utime.sleep_us(int(delay * 1e6))
        STEP_PIN.value(0)
        utime.sleep_us(int(delay * 1e6))

# Function to rotate the motor anticlockwise
def rotate_anticlockwise(steps):
    DIR_PIN.value(0)  # Set direction to anticlockwise
    for _ in range(steps):
        STEP_PIN.value(1)
        utime.sleep_us(int(delay * 1e6))
        STEP_PIN.value(0)
        utime.sleep_us(int(delay * 1e6))

# Rotate the motor
try:
    enable_motor()  # Enable the motor driver
    for i in range(10):
       # Rotate clockwise for 200 steps (approximately half a revolution)
       rotate_clockwise(100)
    
      # Pause for 1 second
       utime.sleep(1)
    
      # Rotate anticlockwise for 200 steps
       rotate_anticlockwise(-100)
       utime.sleep(1)
    
       rotate_clockwise(200)
                     
except KeyboardInterrupt:
    pass
finally:
    disable_motor()  # Disable the motor driver

    # Turn off the motor
    DIR_PIN.value(0)
    STEP_PIN.value(0)
