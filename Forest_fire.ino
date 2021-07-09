S#include <DHT.h>
#include <DHT_U.h>
#include "stdio.h"
#include "DHT.h"
#define dht_1 2
#define DHTTYPE DHT11
DHT dht(dht_1,DHTTYPE);
int flame = 10;
int smoke = 9;
int buzzer = 13;
void setup ()
{
  pinMode (flame, INPUT);
  pinMode (smoke, INPUT);
  pinMode (buzzer, OUTPUT);
  Serial.begin(9600);
  dht.begin();
}
void loop ()
{

  
  
    float temp = dht.readTemperature();
   // Serial.print("Temperature= ");
   // Serial.println(temp);
  
    
   int sval = digitalRead (smoke);

 // Serial.print("sval = ");
  //Serial.println(sval);
 
 

 
  
    float humid =dht.readHumidity();
    //Serial.print("Humidity= ");
    //Serial.println(humid);
   

  int fval = digitalRead (flame);
  //Serial.print("fval = ");
  //Serial.println(fval);

  

 Serial.println("T="+ String(temp)+ ", H ="+ String(humid)+ ", F ="+ String(fval)+ ", S =" +String(sval));
  delay(1000);
  }
  
