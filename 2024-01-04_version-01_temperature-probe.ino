int analog_0 = A0;   //This is where our Output data goes

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:


  float milivolts = analogRead(analog_0);    //Read the analog pin
  float temperature = milivolts * 0.48828125;   // convert output (mv) to readable celcius
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("C");  //print the temperature status
  delay(1000);  

}
