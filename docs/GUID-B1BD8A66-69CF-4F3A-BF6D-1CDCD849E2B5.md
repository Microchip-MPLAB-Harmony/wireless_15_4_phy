# PHY_Init Function

## C

```c
PHY_Retval_t PHY_Init( void )
```

## Summary

Initialization of PHY Layer  

## Description

This function is called to initialize the PHY layer. The transceiver is
initialized and it will be in PHY_STATE_TRX_OFF, the PHY PIBs are set to
their default values. PAL layer is initialized

## Precondition

SYS_Load_Cal(WSS_ENABLE_ZB) function of device support library should be called before calling this function.  

## Parameters

None.  

## Returns

*PHY_SUCCESS* - If the transceiver state is changed to TRX_OFF

*PHY_FAILURE* - Otherwise
 

## Example

```c
PHY_Retval_t retVal = PHY_FAILURE;

retVal = PHY_Init();
if (PHY_SUCCESS =! retVal)
{
    while(1);
}
```

## Remarks

This routine must be called before any of the PHY function is called 

