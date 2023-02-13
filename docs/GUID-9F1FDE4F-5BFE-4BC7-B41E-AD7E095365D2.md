# PHY_TrxWakeup Function

## C

```c
PHY_Retval_t PHY_TrxWakeup(void)
```

## Summary

Wakes up the transceiver from sleep  

## Description

This function awakes the transceiver from sleep state.

## Precondition

PHY_TrxSleep() should have been called before calling this function  

## Parameters

None  

## Returns

*PHY_TRX_AWAKE* - The transceiver is already awake

*PHY_SUCCESS* - The transceiver is woken up from sleep

*PHY_FAILURE* - The transceiver did not wake-up from sleep
 

## Example

```c
PHY_SleepMode_t sleepMode = SLEEP_MODE_1;
bool trxSleepStatus = false;
// Set Transceiver to sleep
if (PHY_SUCCESS == PHY_TrxSleep(sleepMode))
{
    trxSleepStatus = true;
}
//wakeup the transceiver
if (PHY_SUCCESS == PHY_TrxWakeup())
{
    trxSleepStatus = false;
}
```

## Remarks

When TRX is put into DeepSleep, the TRX registers are reset and it will hold default values, PIB values are getting written by PHY layer when Wakeup function is called.User has to reconfigure the configuration parameters (PHY_ConfigParam_t) which are set by application. This procedure is not needed for SLEEP mode as the TRX register values are retained. 



