# Import useful libraries

from datetime import datetime 
import serial # Connect to arduino/read values
import csv
import time


# Board Setup
arduino_port = "/dev/ttyACM0" 
baud = 9600
fileName="analog-data.csv" # file to save recorded data
sensor_data =[]

# Read Serial Port and open file
ser = serial.Serial(arduino_port, baud) # Read serial port
print("Connected to Arduino port:", arduino_port)
file = open(fileName, "a") # append fileName (will create new if no file exists)
print("Created file")


# Sampling 
profile_length = int(input("Enter total length of fermentation in seconds: ")) # [seconds]
sample_resolution = int(input("Enter number of samples to be recorded per hour: ")) # [samples/hour]

# Data Collection 
sensor_data = [] #store data
rest_time = 1/sample_resolution # seconds
for time in profile_length:
    
    serial_data=ser.readline()    

    decode_serial_data = serial_data.decode('UTF-8')
    
    extracted_data = decode_serial_data[0:][:-2] # sig figs
    
    data_point = (datetime.now()),extracted_data.split(" ")
    
    sensor_data.append(data_point)
    
    time.sleep(rest_time)
    


# Store the data
with open(fileName, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)

print("Data collection complete!")
file.close()
    