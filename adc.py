# Adapted from tutorial on Adafruit website
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
inpin = 1 #input from the ADC (channel 1)
LED = 13
print('Calculating frequency, press Ctrl-C to quit...')

#set up LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT) #sets up LED pin to output 

#set up frequency measurement
count = 0
threshold = 130 #below this value, the light is blocked

# Main program loop.
GPIO.output(LED, GPIO.HIGH)
while count<20:
    values= mcp.read_adc(inpin)
    if values < threshold:
        if count == 0:
            starttime = time.time()
        count = count +1
        time.sleep(0.3)

#calculate frequency and BPM
endtime = time.time()
elapsedtime = endtime-starttime
freq = 10/elapsedtime - 0.02
bpm = freq * 120
GPIO.output(LED, GPIO.LOW) 

print("The frequency is " + str(freq) + " Hz")
print("The tempo is " + str(bpm) + " BPM")
GPIO.cleanup()
