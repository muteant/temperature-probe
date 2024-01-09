//the scale factor of TMP36 (temperature sensor) is 10 mV/°C with a 500 mV offset to allow for negative temperatures

// the analog pin number connected to the TMP36
int sensorPin = A0;
// delay between sensor reads
int readDelay = 3000;

void setup()
{
    //initializing serial communication with the Omega2 for sending sensor data
    Serial.begin(9600);
}

void loop()
{
    // getting the voltage reading from the temperature sensor
    float reading = analogRead(sensorPin);  
    Serial.print(reading); Serial.println('analog reading');
    
    // convert the analog reading (0 to 1023) to voltage (0 - 5V)
    float voltage = reading * 5.0/1024;

    // print out the voltage to Omega2
    Serial.print(voltage); Serial.println(" volts");

    // convert voltage to degree Celsius including the 500mV offset adjustment
    float temperatureC = (voltage - 0.5) * 100;  
    Serial.print(temperatureC); Serial.println(" degrees C");

    // convert from Celsius to Fahrenheit and print to Omega2
   // float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
   // Serial.print(temperatureF); Serial.println(" degrees F");

    // delay between readings since the change is gradual
    delay(readDelay);
}
