# bmm_buffer_init Function

## C

```c
void bmm_buffer_init(void)
```

## Summary

Initializes the buffer module  

## Description

This function initializes the buffer module.
This function should be called before using any other functionality
of buffer module

## Precondition

None  

## Parameters

None.  

## Returns

None.  

## Example

```c
bmm_buffer_init();
```

## Remarks

This routine is called by the PHY Layer during PHY Initialization (PHY_Init). Application can directly allocate the buffer and use it. Number of Buffers should be defined as per application needs before ausing the buffer 

