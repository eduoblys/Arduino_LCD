#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>


/* Declare LCD object for SPI
 Adafruit_PCD8544(CLK,DIN,D/C,CE,RST); */
Adafruit_PCD8544 display = Adafruit_PCD8544(7, 6, 5, 4, 3);
int contrastValue = 60; // Default Contrast Value
const int adcPin = 34;
int adcValue = 0;
String incByte;
void setup()
{
  Serial.begin(9600);
  /* Initialize the Display*/
  display.begin();

  /* Change the contrast using the following API*/
  display.setContrast(contrastValue);

  /* Clear the buffer */
  display.clearDisplay();
  display.display();
  delay(1000);
  
  /* Now let us display some text */
  display.setTextColor(WHITE, BLACK);
  display.setCursor(0,1);
  display.setTextSize(2);
  display.println("|ESP32|");
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.setCursor(22,20);
  display.println("|Nokia|");
  display.setCursor(22,32);
  display.println("|5110|");
  display.write("3");
  display.display();
  delay(2000);
}
int x=0;
void loop(){
  while(1){
    if (Serial.available() > 0){
      incByte = Serial.readString();
      if(incByte != ""){
        display.setCursor(0,1);
        display.clearDisplay(); 
        display.print("Players:");
        display.print(incByte);
        display.display();
        delay(25000);
      }
       else{
        display.setCursor(1,1);
        display.clearDisplay(); 
        display.print("Empty string");
        display.display();
        delay(2000);
       }
      
    }
    display.clearDisplay(); 
    display.println(x);
    display.display();
    delay(1000);
    x=++x;
  }

  

}
