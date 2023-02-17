import machine
import utime

# Initialize the PIR sensor on GP14 pin
pir = machine.Pin(14, machine.Pin.IN)

# Main loop
print('hi')
while True:
    print('hi2')
    # Check for motion detected by PIR sensor
    if pir.value() == 0:
        print('hi3')
        # Get the current date and time
        current_time = utime.localtime()

        # Format the date and time as a string
        time_str = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])

        # Output the motion detected message to the screen with the time
        print("Motion detected at", time_str)

    # Wait for 0.1 seconds before checking again
    utime.sleep(0.1)
