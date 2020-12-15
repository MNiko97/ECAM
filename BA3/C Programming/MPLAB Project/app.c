#include "app.h"
#include "mcc_generated_files/pin_manager.h"
#include "mcc_generated_files/ext_int.h"

APP_LED_DATA appLedData;
APP_LED_DATA appLed2Data;
APP_BUFFER_DATA appBufferData;
APP_BTN_INT0_DATA appBtnInt0Data;
APP_ADC_DATA appAdc1Data;
APP_ADC_DATA appAdc2Data;

// Useful variables for APP_BUFFER_Tasks
int msgIndice = 0;
int charToRead = 0;
char data[100];

// ADC Task variable for channel selection
int ADCReady = 1;

// Function linked to Toggle method for D2 and D4
void D3_LED(void){
    D3_Toggle();
}
void D4_LED(void){
    D4_Toggle();
}

void APP_BUFFER_Initialize(APP_BUFFER_DATA *buffer_ptr){
    buffer_ptr->RxCount = 0;
    buffer_ptr->RxHead = 0;
    buffer_ptr->RxTail = 0;
}
void APP_BUFFER_Tasks(APP_BUFFER_DATA *buffer_ptr, char msgFromPC[], int msgSize){
    // Update variable: character left to read 
    charToRead = msgSize-msgIndice;
    
    // Do buffer task until there is no character left to read
    if (charToRead >= 0){
        
        // If head is at the end of the buffer, reset head position
        if(buffer_ptr->RxHead >= sizeof(buffer_ptr->RxBuffer)) buffer_ptr->RxHead = 0; 
        
        // Write message from PC to the buffer until it is full
        if (charToRead > 0)buffer_ptr->RxBuffer[buffer_ptr->RxHead++] = msgFromPC[msgIndice++]; 
        
        /*
        Start to read the buffer only when tail and head position are different
        Tail and head should never meet until the message is entirely read.
        When buffer is full release buffer content into a larger container : data
        */
        if(buffer_ptr->RxTail != buffer_ptr->RxHead){
            data[buffer_ptr->RxCount++] = buffer_ptr->RxBuffer[buffer_ptr->RxTail];
            
            // Replaced character from buffer by "-" after reading it
            buffer_ptr->RxBuffer[buffer_ptr->RxTail++] = '-';
            
            // If tail is at the end of the buffer, reset tail position
            if(buffer_ptr->RxTail >= sizeof(buffer_ptr->RxBuffer))buffer_ptr->RxTail = 0;
        }
    }
}

void APP_LED_Initialize(void (*func)(void), APP_LED_DATA *led_ptr, int blinkDelay){
    led_ptr->state = APP_LED_STATE_INIT;
    led_ptr->TimerCount = 0;
    led_ptr->func = func; //Pointer to the toggle method associated to the right led
    led_ptr->blinkDelay = blinkDelay;
    led_ptr->blinkCount = 0;
}
void APP_LED_Tasks(APP_LED_DATA *led_ptr){
    switch(led_ptr->state){
        case APP_LED_STATE_INIT :
        {
            led_ptr->state = APP_LED_STATE_WAIT;
            break;
        }
        case APP_LED_STATE_WAIT :
        {
            if(led_ptr->TimerCount >= led_ptr->blinkDelay){
                led_ptr->state = APP_LED_STATE_BLINK;
                led_ptr->TimerCount = 0;break;
            }
        }
        case APP_LED_STATE_BLINK :
        {
            (led_ptr->func)(); //call the pointer function Toggle() assiociated to the led pointer
            led_ptr->state = APP_LED_STATE_WAIT;
            led_ptr->blinkCount ++; //increment the counter
            NOP();
            break;
        }
        default :
            led_ptr->state = APP_LED_STATE_INIT;
            break;
    }
}

void APP_BTN_INT0_Initialize(){
    appBtnInt0Data.btnIsPressed = 0;
}
void APP_BTN_INT0_Tasks(){
    if(appBtnInt0Data.btnIsPressed == 1){
        EXT_INT0_InterruptDisable();
        D3_SetHigh();
        NOP();
        NOP();
        D3_SetLow();
        appBtnInt0Data.btnIsPressed = 0;
        EXT_INT0_InterruptEnable();
    }
}

void APP_ADC_Initialize(APP_ADC_DATA *adc_ptr, adc_channel_t channel){
    adc_ptr->adc_btn_int1 = 0;
    adc_ptr->count=0;
    adc_ptr->data = 0;
    adc_ptr->state = APP_ADC_STATE_INIT;
    adc_ptr->channel = channel;
}
void APP_ADC_Tasks(APP_ADC_DATA *adc_ptr){
      
    switch(adc_ptr->state){
        case APP_ADC_STATE_INIT :
        {
            adc_ptr->state = APP_ADC_STATE_WAIT;
            
            break;
        }
        case APP_ADC_STATE_WAIT :
        {
            if(adc_ptr->adc_btn_int1){ //remove the !
                EXT_INT1_InterruptDisable();
                EXT_INT0_InterruptDisable();
                if(ADCReady){
                    ADCReady = 0;
                    ADC_SelectChannel(adc_ptr->channel); 
                    adc_ptr->state = APP_ADC_STATE_START;
                }                 
            }
            adc_ptr->data = 0; 
            break;
        }
        case APP_ADC_STATE_START :
        {
            if(adc_ptr->count >= 4){
                ADCReady = 1;
                adc_ptr->state = APP_ADC_STATE_DONE;
                adc_ptr->data = adc_ptr->data/adc_ptr->count;
                adc_ptr->count = 0;
            }
            else{
                ADC_StartConversion();
                adc_ptr->state = APP_ADC_STATE_IN_PROGRESS;
            }
            break;
        }
        case APP_ADC_STATE_IN_PROGRESS :
        {
            if(ADC_IsConversionDone()){
                adc_ptr->state = APP_ADC_STATE_START;
                adc_ptr->count ++;
                adc_ptr->data += ADC_GetConversionResult();
            }
            break;
        }
        case APP_ADC_STATE_DONE :
        {
            ADCReady = 1;
            adc_ptr->state = APP_ADC_STATE_WAIT;
            adc_ptr->adc_btn_int1 = 0;
            EXT_INT1_InterruptEnable();
            EXT_INT0_InterruptEnable();
            break;
        }
    }
}