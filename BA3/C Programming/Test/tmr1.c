void TMR1_CallBack(void)
{
    // Add your custom callback code here
    if(TMR1_InterruptHandler)
    {
        appLedData.TimerCount ++;
        appLed2Data.TimerCount ++;
        TMR1_InterruptHandler();
    }
}
