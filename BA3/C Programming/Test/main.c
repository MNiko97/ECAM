void main(void)
{
    // Initialize the device
    SYSTEM_Initialize();
    APP_LED_Initialize(&D2_LED, &appLedData, 1);
    APP_LED_Initialize(&D4_LED, &appLed2Data, 2);

    // If using interrupts in PIC18 High/Low Priority Mode you need to enable the Global High and Low Interrupts
    // If using interrupts in PIC Mid-Range Compatibility Mode you need to enable the Global and Peripheral Interrupts
    // Use the following macros to:

    // Enable the Global Interrupts
    //INTERRUPT_GlobalInterruptEnable();

    // Disable the Global Interrupts
    //INTERRUPT_GlobalInterruptDisable();

    // Enable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptEnable();

    // Disable the Peripheral Interrupts
    //INTERRUPT_PeripheralInterruptDisable();

    while (1)
    {
        APP_LED_Tasks(&appLedData);
        APP_LED_Tasks(&appLed2Data);
                
    }
}