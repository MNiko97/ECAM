//74HC595 Shift-Register + Light Sensor DEMO

#define DS_Pin 53
#define STCP_Pin 51
#define SHCP_Pin 49

int lightSensorPin = A0;
int analogValue = 0;

static int LED = 6;
boolean registers[6]; 
int time1 = 300;        

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

void setup() {
  pinMode(DS_Pin, OUTPUT);
  pinMode(STCP_Pin, OUTPUT);
  pinMode(SHCP_Pin, OUTPUT);
  Serial.begin(115200);
  writeRegister(); 
}

void loop() {
  analogValue = analogRead(lightSensorPin);
  Serial.println(analogValue);
  if(analogValue > 250){ //change > by < if LED do the opposite behavior
    for (int i=0; i<LED; i++){
    registers[i]=HIGH;
    delay(time1);
    writeRegister();
    }
  }
  else{
    for (int i=LED-1; i>=0; i--){
    registers[i]=LOW;
    delay(time1);
    writeRegister();
    }
  }
}
