# PHY_EdSample Function

## C

```c
uint8_t PHY_EdSample(void)
```

## Summary

Perform a single ED measurement on current channel  

## Description

This function is used to measure the energy level on current channel

## Precondition

PHY_Init() should have been called before calling this function.  

## Parameters

None  

## Returns

*edValue* - Result of the measurement
 

## Example

```c
PHY_Retval_t retVal = PHY_FAILURE;
uint8_t phyChannel = 15;
uint8_t edLevel;
int8_t pwrDbm;
PibValue_t pibValue;

// Setting Current channel
pibValue.pib_value_8bit = phyChannel;
retVal = PHY_PibSet(phyCurrentChannel, &pibValue);
if(PHY_SUCCESS == retVal)
{
    //Take the Ed sample
    edLevel = PHY_EdSample();
    //Convert the energy level to input power in Dbm
    pwrDbm = (int8_t)(edLevel + PHY_GetRSSIBaseVal());
}

```
## Remarks

PHY_EdSample scans the channel for 8 symbols(128us) and returns the energy level 

