# PAL_TimerGetId Function

## C

```c
PAL_Status_t PAL_TimerGetId(TimerId_t *timer_id)
```

## Summary

Gets the Timer Id  

## Description

Returns a timer id to be used before starting a timer

## Precondition

PAL_Init() should have been called before calling this function.  

## Parameters

| Param | Description |
|:----- |:----------- |
| timer_id | Value of the id returned by the function  

## Returns

*PAL_SUCCESS* - If there is a unused timer

*PAL_FAILURE* - If there are no timer unused
 

## Example

```c
TimerId_t appTimer;
//Get the Id for the sotware timer instance
PAL_TimerGetId(&appTimer);
```

## Remarks

None 

