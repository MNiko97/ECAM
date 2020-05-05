const int BUZZER = 11;

unsigned long sound_task;
unsigned long radar_task;
const int SENSOR = 3;
int response_time = 0;
int levelbackup[] = {3, 5, 2};
int sound_level;
int frequency;
 
void setup(){
  Serial.begin(115200);
  pinMode(BUZZER, OUTPUT); 
  sound_task = millis();
  response_time = 0;
  frequency = 500;
}

void loop(){
  if (millis()-radar_task >2){
    response_time++;
    //Serial.println(response_time);
    radar_task = millis();
  }
  if (response_time == 500){
    response_time = 0;
    int sound_level = getMin();
    frequency = 500-(60*sound_level);
  }
  
  if (millis() - sound_task > frequency){
    tone(BUZZER, 1000);
  }
  if (millis() - sound_task > 2*frequency){
    sound_task = millis();
    noTone(BUZZER);
  }
}

int getMin(){
  int minimum;
  for (int i = 0; i < SENSOR; i++){
    minimum = levelbackup[i];
    if (levelbackup[i] < minimum){
      minimum = levelbackup[i];
    }
  }
  return minimum;
}
