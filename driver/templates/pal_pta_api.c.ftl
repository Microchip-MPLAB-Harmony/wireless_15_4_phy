/*******************************************************************************
  PAL Source

  File Name:
    pal.c

  Summary:
    Performs interface functionalities between the PHY layer and Harmony
    drivers

  Description:
 *  None
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

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Included Files                                                    */
/* ************************************************************************** */
/* ************************************************************************** */
#include <string.h>
#include <stdio.h>
#include "pal.h"
#include "pal_pta_api.h"
#include "pal_pta_interface.h"
#include "system/time/sys_time.h"
#include "phy.h"

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Macros                                                  */
/* ************************************************************************** */
/* ************************************************************************** */

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Prototypes                                                   */
/* ************************************************************************** */
/* ************************************************************************** */

static void palNotifyUpdatedPTAStatus(void);

static PHY_PtaConfig_t  gs_pta_config;

pal_pta_debug_info_t gs_pta_debug_ctrs;

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Function Implementation                                                   */
/* ************************************************************************** */
/* ************************************************************************** */
PAL_Status_t PAL_PTA_Init(PHY_PtaConfig_t *pta_config)
{
    PAL_Status_t status = PAL_SUCCESS;
    if(NULL != pta_config)
    {
        gs_pta_config.tx.cca_backoff_prio = pta_config->tx.cca_backoff_prio;
        gs_pta_config.tx.mac_retry_prio = pta_config->tx.mac_retry_prio;
        gs_pta_config.rx.prio = pta_config->rx.prio;
        gs_pta_config.ed.enable = pta_config->ed.enable;
        gs_pta_config.debug.enable = pta_config->debug.enable;
    }
    else // Default configuration will be used, if application is not configuring it's own values
    {
        gs_pta_config.ptaenable = true;
        gs_pta_config.tx.cca_backoff_prio = ${PHY_PTA_TX_CCA_PRIORITY_LEVEL};
        gs_pta_config.tx.mac_retry_prio = ${PHY_PTA_TX_MAC_RETRY_PRIORITY_LEVEL};
        gs_pta_config.rx.prio = ${PHY_PTA_RX_PRIORITY_LEVEL};
		<#if PHY_PTA_ED_PRIORITY == true>
		gs_pta_config.ed.enable = true;
		<#else>
        gs_pta_config.ed.enable = false;
		</#if>
		<#if PHY_PTA_DEBUG_CONFIG_ENABLE == true>
		gs_pta_config.debug.enable = true;
		<#else>
        gs_pta_config.debug.enable = false;
		</#if>
    }
    palNotifyUpdatedPTAStatus();
    return status;
}

PAL_Status_t PAL_PTA_Enable(bool enable)
{
    PAL_Status_t status = PAL_SUCCESS;
    gs_pta_config.ptaenable = enable;
    palNotifyUpdatedPTAStatus();
    return status;
    
}

uint8_t PAL_PTA_IsEnabled(void)
{
    return gs_pta_config.ptaenable;
}

PAL_Status_t PAL_PTA_GetConfig(PHY_PtaConfig_t *pta_config)
{
    PAL_Status_t status = PAL_SUCCESS;
    if (gs_pta_config.ptaenable)
    {
        memcpy(pta_config,&gs_pta_config,sizeof(PHY_PtaConfig_t));
    }
    else
    {
        status = PAL_PTA_DISABLED; 
    }
    return status;
}

PAL_Status_t PAL_PTA_SetConfig(PHY_PtaConfig_t pta_config)
{
    PAL_Status_t status = PAL_SUCCESS;
    if (gs_pta_config.ptaenable)
    {
        memcpy(&gs_pta_config,&pta_config,sizeof(PHY_PtaConfig_t));
        palNotifyUpdatedPTAStatus();
        
    }
    else
    {
        status = PAL_PTA_DISABLED; 
    }
    return status;    
}

PAL_Status_t PAL_PTA_GetDebugCtrs(pal_pta_debug_info_t *pta_debug_ctrs)
{
    PAL_Status_t status = PAL_SUCCESS;
    if ((gs_pta_config.ptaenable) && (gs_pta_config.debug.enable))
    {
        memcpy(pta_debug_ctrs,&gs_pta_debug_ctrs,sizeof(pal_pta_debug_info_t));
    }
    else
    {
        status = PAL_PTA_DEBUG_DISABLED; 
    }
    return status;        
}

void PAL_PTA_ResetDebugCtrs(void)
{
   gs_pta_debug_ctrs.ed_abort_wi_prio = 0;
   gs_pta_debug_ctrs.ed_abort_wo_prio = 0;
   gs_pta_debug_ctrs.ed_req_wi_prio = 0;
   gs_pta_debug_ctrs.ed_req_wo_prio = 0;
   gs_pta_debug_ctrs.rx_abort_wi_prio = 0;
   gs_pta_debug_ctrs.rx_abort_wo_prio = 0;
   gs_pta_debug_ctrs.rx_req_wi_prio = 0;
   gs_pta_debug_ctrs.rx_req_wo_prio = 0;
   gs_pta_debug_ctrs.tx_abort_wi_prio = 0;
   gs_pta_debug_ctrs.tx_abort_wo_prio = 0;
   gs_pta_debug_ctrs.tx_req_wi_prio = 0;
   gs_pta_debug_ctrs.tx_req_wo_prio = 0;
}

static void palNotifyUpdatedPTAStatus(void)
{
	PHY_PtaReq_t req;
	if(gs_pta_config.ptaenable)
	{
		req.pta_req_tx_set = &PAL_PTA_TxReqSet;
		req.pta_req_rx_set = &PAL_PTA_RxReqSet;
		if(gs_pta_config.ed.enable)
	    {
			req.pta_req_ed_set = &PAL_PTA_EdReqSet;
	    }
		else
		{
			req.pta_req_ed_set = NULL;
		}
	}
	else
	{
		req.pta_req_tx_set  = NULL;
		req.pta_req_rx_set  = NULL;
		req.pta_req_ed_set  = NULL;
	}
    PHY_NotifyUpdatedPTAStatus(&req,&gs_pta_config);
}

