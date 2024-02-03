# temperature-probe

Record, process, and visualize temperature data for single sensor and single arduino board

Basic Operations: 

1. Arduino records an analog reading value between (0-1024) fromm the TMP36 Sensor (this sensor's value will increase or decrease linearly with the temperature)

2. Analog values are converted to voltage readings which are then converted to temperature values. 

3. Python reads information being recorded and processed by Arduino
	Note: Python is not pulling information from the Arduino directly. Python is collecting information from the computers Serial Port. This information is dependant on how the Arduino sketch file 				is configured. All the information that is printed using the Arduino function Serial.print can be collected by Python.

4. Python creates a massive array of the recorded data then exports this as csv.
	Note: 
	- It could be more efficient to record data in smaller sets of arrays then update the csv (if you are a programmer this could be done even better)
	
	- Arduino is pulling information at an extremely high sample rate (multiple times a second). This is a constant stream of information that is stored temporarily on the computers memory. 

 	- Python is plucking out the values from the constant stream based on the sample frequency set in the loop in Python

6. This process for recording and sampling can be highly optimized. 
	For testing:
	- use short run times (10 seconds -> 1 minute) 
	
	- use low sample frequency (1->3 times a second)
		 
	For application:
	- long projects (1 day -> 1 week) use a low density sample frequency (once every 15->30 mins)
			
	- short projects (1 hour -> 1 day) use a higher density sample frequency (once every 1-> 30 seconds)
	
7. Recorded data is updated in Python using the library pandas (soooo powerful!)

8. Import clean data set in Jupyter notebook and analyze with pandas + matplotlib
	Note:
	- This step could done using any form of data analysis program. 
	- The purpose of using the Python scripts for data recording and cleaning is to allow the analysis and recording to run as seperate operations



