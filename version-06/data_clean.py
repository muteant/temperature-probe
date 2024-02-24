# Import Useful Libraries

import pandas as pd
from datetime import datetime

# Import recorded data as a panadas DataFrame
dataset = pd.read_csv(('analog-data.csv'), names = ['time', 'recorded_data'])

# Seperate recorded data into new columns
dataset[['Analog','Voltage [V]','Temperature [C]']] = dataset['recorded_data'].str.split(' ', expand=True)

# Clean up the new columns 
dataset['Analog'] = dataset['Analog'].str.strip("[',]").astype('float')
dataset['Voltage [V]'] = dataset['Voltage [V]'].str.strip("[',]").astype('float')
dataset['Temperature [C]'] = dataset['Temperature [C]'].str.strip("[',]").astype('float')

# Convert time to datetime for delta Time Calculations
dataset['time'] = pd.to_datetime(dataset['time'])

# Create a column for Year, Month, Day, Clock 
dataset['Year'] = dataset['time'].dt.year
dataset['Month'] = dataset['time'].dt.month_name()
dataset['Weekday'] = dataset['time'].dt.day_name()
dataset['Hour'] = dataset['time'].dt.hour
dataset['Minute'] = dataset['time'].dt.minute
dataset['Second'] = dataset['time'].dt.second

# Output cleaned dataset
dataset.to_csv('processed-analog-data.csv', index=False)  
