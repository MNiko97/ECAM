/* 
 * File:   app.h
 * Author: Niko
 *
 * Created on November 11, 2020, 10:30 PM
 */

#ifndef APP_H
#define	APP_H
#include "mcc_generated_files/adc.h"

typedef enum{
    APP_LED_STATE_INIT = 0,
    APP_LED_STATE_WAIT = 1,
    APP_LED_STATE_BLINK = 2
}APP_LED_STATE;
typedef enum{
    APP_ADC_STATE_INIT = 0,
    APP_ADC_STATE_WAIT = 1,
    APP_ADC_STATE_START = 2,
    APP_ADC_STATE_IN_PROGRESS =3,
    APP_ADC_STATE_DONE = 4
}APP_ADC_STATE;
typedef struct{
    APP_LED_STATE state;
    void (*func)(void);
    int TimerCount;
    int blinkDelay;
    int blinkCount;  
}APP_LED_DATA;
typedef struct{
    // 8 bit char buffer
    char RxBuffer[8];
    int RxCount;
    int RxHead;
    int RxTail;
}APP_BUFFER_DATA;
typedef struct{
    int btnIsPressed;
}APP_BTN_INT0_DATA;
typedef struct{
    APP_ADC_STATE state;
    int data;
    int count;
    int adc_btn_int1;
    adc_channel_t channel;
}APP_ADC_DATA;

extern APP_LED_DATA appLedData;
extern APP_LED_DATA appLed2Data;
extern APP_BUFFER_DATA appBufferData;
extern APP_BTN_INT0_DATA appBtnInt0Data;
extern APP_ADC_DATA appAdc1Data;
extern APP_ADC_DATA appAdc2Data;

void APP_LED_Initialize(void (*func)(void), APP_LED_DATA *led_ptr, int blinkDelay);
void APP_BUFFER_Initialize(APP_BUFFER_DATA *buffer_ptr);
void APP_BTN_INT0_Initialize(void);
void APP_ADC_Initialize(APP_ADC_DATA *adc_ptr, adc_channel_t channel);

void APP_LED_Tasks(APP_LED_DATA *led_ptr);
void APP_BUFFER_Tasks(APP_BUFFER_DATA *buffer_ptr, char msgFromPC[], int msgSize);
void APP_BTN_INT0_Tasks(void);
void APP_ADC_Tasks(APP_ADC_DATA *adc_ptr);

// Toggle LED 2 and 4 Definition
void D2_LED(void);
void D4_LED(void);
#endif	/* APP_H */