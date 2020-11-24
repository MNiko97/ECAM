/* 
 * File:   app.h
 * Author: Niko
 *
 * Created on November 11, 2020, 10:30 PM
 */

#ifndef APP_H
#define	APP_H

// Create 3 possible states
typedef enum
{
    APP_LED_STATE_INIT = 0,
    APP_LED_STATE_WAIT = 1,
    APP_LED_STATE_BLINK = 2
}APP_LED_STATE;

// Allow to create a state and a timer counter
typedef struct
{
    APP_LED_STATE state;
    void (*func)(void);
    int TimerCount;
    int blinkDelay;
    int blinkCount;  
}APP_LED_DATA;

// Create a buffer structure
typedef struct
{
    // 8 bit char buffer
    char RxBuffer[8];
    int RxCount;
    int RxHead;
    int RxTail;
    int isFull;
}APP_BUFFER_DATA;

//Define Buffer
extern APP_BUFFER_DATA appBufferData;

//Initialise Buffer
void APP_BUFFER_Initialize(APP_BUFFER_DATA *buffer_ptr);

// Buffer Task
void APP_BUFFER_Tasks(APP_BUFFER_DATA *buffer_ptr, char msgFromPC[], int msgSize);

// Define 2 LEDs of APP_LED_DATA Structure 
extern APP_LED_DATA appLedData;
extern APP_LED_DATA appLed2Data;

// Initialize the LED task
void APP_LED_Initialize(void (*func)(void), APP_LED_DATA *led_ptr, int blinkDelay);
// Evaluate Counter (Timer) State
void APP_LED_Tasks(APP_LED_DATA *led_ptr);
// Toggle LED 2 and 4 Definition
void D2_LED(void);
void D4_LED(void);
#endif	/* APP_H */