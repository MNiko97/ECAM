#include "app.h"
#include "mcc_generated_files/pin_manager.h"

APP_LED_DATA appLedData;
APP_LED_DATA appLed2Data;
APP_BUFFER_DATA appBufferData;

// Useful variables for APP_BUFFER_Tasks
int msgIndice = 0;
int charToRead = 0;
char data[100];

// Function linked to Toggle method for D2 and D4
void D2_LED(void){
    D2_Toggle();
}
void D4_LED(void){
    D4_Toggle();
}

// Initialize Buffer variables
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
// Initialize APP_LED variables
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