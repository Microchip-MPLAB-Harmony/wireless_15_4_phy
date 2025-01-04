/*******************************************************************************
  PAL Header

  File Name:
    pal_pta.h

  Summary:
    This file contains Platform Abstraction Layer API function declarations

  Description:
    PAL Layer provides the interface to Timers, Interrupts and other platform 
    related resources. PHY layer is using PAL for its internal operations
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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
#ifndef PAL_PTA_API_H
#define PAL_PTA_API_H

/*
 * This module acts as a wrapper layer between the Wireless stack and the Harmony
 * drivers and peripherals
 * All hardware level access to the Harmony drivers from the stack happens through
 * this module 
 */
// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************
#include "definitions.h" 
#include "pal.h"

// *****************************************************************************
// *****************************************************************************
// Section: Types
// *****************************************************************************
// *****************************************************************************
 
/* PTA Debug Info */
typedef struct pal_pta_debug_info
{
    uint64_t tx_req_wo_prio;
    uint64_t tx_req_wi_prio;
    uint64_t tx_abort_wo_prio;
    uint64_t tx_abort_wi_prio;
    uint64_t rx_req_wo_prio;
    uint64_t rx_req_wi_prio;
    uint64_t rx_abort_wo_prio;
    uint64_t rx_abort_wi_prio; 
    uint64_t ed_req_wo_prio;
    uint64_t ed_req_wi_prio;
    uint64_t ed_abort_wo_prio;
    uint64_t ed_abort_wi_prio;
}pal_pta_debug_info_t;


// *****************************************************************************
// *****************************************************************************
// Section: Externals
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Function Prototypes
// *****************************************************************************
// *****************************************************************************

#ifdef __cplusplus
extern "C" {
#endif

// *****************************************************************************
/*
  Function:
    PAL_Status_t PAL_PTA_Init(PHY_PtaConfig_t *pta_config)

  Summary:
    Initialization of PAL PTA

  Description:
    This function initializes the PTA Coex and initializes the PTA Config 
	variables

  Precondition:
    None 

  Parameters:
    pta_config - Desired Configuration for the pta.

  Returns:
    PAL_Status_t - PAL_SUCCESS - if PAL initialization is successful
                   PAL_FAILURE - otherwise

  Example:
    <code>
	PHY_PtaConfig_t *AppPtaConfig;
	AppPtaConfig.tx.cca_backoff_prio = TX_PRIO_PENULTIMATE;
	AppPtaConfig.tx.mac_retry_prio = TX_PRIO_PENULTIMATE;
    AppPtaConfig.rx.prio = RX_PRIO_ADDR_MATCH;
    AppPtaConfig.ed.enable = true;
    AppPtaConfig.debug.enable = true;        
	
	PAL_Status_t retVal = PAL_FAILURE;
	retVal = PAL_PTA_Init(AppPtaConfig);
    if (PAL_SUCCESS =! retVal)
    {
        while(1);
    }
    </code>

  Remarks:
    This routine is should be call from the Application to set the desired 
	parameters for PTA Usage. 
*/

PAL_Status_t PAL_PTA_Init(PHY_PtaConfig_t *pta_config);

// *****************************************************************************
/*
  Function:
	PAL_Status_t PAL_PTA_Enable(bool enable)

  Summary:
    Enables/Disables the PTA CoEx feature

  Description:
    This function enables/disables the PTA CoEx feature.

  Precondition:
   PAL_PTA_Init() should have been called before calling this function. 

  Parameters:
   enable - boolean value to enable or disables
            True  - Enables the PTA CoEx Feature.
			False - Disables the PTA CoEx Feature.

  Returns:
    PAL_Status_t - PAL_SUCCESS - if PAL initialization is successful
                   PAL_FAILURE - otherwise

  Example:
    <code>
    PAL_PTA_Enable(True);
    </code>

  Remarks:
	None
*/

PAL_Status_t PAL_PTA_Enable(bool enable);

// *****************************************************************************
/*
  Function:
    PAL_Status_t PAL_PTA_GetConfig(PHY_PtaConfig_t *pta_config)

  Summary:
    This function provides the PTA CoEx Configuration set. 

  Description:
    This function provides the PTA CoEx Configuration structure.

  Precondition:
    PAL_PTA_Init() should have been called before calling this function. 
	PAL_PTA_Enable(enable) should have been called before calling this function.

  Parameters:
    pta_config - structure to get PTA CoEx.

  Returns:
    PAL_Status_t - PAL_SUCCESS - if PAL initialization is successful
                   PAL_FAILURE - otherwise

  Example:
    <code>
    PAL_Status_t retVal = PAL_FAILURE;
	
	retVal = PAL_PTA_Init();
	
	retVal = PAL_PTA_Enable(True);
	
    PHY_PtaConfig_t ptaConfig;
    
    PAL_PTA_GetConfig(&ptaConfig);
        
    </code>

  Remarks:
    None
*/

PAL_Status_t PAL_PTA_GetConfig(PHY_PtaConfig_t *pta_config);

// *****************************************************************************
/*
  Function:
    PAL_Status_t PAL_PTA_SetConfig(PHY_PtaConfig_t pta_config)

  Summary:
    This function sets the PTA CoEx Configurations.

  Description:
    This function sets the PTA CoEx Configurations.

  Precondition:
    PAL_PTA_Init() should have been called before calling this function. 
	PAL_PTA_Enable(enable) should have been called before calling this function.

  Parameters:
    pta_config - structure to set PTA CoEx.

  Returns:
    PAL_Status_t - PAL_SUCCESS - if PAL initialization is successful
                   PAL_FAILURE - otherwise

  Example:
    <code>
    PAL_Status_t retVal = PAL_FAILURE;
	
	retVal = PAL_PTA_Init();
	
	retVal = PAL_PTA_Enable(True);
	
	PHY_PtaConfig_t AppPtaConfig;
	AppPtaConfig.tx.cca_backoff_prio = TX_PRIO_PENULTIMATE;
	AppPtaConfig.tx.mac_retry_prio = TX_PRIO_PENULTIMATE;
    AppPtaConfig.rx.prio = RX_PRIO_ADDR_MATCH;
    AppPtaConfig.ed.enable = true;
    AppPtaConfig.debug.enable = true; 
	
	PAL_PTA_SetConfig(AppPtaConfig);
	
    </code>

  Remarks:
	Timer should be started before stopping it
*/

PAL_Status_t PAL_PTA_SetConfig(PHY_PtaConfig_t pta_config);

// *****************************************************************************
/*
  Function:
	PAL_Status_t PAL_PTA_GetDebugCtrs(pal_pta_debug_info_t *pta_debug_ctrs)

  Summary:
    Gets the Debug Counter info

  Description:
    This function returns the Debug counter information.

  Precondition:
    PAL_PTA_Enable(True) should have been called before calling this function.

  Parameters:
    pta_debug_ctrs - Structure pointer to get the debug counters info.

  Returns:
    PAL_Status_t - PAL_SUCCESS - if PAL initialization is successful
                   PAL_FAILURE - otherwise 

  Example:
    <code>
	PAL_Status_t retVal = PAL_FAILURE;
    retVal = PAL_PTA_Enable(True);
	pal_pta_debug_info_t pta_dbg_Info;
	PAL_PTA_GetDebugCtrs(&pta_dbg_Info);
    </code>

  Remarks:
	None
*/

PAL_Status_t PAL_PTA_GetDebugCtrs(pal_pta_debug_info_t *pta_debug_ctrs);


// *****************************************************************************
/*
  Function:
	void PAL_PTA_ResetDebugCtrs(void)

  Summary:
    Reset the Debug Counter info

  Description:
    This function resets the Debug counter information.

  Precondition:
    None

  Parameters:
   None

  Returns:
    None

  Example:
    <code>
     PAL_PTA_ResetDebugCtrs();
    </code>

  Remarks:
	None
*/

void PAL_PTA_ResetDebugCtrs(void);

// *****************************************************************************
/*
  Function:
	uint8_t PAL_PTA_IsEnabled(void)

  Summary:
    Get the PTA Enable/Disable status

  Description:
    This function returns the PTA Enable/Disable status.

  Precondition:
    None

  Parameters:
   None

  Returns:
    uint8_t - true: PTA is enabled
	        - false: PTA is Disbaled

  Example:
    <code>
     PAL_PTA_IsEnabled();
    </code>

  Remarks:
	None
*/
uint8_t PAL_PTA_IsEnabled(void);


/* ! @} */
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif  /* PAL_H */
/* EOF */
