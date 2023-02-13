# PAL_TimerIsRunning Function

## C

```c
bool PAL_TimerIsRunning(TimerId_t timer_id)
```

## Summary

Gets the status of running timer  

## Description

Checks if the timer of requested timer identifier is running

## Precondition

Timer should have been started before using this function  

## Parameters

| Param | Description |
|:----- |:----------- |
| timer_id | Timer identifier  

## Returns

*bool* - true
- false otherwise.  

## Example

```c
PAL_Status_t retVal = PAL_FAILURE;
TimerId_t appTimer;
bool IsTimerRunning = false;

static void AppTimerCallback(void *paramCb)
{
    //Toggle LED
}

//Get the Id for the sotware timer instance
PAL_TimerGetId(&appTimer);

if (PAL_SUCCESS == PAL_TimerStart(appTimer,
5000,
TIMEOUT_RELATIVE,
(void *)AppTimerCallback,
NULL, CALLBACK_SINGLE))
{
    //Timer Started
    //ToggleLED
}

IsTimerRunning = PAL_TimerIsRunning(appTimer);

if(IsTimerRunning)
{
    //Timer is running
}

```
## Remarks

None 

