/*******************************************************************************
  PHY Layer Constants Header

  File Name:
    phy_constants.h

  Summary:
    This file contains PHY Layer constants definitions

  Description:
    None
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

/* Prevent double inclusion */
#ifndef PHY_CONSTANTS_H
#define PHY_CONSTANTS_H

// *****************************************************************************
// *****************************************************************************
// Section: Includes
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Externals
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Macros
// *****************************************************************************
// *****************************************************************************
/** Minimum channel */
#define MIN_CHANNEL                 (11)

/** Maximum channel */
#define MAX_CHANNEL                 (26)

/** Valid channel masks for scanning */
#define VALID_CHANNEL_MASK          (0x07FFF800UL)

/*
 * 4 bits form one symbol since O-QPSK is used
 */
/** Symbols per octet */
#define SYMBOLS_PER_OCTET                   (2)

/** Number of symbols included in the preamble */
#define NO_SYMBOLS_PREAMBLE                 (8)

/** Number of symbols included in the SFD field */
#define NO_SYMBOLS_SFD                      (2)

/**
 * Number of symbols forming the synchronization header (SHR) for the current
 * PHY.
 * This value is the base for the PHY PIB attribute phySHRDuration.
 */
#define NO_OF_SYMBOLS_PREAMBLE_SFD          (NO_SYMBOLS_PREAMBLE + \
	NO_SYMBOLS_SFD)

/**
 * Maximum number of symbols in a frame for the current PHY.
 * This value is the base for the PHY PIB attribute phyMaxFrameDuration.
 */
#define MAX_FRAME_DURATION \
	(NO_OF_SYMBOLS_PREAMBLE_SFD + \
	(aMaxPHYPacketSize + 1) * SYMBOLS_PER_OCTET)

/**
 * The maximum time in symbols for a 32 bit timer
 */
#define MAX_SYMBOL_TIME                     (0x0FFFFFFF)

/**
 * Symbol mask for ignoring most significant nibble
 */
#define SYMBOL_MASK                         (0x0FFFFFFF)

/**
 * Maximum PDT Level 
 */
#define MAX_PDT_LEVEL                       (0x0F)
 
/**
 * TX Power Tolerance 
 */
#define TX_PWR_TOLERANCE                              (0x80)

/*
 * Default tx power for Ch26 to meet FCC compliance
 */
#define DEFAULT_TX_POWER_CH26             (TX_PWR_TOLERANCE | 0x0d)

/** 
 * Constant ANTENNA_DIVERSITY_ENABLE 
 */
#define ANTENNA_DIVERSITY_ENABLE            (1)

/** 
 * Constant ANTENNA_DIVERSITY_DISABLE 
 */
#define ANTENNA_DIVERSITY_DISABLE           (0)

/** 
 * Constant ANTENNA_CTRL_0 
 */
#define ANTENNA_CTRL_0                      (0)

/** 
 * Constant ANTENNA_CTRL_1 
 */
#define ANTENNA_CTRL_1                      (1)

/** 
 * Constant ANTENNA_CTRL_2 
 */
#define ANTENNA_CTRL_2                      (2)

/** 
 * Constant ANTENNA_CTRL_3 
 */
#define ANTENNA_CTRL_3                      (3)

/** 
 * Constant PA_EXT_ENABLE 
 */
#define PA_EXT_ENABLE                       (1)

/** 
 * Constant PA_EXT_DISABLE 
 */
#define PA_EXT_DISABLE                      (0)

/** 
 * Constant PWR_REGISTER_VALUE 
 */
#define PWR_REGISTER_VALUE                  (1)

/** 
 * Constant PWR_DBM_VALUE 
 */
#define PWR_DBM_VALUE                       (0)

/** 
 * Constant PROMISCUOUS_ENABLE 
 */
#define PROMISCUOUS_ENABLE                  (1)

/** 
 * Constant PROMISCUOUS_DISABLE 
 */
#define PROMISCUOUS_DISABLE                 (0)


/* Constant Total number of Timers used by the PHY Layer*/
#define NUMBER_OF_TOTAL_STACK_TIMERS        (1)


// *****************************************************************************
// *****************************************************************************
// Section: Prototypes
// *****************************************************************************
// *****************************************************************************

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* PHY_CONSTANTS_H */

/* EOF */
