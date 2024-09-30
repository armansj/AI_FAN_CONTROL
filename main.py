from machine import Pin, PWM, Timer
import time
import uasyncio as asyncio

servo_pin = Pin(0, Pin.OUT)
trigger_pin = Pin(1, Pin.OUT)
echo_pin = Pin(2, Pin.IN)
buzzer_pin = Pin(3, Pin.OUT)

servo_pwm = PWM(servo_pin)
servo_pwm.freq(50)


def move_servo(angle):
    min_duty = 1000
    max_duty = 2000
    duty = int((angle / 180.0) * (max_duty - min_duty) + min_duty)

    servo_pwm.duty_u16(int(duty * 65536 / 20000))


def get_distance():
    trigger_pin.value(0)
    time.sleep_us(2)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration / 2) / 29.1  # Convert to cm
    return distance


def beep_buzzer(on):
    buzzer_pin.value(1 if on else 0)


async def radar_scan():
    angle = 0
    step = 5
    while True:
        move_servo(angle)
        await asyncio.sleep(0.05)

        distance = get_distance()
        print(f"Angle: {angle}, Distance: {distance} cm")

        if distance < 10:
            beep_buzzer(True)
        else:
            beep_buzzer(False)

        angle += step
        if angle > 180 or angle < 0:
            step = -step

        await asyncio.sleep(0.05)


asyncio.run(radar_scan())

