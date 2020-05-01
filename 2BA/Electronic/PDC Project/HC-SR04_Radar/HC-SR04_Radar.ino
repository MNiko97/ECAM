//Multiple HC-SR04 Sensor DEMO

static int trigPin[] = {2, 4, 6}; 
static int echoPin[] = {3, 5, 7}; 
static int SENSOR = 3;

void setup() {
  Serial.begin (115200);
  for(int i = 0; i < SENSOR; i++){
    pinMode(trigPin[i], OUTPUT); 
    pinMode(echoPin[i], INPUT); 
  }
}

void loop() {
  for(int i = 0; i < SENSOR; i++){
    int distance = measure(i);
    Serial.print(distance);  
    Serial.print("cm");
    Serial.println();
  }
}
