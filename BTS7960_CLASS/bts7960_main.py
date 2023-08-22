import machine
import utime
import BTS7960MotorDriver

# Example usage:
motor = BTS7960MotorDriver(pwm_pin=0, in1_pin=1, in2_pin=2)  # Adjust pin numbers
motor.control_motor(speed=50, direction="forward")