
import machine
import utime

# Initialize the PIR sensor on GP16 pin
pir = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(28, machine.Pin.OUT)

print('Callibrating, please wait 40 sec')
seconds = 0
print(seconds,' sec')
while seconds < 60:
    utime.sleep(1)
    seconds += 1
    print(seconds, ' sec')
    
# Main loop
while True:
    # Check for motion detected by PIR sensor
    print('PIR Value: ', pir.value())
    current_time = utime.localtime()
    if pir.value() == 0:
        
        # Format the date and time as a string
        time_str = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])

        # Output the motion detected message to the screen with the time
        print("Motion detected at", time_str)
        led.high()
        utime.sleep(0.5)
        
    else:
        time_str = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])
        print("No Motion Detected at ", time_str)
        led.low()
        

    # Wait for 0.1 seconds before checking again
    utime.sleep(3)

