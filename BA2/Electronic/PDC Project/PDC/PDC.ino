#include <LedControl.h>
#include <binary.h>

#define DS_Pin 53
#define STCP_Pin 51
#define SHCP_Pin 49

const int DIN = 10;
const int CS =  9;
const int CLK = 8;
const int DEVICE = 4;
const int trigPin[] = {2, 4, 6}; 
const int echoPin[] = {3, 5, 7}; 
const int BUZZER = 11;
const int LIGHTSENSOR = A0;

const int SENSOR = 3;
const int LED = 3;
boolean registers[3]; 
int analogValue;

unsigned long radar_task;
unsigned long display_task;
unsigned long sound_task;
unsigned long light_task;

int response_time;
int levelbackup[3];
int sound_level;
int frequency;

LedControl lc=LedControl(DIN,CLK,CS,DEVICE);

void setup() {
  Serial.begin (115200);
  pinMode(DS_Pin, OUTPUT);
  pinMode(STCP_Pin, OUTPUT);
  pinMode(SHCP_Pin, OUTPUT);
  for(int index=0;index<lc.getDeviceCount();index++) {
      lc.shutdown(index,true);
      lc.setIntensity(index, 0);
      lc.clearDisplay(index);
  }

  for(int i = 0; i < SENSOR; i++){
    pinMode(trigPin[i], OUTPUT); 
    pinMode(echoPin[i], INPUT); 
  }
  radar_task = millis();
  display_task = millis();
  sound_task = millis();
  light_task = millis();
 
  response_time = 0;
  frequency = 1000000;
}

void loop() {

  // Measure from every sensor every 1ms
  if (millis() - radar_task > 1){
    radar_task = millis();
    for(int i = 0; i < SENSOR; i++){
      response_time ++;
      int distance = measure(i);
      int level = check(distance); 
      levelbackup[i] = level;
    }
    // Display data on LED Matrix every 5 ms
    if (millis() - display_task > 5){
      for(int i = 0; i < SENSOR; i++){
        display(i, levelbackup[i]);  
      }
    }
  }
  // Update sound event frequency every 10 measurements
  // To let enough time to the buzzer to ring.
  if (response_time >= 10){
    response_time = 0;
    frequency = getFrequency();
  }
  // Zero means out of range
  if (frequency == 0){
    noTone(BUZZER);
    sound_task = millis();
  }
  // One means max range
  if (frequency == 1){
    tone(BUZZER, 1000);
    sound_task = millis();
  }
  // Make the buzzer beeping at the right frequency 
  // Frequency value vary from distances
  if (frequency != 0){
    if (millis() - sound_task > frequency){
      tone(BUZZER, 1000);
    }
    if (millis() - sound_task > 2*frequency){
      noTone(BUZZER);
      sound_task = millis();
    }
  }
  // Check if light need to be turned on every second
  if (millis() - light_task > 1000){
    light();
    light_task = millis();
  } 
}

// Get the right beeping frequency 
// From the most important distance between the 3 sensors
int getFrequency(){
  int maximum = 0;
  int out_of_range = 0;
  for (int i = 0; i < SENSOR; i++){
    if (levelbackup[i] > maximum and levelbackup[i] != 10){
      maximum = levelbackup[i];
    }
    if (levelbackup[i] == 10){
      out_of_range ++;
    }
  }
  if (out_of_range == SENSOR){
    return 0;
  }
  if (maximum == 7){
    return 1;
  }
  else{
    return 500-(70*maximum);
  }
}

// Measure the distance from a sensor
int measure(int index){
  digitalWrite (trigPin[index], HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin[index], LOW);
  int duration = pulseIn (echoPin[index], HIGH);
  int distance = (duration*0.0340)/2;
  if (distance < 0){
    return 0;
  }
  else{
    return distance;
  }
}

// Return the level of proximity
// Higher means object is near from the sensor
int check(int distance){
  int level;
  if (distance > 34){
    level =  10;
  }
  else if (distance <= 31 and distance > 28){
    level = 0;
  }
  else if (distance <= 28 and distance > 25){
    level = 1;
  }
  else if (distance <= 25 and distance > 22){
    level = 2;
  }
  else if (distance <= 22 and distance > 19){
    level = 3;
  }
  else if (distance <= 19 and distance > 16){
    level = 4;
  }
  else if (distance <= 16 and distance > 13){
    level = 5;
  }
  else if (distance <= 13 and distance >10){
    level = 6;
  }
  else if (distance <= 10){
    level = 7;
  }
  return level;
}

// Display as many rows as the proximity level is high
// On the LED Matrix
void display(int matrix, int level){
  int row = level;
  if (row != 10){
    int intensity = 1;
    lc.shutdown(matrix,false);
    lc.setIntensity(matrix, intensity);
    lc.clearDisplay(matrix);
    for (int i=0; i<=row; i++){
      lc.setRow(matrix, i, B11111111);
    }
  }
  else{
    lc.shutdown(matrix,true);
    lc.setIntensity(matrix, 0);
    lc.clearDisplay(matrix);
  }
}

// Write data on internal memory from shift register 74HC595
// Data is turning RGB LED ON
void writeRegister() {
  digitalWrite(STCP_Pin, LOW);        

  for (int i=LED-1; i>=0; i--)                     
  {
    digitalWrite(SHCP_Pin, LOW);     
    digitalWrite(DS_Pin, registers[i]);
    digitalWrite(SHCP_Pin, HIGH);    
  }
  digitalWrite(STCP_Pin, HIGH);      
}

// Read the light sensor value
// Turn LED ON above certain value
void light() {
  analogValue = analogRead(LIGHTSENSOR);
  if(analogValue > 250){ //change > by < if LED do the opposite behavior
    for (int i=0; i<LED; i++){
    registers[i]=HIGH;
    writeRegister();
    }
  }
  else{
    for (int i=LED-1; i>=0; i--){
    registers[i]=LOW;
    writeRegister();
    }
  }
}
