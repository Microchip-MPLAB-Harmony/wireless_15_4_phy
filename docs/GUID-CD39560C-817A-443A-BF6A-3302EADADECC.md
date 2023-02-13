# PHY_GetRSSIBaseVal Function

## C

```c
int8_t PHY_GetRSSIBaseVal(void)
```

## Summary

Get RSSI base value of TRX  

## Description

This function is called to get the base RSSI value for respective
radios

## Precondition

PHY_Init() should have been called before calling this function  

## Parameters

None  

## Returns

Integer contains RSSI value

## Example

```c
int8_t trxBaseRSSI;

// Get RSSI base value of TRX
trxBaseRSSI = PHY_GetRSSIBaseVal();

```

## Remarks

None
