//the scale factor of TMP36 (temperature sensor) is 10 mV/°C with a 500 mV offset to allow for negative temperatures

// the analog pin number connected to the TMP36
int pin_a0 = A0;
// delay between sensor reads
int readDelay = 5000;

void setup()
{
    //initializing serial communication with the Omega2 for sending sensor data
    Serial.begin(9600);
}

void loop()
{
    // getting the voltage reading from the temperature sensor
    int reading = analogRead(pin_a0);  
    Serial.println(reading);
 
}
