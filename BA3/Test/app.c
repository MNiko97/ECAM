APP_LED_DATA appLedData;
APP_LED_DATA appLed2Data;

void D2_LED(void){
    D2_Toggle();
}
void D4_LED(void){
    D4_Toggle();
}
void APP_LED_Initialize(void (*func)(void), APP_LED_DATA *led_ptr, int delay){
    led_ptr->state = APP_LED_STATE_INIT;
    led_ptr->TimerCount = 0;
    led_ptr->func = func;
    led_ptr->delay = delay;
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
            if(led_ptr->TimerCount >= 2){
                led_ptr->state = APP_LED_STATE_BLINK;
                led_ptr->TimerCount = 0;
                break;
            }
        }
        case APP_LED_STATE_BLINK :
        {
            led_ptr->func(); //call the pointer function assiociated to the led
            led_ptr->state = APP_LED_STATE_WAIT;
            led_ptr->blinkCount ++;
            NOP();
            break;
        }
        default :
            led_ptr->state = APP_LED_STATE_INIT;
            break;
    }
}