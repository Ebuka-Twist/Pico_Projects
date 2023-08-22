from machine import Pin, PWM

class BTS7960MotorDriver:
    def __init__(self, pwm_pin, in1_pin, in2_pin):
        self.pwm = PWM(pwm_pin)
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        if speed > 0:
            self.in1.value(1)
            self.in2.value(0)
            self.pwm.duty(int(speed * 1023 / 100))  # Map speed to PWM range
        elif speed < 0:
            self.in1.value(0)
            self.in2.value(1)
            self.pwm.duty(int(-speed * 1023 / 100))  # Map speed to PWM range
        else:
            self.in1.value(0)
            self.in2.value(0)
            self.pwm.duty(0)

    def stop(self):
        self.set_speed(0)

    def control_motor(self, speed, direction):
        if direction == "forward":
            self.set_speed(speed)
        elif direction == "backward":
            self.set_speed(-speed)
        elif direction == "stop":
            self.stop()
        else:
            print("Invalid direction")

try:
    while True:
# Example usage:
        motor = BTS7960MotorDriver(pwm_pin=5, in1_pin=3, in2_pin=4)  # Adjust pin numbers
        motor.control_motor(speed=50, direction="forward")
except KeyboardInterrupt:
    pass

# Turn off the motor        