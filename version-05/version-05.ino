
// Scale Factor is 100 (10 [mV]/[deg C]) 
// Accuracy is +/- 2 for analog readings
// Built-in offset of 0.5 V -> specified to read negative temperatures


// the analog pin number connected to the TMP36
int analog_a0 = A0;
// delay between sensor reads
int readDelay = 100;

void setup()
{
    //initializing serial communication
    Serial.begin(9600);
}

void loop()
{
    // getting the voltage reading from the temperature sensor
    float analog_reading_tmp36 = analogRead(analog_a0);  
    
    // convert the analog reading (0 to 1023) to voltage (0 - 5V)
    float voltage_tmp36 = analog_reading_tmp36 * 5.0/1024;

    // convert voltage to degree C including the 0.5 V adjustment
    float temperature_C = (voltage_tmp36 - 0.5) * 100;  

    // print readings and calculations
    Serial.print(analog_reading_tmp36); 
    Serial.print(" "); 
    Serial.print(voltage_tmp36); 
    Serial.print(" ");
    Serial.println(temperature_C); 


    // delay between readings since the change is gradual
    delay(readDelay);
}
