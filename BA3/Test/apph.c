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
    int delay;
    int blinkCount;
    
}APP_LED_DATA;

// Define 2 LEDs of APP_LED_DATA Structure 
extern APP_LED_DATA appLedData;
extern APP_LED_DATA appLed2Data;

// Initialize the task
void APP_LED_Initialize(void (*func)(void), APP_LED_DATA *led_ptr, int delay);
// Evaluate Counter (Timer) State
void APP_LED_Tasks(APP_LED_DATA *led_ptr);
void D2_LED(void);
void D4_LED(void);