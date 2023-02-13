# PHY_FrameInfo_t Struct

## C

```c
typedef struct frame_info_tag
{
    /** Pointer to buffer header of frame */
    buffer_t *buffer_header;
    /** Pointer to MPDU */
    uint8_t *mpdu;
} PHY_FrameInfo_t;

```

## Summary

PHY_FrameInfo_t holds the data to be transmitted or the data being received by the transceiver.  

## Description
| Param | Description |
|:------|:------------|
| bufferHeader | Pointer to transmit buffer |
| mpdu | Pointer to the PHY Payload. mpdu[0] should hold the length of the payload(N) + 1 (for length field length) |
| mpdu[1-N] | Hold the phyPayload  |

## Remarks

None 

