﻿![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip PIC32CX-BZ2 Device Standalone IEEE 802.15.4 Physical Layer Release Notes

## Release v1.3.0

### Features
- Support for WBZ451H high power module

### Known Issues
- None

## Development Tools
- [MPLAB X v6.20 or later](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB® XC32 C/C++ Compiler v4.40 or later](https://www.microchip.com/mplab/compilers)
-   MPLAB® X IDE plug-ins: MPLAB® Code Configurator (MCC) v5.5.0 and above
-   Device Pack: PIC32CX-BZ2-DFP (1.4.243)

__________________

## Release v1.2.0

### New Features
- Adding Support for Software CSMA and basic transceiver modes operations.
- Enhancements to Tx power handling algorithm.


### Bug fixes
- Fix for BLE is failing to initialize if PHY_TrxSleep is called before
- Fix for load Calibration value for wireless_15_4_phy

### Known Issues
- None

## Development Tools
-   MPLAB X v6.20 or later
-   MPLAB® XC32 C/C++ Compiler v4.35 or later
-   MPLAB® X IDE plug-ins: MPLAB® Code Configurator (MCC) v5.5.0 and above
-   Device Pack: PIC32CX-BZ2-DFP (1.4.241)

## Notes
- None

__________________

## Release v1.1.1

### Bug fixes

- Fix of dependency version string in package.yml

__________________

## Release v1.1.0

### New Features
- Introduced new API PHY_IsFramePendingFromNextLayer
- PHY Library Update for handling Tx Power (EIRP)/Ant Gain Setting for WBZ451 and 450 based on the regions


### Bug fixes
- Fix for checking the BMM buffer availability frequently if there is no buffer

### Known Issues
- None

## Development Tools
-	MPLAB X v6.15
-	MPLAB® XC32 C/C++ Compiler v4.21
-	MPLAB® X IDE plug-ins: MPLAB® Code Configurator (MCC) v5.3.7 and above
-	Device Pack: PIC32CX-BZ2-DFP (1.2.230)

## Notes
-	None

__________________

## Release v1.0.0

The physical layer contains the transceiver specific functionalities as mentioned as the requirements of IEEE 802.15.4 specification. It gives the interface to the MAC core layer which is independent of the underlying transceiver.
Besides that, the PHY layer provides the set of APIs which can be used to interface a basic application.
The following are the funcionalities of PHY layer

-	Frame Transmission  (including automatic frame retries)
-	Frame reception  (including automatic acknowledgement handling)
-	PHY PIB storage
-	CSMA module
-	Energy detection
-	Power management(Trx Sleep)
-	Interrupt handling
-	Initialization and Reset
-	Enabling High Datarate Support
-	Enabling Promiscuous Mode
-	Enabling Antenna Diversity
-	Enabling Reduced Power consumption modes
-	Enabling reception of reserved frames

## Known Issues / Limitations

-	No issues

## Development Tools
-	MPLAB X v6.05
-	MPLAB® XC32 C/C++ Compiler v4.21
-	MPLAB® X IDE plug-ins: MPLAB® Code Configurator (MCC) v5.2.2 and above
-	Device Pack: PIC32CX-BZ2-DFP (1.1.218)

## Notes
-	None


