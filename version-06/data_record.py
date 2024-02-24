# Import useful libraries

from datetime import datetime # for getting accurate date time 
import serial # Connect to arduino/read values
import csv # For exporting file
import time # For use in sampling


# Board Setup
arduino_port = "/dev/ttyACM0" # You can check your connections with /dev/tty*
baud = 9600 # Match this to arduino
#fileName=str(input("Enter data file name (i.e: analog-data.csv)"))# "analog-data.csv" # file to save recorded data
fileName = 'analog-data.csv'
sensor_data =[] #empty array for storing all the data

# Read Serial Port and open file
ser = serial.Serial(arduino_port, baud) # Read serial port
print("Connected to Arduino port:", arduino_port)
file = open(fileName, "a") # append fileName (will create new if no file exists)
print("Created file")


# Sampling 

time_between_samples = 60 # seconds (60 is 5 mins)

steps =60

sensor_data = [] #store data

while steps > 0:
    
    serial_data=ser.readline()    

    decode_serial_data = serial_data.decode('UTF-8')
    
    clean_data = decode_serial_data[0:][:-2] # sig figs
    
    data_for_upload = datetime.now(),clean_data.split(" ") # saves the arduino recorded value and current datetime
    
    sensor_data.append(data_for_upload)
    
    time.sleep(time_between_samples)
    steps -= 1


# Store the data
with open(fileName, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)

print("Data collection complete!")
file.close()
    
