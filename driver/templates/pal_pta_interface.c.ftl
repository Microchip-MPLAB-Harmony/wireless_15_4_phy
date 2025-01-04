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
#include "pal_pta_interface.h"
#include "phy.h"
<#if PHY_PTA_ENABLE == true>
#include "pta.h"
#include "pal_pta_api.h"
</#if>

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
<#if PHY_PTA_ENABLE == true>
static void PAL_PTA_AbortRequest(void);
static ptaIrqHandler phyPtaIrqHandler = NULL;
extern pal_pta_debug_info_t gs_pta_debug_ctrs;
volatile bool ptaReqSet = false;

static PHY_TRNSC_TYPE_T trnscType;
</#if>
/* ************************************************************************** */
/* ************************************************************************** */
/* Section: Function Implementation                                                   */
/* ************************************************************************** */
/* ************************************************************************** */
<#if PHY_PTA_ENABLE == true>
void PAL_PTA_InitInterface(void)
{
    phyPtaIrqHandler = (ptaIrqHandler)PHY_RegisterPtaIrqHandler();
}

uint8_t PAL_PTA_TxReqSet(uint8_t setPrio)
{
    uint8_t status = true;
    
    if(PTA_GetReq())
    {
        return false;
    }
    
    if(setPrio)
    {
        PTA_PrioSet(); 
                
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);
        
        trnscType = TX_WI_PRIO;
        gs_pta_debug_ctrs.tx_req_wi_prio++;
    }
    else
    {
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);
        
        trnscType = TX_WO_PRIO;
        gs_pta_debug_ctrs.tx_req_wo_prio++;
    }

    ptaReqSet = true;
    return status;
    
}

uint8_t PAL_PTA_RxReqSet(uint8_t setPrio)
{
    uint8_t status = true;
    
    if(PTA_GetReq())
    {
        return false;
    }
    
    if(setPrio)
    {
        PTA_PrioSet(); 
                
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);
        
        trnscType = RX_WI_PRIO;
        gs_pta_debug_ctrs.rx_req_wi_prio++;
    }
    else
    {
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);
        
        trnscType = RX_WO_PRIO;
        gs_pta_debug_ctrs.rx_req_wo_prio++;
    }

    ptaReqSet = true;
    return status;
    
}

uint8_t PAL_PTA_EdReqSet(uint8_t setPrio)
{
    bool status = true;

    if(PTA_GetReq())
    {
        return false;
    }
    
    
    if(setPrio)
    {
        PTA_PrioSet(); 
                
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);

        trnscType = ED_WI_PRIO;
        gs_pta_debug_ctrs.ed_req_wi_prio +=1;
    }
    else
    {
        PTA_ReqSet((void*)&PAL_PTA_AbortRequest);
        
        trnscType = ED_WO_PRIO;
        gs_pta_debug_ctrs.ed_req_wo_prio +=1;
    }
    
    ptaReqSet = true;
    return status;
    
}
</#if>
void PAL_PTA_ReqClear(void)
{
<#if PHY_PTA_ENABLE == true>
    PTA_ReqClear();
    PTA_PrioClear(); 
</#if>

}

void PAL_PTA_ClearRegisterIrq(void)
{
<#if PHY_PTA_ENABLE == true>
    PTA_ClearIrqHandler();
    ptaReqSet = false;
</#if>
}

uint8_t PAL_PTA_GetWlanStatus(void)
{
<#if PHY_PTA_ENABLE == true>
    if(PAL_PTA_IsEnabled())
        return PTA_WlanStatus();
    else
        return false;
<#else>
    return false;
</#if>
}
<#if PHY_PTA_ENABLE == true>
static void PAL_PTA_AbortRequest(void)
{
    volatile bool status = false; 
    if(phyPtaIrqHandler != NULL)
    {
        if((ptaReqSet == true) && (PAL_PTA_GetWlanStatus() == true))
        {
            status = phyPtaIrqHandler();
            if(status == false)
                return;
        }
        else
        {
            return;
        }
    }
    
    switch(trnscType)
    {
        case TX_WO_PRIO:
        {
            gs_pta_debug_ctrs.tx_abort_wo_prio+=1;
        }
        break;
        
        case TX_WI_PRIO:
        {
            gs_pta_debug_ctrs.tx_abort_wi_prio+=1;
        }
        break;
        
        case RX_WO_PRIO:
        {
            gs_pta_debug_ctrs.rx_abort_wo_prio+=1;
        }
        break;
        
        case RX_WI_PRIO:
        {
            gs_pta_debug_ctrs.rx_abort_wi_prio+=1;
        }
        break;
        
        case ED_WO_PRIO:
        {
            gs_pta_debug_ctrs.ed_abort_wo_prio+=1;
        }
        break;
        
        case ED_WI_PRIO:
        {
            gs_pta_debug_ctrs.ed_abort_wi_prio+=1;
        }
        break;
        
        default:
            break;
    }
}
</#if>