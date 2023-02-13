# PHY_RxFrameCallback Function

## C

```c
void PHY_RxFrameCallback(PHY_FrameInfo_t *rxFrame)
```

## Summary

User callback function for the reception of a frame  

## Description

This callback function SHOULD be defined by the upper layer(Application/MAC)
for getting the received frame details

## Precondition

This is a Asynchronous function call for the reception of a frame  

## Parameters

| Param | Description |
|:----- |:----------- |
| rxFrame | Pointer to received frame structure of type PHY_FrameInfo_t or to received frame array |
| |rxFrame->buffer_header - BMM Buffer Header of the frame |
| |rxFrame->mpdu - Actual MPDU comprises of |
| |mpdu[0]  - Payload Length(N) |
| |mpdu[1-N]- Payload mpdu[N+1]- LQI of received packet |
| |mpdu[N+2]- ED_LEVEL of received packet |

## Returns

None  

## Example

```c
uint8_t rxBuffer[LARGE_BUFFER_SIZE];
uint8_t frameLen, frameLQI, frameED;
int8_t frameRSSI;
void PHY_RxFrameCallback(PHY_FrameInfo_t *frame)
{
    printf("\n--RxCallbackreceived--");
    frameLen = frame->mpdu[0];
    //Copy the payload
    memcpy(rxBuffer, (uint8_t *)&(frame->mpdu[1]), frameLen);
    //Copy the LQI
    frameLQI = frame->mpdu[frameLen+LQI_LEN];
    //Copy the RSSI
    frameED = frame->mpdu[frameLen+LQI_LEN+ED_VAL_LEN];
    
    frameRSSI = (int8_t)(frameED + PHY_GetRSSIBaseVal());
    
    // free the buffer that was used for frame reception
    bmm_buffer_free((buffer_t *)(frame->buffer_header));
}
```

## Remarks

bmm_buffer_free SHOULD be called in the PHY_RxFrameCallback() for reusing the buffer for reception. Otherwise no buffers will be availble for reception. Number of buffers can be increased by changing the NUMBER_OF_LARGE_PHY_BUFS in stack_config.h. By default, the value is 3. 
If the buffer is not freed upon receiving the packet, transceiver can receive upto NUMBER_OF_LARGE_PHY_BUFS (3) frames only.



