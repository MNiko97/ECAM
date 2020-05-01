#include <LedControl.h>
#include <binary.h>

static int DIN = 12;
static int CS =  10;
static int CLK = 11;
static int DEVICE = 4;

static int trigPin[] = {2, 4, 6}; 
static int echoPin[] = {3, 5, 7}; 
static int SENSOR = 3;

LedControl lc=LedControl(DIN,CLK,CS,DEVICE);

void setup() {
  Serial.begin (115200);
 
  for(int index=0;index<lc.getDeviceCount();index++) {
      lc.shutdown(index,true);
      lc.setIntensity(index, 0);
      lc.clearDisplay(index);
  }

  for(int i = 0; i < SENSOR; i++){
    pinMode(trigPin[i], OUTPUT); 
    pinMode(echoPin[i], INPUT); 
  }
}

void loop() {

  for(int i = 0; i < SENSOR; i++){
    int distance = measure(i);
    show(i, distance);
  }
  //delay(10);
}

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

void show(int matrix, int distance){
  int row = check(distance);
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
