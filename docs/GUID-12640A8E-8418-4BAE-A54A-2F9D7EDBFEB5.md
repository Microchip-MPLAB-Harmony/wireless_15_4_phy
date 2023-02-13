# PHY_TrxState_t Enum

## C

```c
typedef enum phy_trx_state_tag{
    /* Transceiver to be configured to Transceiver OFF state*/
    PHY_STATE_TRX_OFF,
    /* Transceiver to be configured to Receiver ON state */
    PHY_STATE_RX_ON
}PHY_TrxState_t;

```

## Summary

Enumeration for Transceiver States that can be set/configured 

## Description

|State|Description|
|:----|:----------|
|PHY_STATE_TRX_OFF| Configures the transceiver to TRX_OFF state |
|PHY_STATE_RX_ON | Configures the transceiver to RX_ON state |
## Remarks

Once the tranceiver state is set to RX_ON, it will stay in receive mode after each reception and transmission. User has to configure the TRX to change the state to TRX_OFF if needed.

