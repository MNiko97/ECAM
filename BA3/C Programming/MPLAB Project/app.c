#include "app.h"
#include "mcc_generated_files/pin_manager.h"

APP_LED_DATA appLedData;
APP_LED_DATA appLed2Data;
APP_BUFFER_DATA appBufferData;
int msgIndice = 0;
int charToRead = 0;
char data[100];

// Function linked to Toggle method for D2 and D4
void D2_LED(void){D2_Toggle();}
void D4_LED(void){D4_Toggle();}

// Initialize Buffer variables
void APP_BUFFER_Initialize(APP_BUFFER_DATA *buffer_ptr){
    buffer_ptr->RxCount = 0;
    buffer_ptr->RxHead = 0;
    buffer_ptr->RxTail = 0;
    buffer_ptr->isFull = 0;
}
void APP_BUFFER_Tasks(APP_BUFFER_DATA *buffer_ptr, char msgFromPC[], int msgSize){
    // Update character left to read variable
    charToRead = msgSize - msgIndice;
    // Write message from PC to buffer until it is full
    if (buffer_ptr->isFull == 0){
        buffer_ptr->RxBuffer[buffer_ptr->RxHead++] = msgFromPC[msgIndice++]; 
        if(buffer_ptr->RxHead >= sizeof(buffer_ptr->RxBuffer) && msgIndice < msgSize){
            buffer_ptr->isFull = 1;
            buffer_ptr->RxHead = 0; 
        } 
        // Check of the message from PC has been fully copied to the buffer
        else if (msgIndice >= msgSize) buffer_ptr->isFull = 1;
    }
    // When buffer is full release buffer content into a larger container named data
    if (buffer_ptr->isFull == 1){
        data[buffer_ptr->RxCount] = buffer_ptr->RxBuffer[buffer_ptr->RxTail];
        // Replaced character from buffer by "-" after reading it
        buffer_ptr->RxBuffer[buffer_ptr->RxTail] = '-';
        buffer_ptr->RxTail ++;
        buffer_ptr->RxCount++;
        // Read entire buffer then reset the Tail and start to write buffer again
        if(buffer_ptr->RxTail >= sizeof(buffer_ptr->RxBuffer)){
            buffer_ptr->isFull = 0;
            buffer_ptr->RxTail = 0; 
        }   
    }
    // when Tail has the same position as Head, means the last buffer content has been released to data
    // Reset Tail and Head and stop the buffer task
    if (buffer_ptr->RxTail == buffer_ptr->RxHead && buffer_ptr->RxHead != 0){
        buffer_ptr->RxTail = 0;
        buffer_ptr->RxHead = 0;
        buffer_ptr->isFull = -1;
    }
    NOP();
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