//Sorting Methods

unsigned long startTime; 
unsigned long currentTime; 
unsigned long elapsedTime; 

float varianceError = 0.75; //test 0.75 is a good limit

float mean(){
  float sum = 0;
  for(int i = 0; i < size(); i++){ // parcourir la liste <sampleArray> pour afficher toutes les distances de l'echantillon
    sum += data[i];
  }
  float mean = sum / size();
  return mean;
}

void sort(){
  bool tabSorted = false;
  while(tabSorted == false){
    tabSorted = true;
    for(int i = 0; i < size(); i++){
      if(data[i] < data[i + 1]){
        float tmp = data[i + 1];
          data[i + 1] = data[i];
          data[i] = tmp;
          tabSorted = false;
      }
    }
  }
}

float variance(){
    float result = 0;
    for(int i = 0; i < size(); i++){
        result += pow((data[i] - mean()), 2);
    }
    float variance = result / size();
    return variance;
}

float checkVariance(){
    if(variance() > varianceError){
      Serial.println("Modifying data, variance not acceptable !");
      float IIQ = (data[5]+data[6])/2; //intervalle interquartil
      data[0] = IIQ;
      data[9] = IIQ;
      mean();
      variance();
      display_data();
    }
    else {
        Serial.println("Variance acceptable");
    }
}

int size(){
    byte numberOfElem = sizeof(data) / sizeof(data[0]);
    return numberOfElem;
}