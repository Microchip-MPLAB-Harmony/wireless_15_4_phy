# coding: utf-8
##############################################################################
# Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
###############################################################################

# === PTA Configuration
#
# Interface
#
##PTA Callback

global sort_alphanumeric

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

global handlePTA_Support
def handlePTA_Support(args):
    ptaEnabled = args['isEnabled']
    source  = args['source']
    print("DevSupport:",args)
    
    if ptaEnabled == True:
        phyMenupta.setVisible(True)
        phyPtaInterface.setVisible(True)
        phyptaPriorityConfig.setVisible(True)
        phyptaDebugConfig.setVisible(True)
        phyEnablePta.setValue(True)
    else:
        phyMenupta.setVisible(False)
        phyPtaInterface.setVisible(False)
        phyptaPriorityConfig.setVisible(False)
        phyptaDebugConfig.setVisible(False)
        phyEnablePta.setValue(False)
        

def ptaConfigurationCallback(symbol,event):
    symbolID = event["id"]
    value = event["value"]
    print("phy-symbolID:",symbolID,"value:",value)
    
    if (deviceName in pic32cx_bz2_family):
        devSupportLib = "pic32cx_bz2_devsupport"
    elif (deviceName in pic32cx_bz3_family):
        devSupportLib = "pic32cx_bz3_devsupport"
    
    if symbolID == "PHY_PTA_ENABLE":
        if value == True:
            # phyPtaInterface.setVisible(True)
            # phyptaPriorityConfig.setVisible(True)
            # phyptaDebugConfig.setVisible(True)
            phypalptaApiHeaderFile.setEnabled(True)
            phypalptaApiSourceFile.setEnabled(True)
            phypalptaInterfaceHeaderFile.setEnabled(True)
            phypalptaInterfaceSourceFile.setEnabled(True)
        else:
            # phyPtaInterface.setVisible(False)
            # phyptaPriorityConfig.setVisible(False)
            # phyptaDebugConfig.setVisible(False)
            phypalptaApiHeaderFile.setEnabled(False)
            phypalptaApiSourceFile.setEnabled(False)
            phypalptaInterfaceHeaderFile.setEnabled(True)
            phypalptaInterfaceSourceFile.setEnabled(True)
            
    elif symbolID == "PHY_PTA_INTERFACE":
        if phyEnablePta.getValue() == True:
            if value == 0:
                # phyptaReqPin.setVisible(True)
                # phyptaWlanActivePin.setVisible(True)
                if Database.getSymbolValue(devSupportLib,"BLE_PTA_SUPPORTED") == False:
                    Database.setSymbolValue(devSupportLib,"PTA_INTERFACE",0)
                phyptaPriorityConfig.setVisible(True)
                # phyptaPriorityPin.setVisible(True)
                phyptaDebugConfig.setVisible(True)
                phypalptaApiHeaderFile.setEnabled(True)
                phypalptaApiSourceFile.setEnabled(True)
                phypalptaInterfaceHeaderFile.setEnabled(True)
                phypalptaInterfaceSourceFile.setEnabled(True)
                phyptaTxCCAPriorityLevel.setReadOnly(False)
                phyptaTxMACRetryPriorityLevel.setReadOnly(False)
                phyptaRXPriorityLevel.setReadOnly(False)
                phyptaEDPriority.setReadOnly(False)
                phyptaTxCCAPriorityLevel.setValue(1)
                phyptaTxMACRetryPriorityLevel.setValue(1)
                phyptaRXPriorityLevel.setValue(1)
                phyptaEDPriority.setValue(False)
            elif value == 1:
                # phyptaReqPin.setVisible(False)
                # phyptaWlanActivePin.setVisible(True)
                if Database.getSymbolValue(devSupportLib,"BLE_PTA_SUPPORTED") == False:
                    Database.setSymbolValue(devSupportLib,"PTA_INTERFACE",1)
                phyptaPriorityConfig.setVisible(True)
                # phyptaPriorityPin.setVisible(True)
                phyptaDebugConfig.setVisible(True)
                phypalptaApiHeaderFile.setEnabled(True)
                phypalptaApiSourceFile.setEnabled(True)
                phypalptaInterfaceHeaderFile.setEnabled(True)
                phypalptaInterfaceSourceFile.setEnabled(True)
                phyptaTxCCAPriorityLevel.setValue(0)
                phyptaTxMACRetryPriorityLevel.setValue(0)
                phyptaRXPriorityLevel.setValue(0)
                phyptaEDPriority.setValue(True)
                phyptaTxCCAPriorityLevel.setReadOnly(True)
                phyptaTxMACRetryPriorityLevel.setReadOnly(True)
                phyptaRXPriorityLevel.setReadOnly(True)
                phyptaEDPriority.setReadOnly(True)
    
    # elif symbolID == "PTA_ENABLE":
        # if value == False:
           # phyEnablePta.setValue(False)
        # elif value == True:
            # phyEnablePta.setValue(True)
    
    elif symbolID == "BLE_PTA_SUPPORTED":
        if value == True:
            phyPtaInterface.setValue(0)
            phyPtaInterface.setReadOnly(True)
        else:
            phyPtaInterface.setReadOnly(False)
            
            
global phyMenupta
phyMenupta = ieee802154phy.createMenuSymbol("PHY_PTA_MENU", None)
phyMenupta.setLabel("PTA Configuration")
phyMenupta.setVisible(False)


global phyEnablePta
phyEnablePta = ieee802154phy.createBooleanSymbol("PHY_PTA_ENABLE",phyMenupta)
phyEnablePta.setLabel("Enable PTA CoEx")
phyEnablePta.setVisible(False)
phyEnablePta.setDefaultValue(False)
if (deviceName in pic32cx_bz2_family):
    phyEnablePta.setDependencies(ptaConfigurationCallback,["pic32cx_bz2_devsupport.BLE_PTA_SUPPORTED"]) #BLESTACK_LOADED
elif (deviceName in pic32cx_bz3_family):
    phyEnablePta.setDependencies(ptaConfigurationCallback,["pic32cx_bz3_devsupport.BLE_PTA_SUPPORTED"])
    
global phyPtaInterface
phyPtaInterface = ieee802154phy.createKeyValueSetSymbol("PHY_PTA_INTERFACE",phyMenupta)
phyPtaInterface.setLabel("PTA Interface")
phyPtaInterface.addKey("3-Wire", "3-Wire", "3-Wire")
phyPtaInterface.addKey("2-Wire", "2-Wire", "2-Wire")
phyPtaInterface.setDefaultValue(0)
phyPtaInterface.setOutputMode("Value")
phyPtaInterface.setDisplayMode("Description")
phyPtaInterface.setDescription("PHY PTA Interface Line")
phyPtaInterface.setVisible(False)
phyPtaInterface.setReadOnly(False)
phyPtaInterface.setDependencies(ptaConfigurationCallback,["PHY_PTA_ENABLE","PHY_PTA_INTERFACE"])


global phyptaPriorityConfig
phyptaPriorityConfig = ieee802154phy.createMenuSymbol("PHY_PTA_PRIORITY_MENU", phyMenupta)
phyptaPriorityConfig.setLabel("Priority Configuration")
phyptaPriorityConfig.setVisible(False)

global phyptaTxPriorityLevelMenu
phyptaTxPriorityLevelMenu = ieee802154phy.createMenuSymbol("PHY_PTA_TX_PRIORITY_MENU",phyptaPriorityConfig)
phyptaTxPriorityLevelMenu.setLabel("TX Priority")
phyptaTxPriorityLevelMenu.setVisible(True)

global phyptaTxCCAPriorityLevel
phyptaTxCCAPriorityLevel = ieee802154phy.createKeyValueSetSymbol("PHY_PTA_TX_CCA_PRIORITY_LEVEL",phyptaTxPriorityLevelMenu)
phyptaTxCCAPriorityLevel.setLabel("CCA Priority Level")
phyptaTxCCAPriorityLevel.addKey("ALWAYS", "TX_PRIO_ALWAYS", "ALWAYS")
phyptaTxCCAPriorityLevel.addKey("PENULTIMATE", "TX_PRIO_PENULTIMATE", "PENULTIMATE")
phyptaTxCCAPriorityLevel.addKey("NEVER", "TX_PRIO_NEVER", "NEVER")
phyptaTxCCAPriorityLevel.setDefaultValue(1)
phyptaTxCCAPriorityLevel.setOutputMode("Value")
phyptaTxCCAPriorityLevel.setDisplayMode("Description")
phyptaTxCCAPriorityLevel.setDescription("PHY PTA CCA Priority Level")

global phyptaTxMACRetryPriorityLevel
phyptaTxMACRetryPriorityLevel = ieee802154phy.createKeyValueSetSymbol("PHY_PTA_TX_MAC_RETRY_PRIORITY_LEVEL",phyptaTxPriorityLevelMenu)
phyptaTxMACRetryPriorityLevel.setLabel("MAC Retry Priority Level")
phyptaTxMACRetryPriorityLevel.addKey("ALWAYS", "TX_PRIO_ALWAYS", "ALWAYS")
phyptaTxMACRetryPriorityLevel.addKey("PENULTIMATE", "TX_PRIO_PENULTIMATE", "PENULTIMATE")
phyptaTxMACRetryPriorityLevel.addKey("NEVER", "TX_PRIO_NEVER", "NEVER")
phyptaTxMACRetryPriorityLevel.setDefaultValue(1)
phyptaTxMACRetryPriorityLevel.setOutputMode("Value")
phyptaTxMACRetryPriorityLevel.setDisplayMode("Description")
phyptaTxMACRetryPriorityLevel.setDescription("PHY PTA TX Retry Priority Level")

global phyptaRXPriorityLevel
phyptaRXPriorityLevel = ieee802154phy.createKeyValueSetSymbol("PHY_PTA_RX_PRIORITY_LEVEL",phyptaPriorityConfig)
phyptaRXPriorityLevel.setLabel("RX Priority Level")
phyptaRXPriorityLevel.addKey("ALWAYS", "RX_PRIO_ALWAYS", "ALWAYS")
phyptaRXPriorityLevel.addKey("PREAMBLE_DETECT", "RX_PRIO_PREAMBLE_DETECT", "PREAMBLE_DETECT")
# phyptaRXPriorityLevel.addKey("ADDR_MATCH", "RX_PRIO_ADDR_MATCH", "ADDR_MATCH")
phyptaRXPriorityLevel.addKey("NEVER", "RX_PRIO_NEVER", "NEVER")
phyptaRXPriorityLevel.setDefaultValue(1)
phyptaRXPriorityLevel.setOutputMode("Value")
phyptaRXPriorityLevel.setDisplayMode("Description")
phyptaRXPriorityLevel.setDescription("PHY PTA RX Priority Level")


global phyptaEDPriority
phyptaEDPriority = ieee802154phy.createBooleanSymbol("PHY_PTA_ED_PRIORITY",phyptaPriorityConfig)
phyptaEDPriority.setLabel("ED Priority")
phyptaEDPriority.setDefaultValue(False)

global phyptaDebugConfig
phyptaDebugConfig = ieee802154phy.createBooleanSymbol("PHY_PTA_DEBUG_CONFIG_ENABLE",phyMenupta)
phyptaDebugConfig.setLabel("Debug Info")
phyptaDebugConfig.setDefaultValue(False)
phyptaDebugConfig.setVisible(False)
                                         

# === File templates processing
global phypalptaInterfaceHeaderFile
phypalptaInterfaceHeaderFile = ieee802154phy.createFileSymbol("PHY_PAL_PTA_INTERFACE_HEADER_FILE", None)
phypalptaInterfaceHeaderFile.setSourcePath("/driver/templates/pal_pta_interface.h.ftl")
phypalptaInterfaceHeaderFile.setOutputName("pal_pta_interface.h")
phypalptaInterfaceHeaderFile.setDestPath("driver/IEEE_802154_PHY/pal/inc")
phypalptaInterfaceHeaderFile.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/pal/inc")
phypalptaInterfaceHeaderFile.setType("HEADER")
phypalptaInterfaceHeaderFile.setOverwrite(True)
phypalptaInterfaceHeaderFile.setMarkup(True)
phypalptaInterfaceHeaderFile.setEnabled(True)

global phypalptaInterfaceSourceFile
phypalptaInterfaceSourceFile = ieee802154phy.createFileSymbol("PHY_PAL_PTA_INTERFACE_SOURCE_FILE", None)
phypalptaInterfaceSourceFile.setSourcePath("/driver/templates/pal_pta_interface.c.ftl")
phypalptaInterfaceSourceFile.setOutputName("pal_pta_interface.c")
phypalptaInterfaceSourceFile.setDestPath("driver/IEEE_802154_PHY/pal/src")
phypalptaInterfaceSourceFile.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/pal/src")
phypalptaInterfaceSourceFile.setType("SOURCE")
phypalptaInterfaceSourceFile.setOverwrite(True)
phypalptaInterfaceSourceFile.setMarkup(True)
phypalptaInterfaceSourceFile.setEnabled(False)


global phypalptaApiHeaderFile
phypalptaApiHeaderFile = ieee802154phy.createFileSymbol("PHY_PAL_PTA_API_HEADER_FILE", None)
phypalptaApiHeaderFile.setSourcePath("/driver/templates/pal_pta_api.h.ftl")
phypalptaApiHeaderFile.setOutputName("pal_pta_api.h")
phypalptaApiHeaderFile.setDestPath("driver/IEEE_802154_PHY/pal/inc")
phypalptaApiHeaderFile.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/pal/inc")
phypalptaApiHeaderFile.setType("HEADER")
phypalptaApiHeaderFile.setOverwrite(True)
phypalptaApiHeaderFile.setMarkup(True)
phypalptaApiHeaderFile.setEnabled(True)

global phypalptaApiSourceFile
phypalptaApiSourceFile = ieee802154phy.createFileSymbol("PHY_PAL_PTA_API_SOURCE_FILE", None)
phypalptaApiSourceFile.setSourcePath("/driver/templates/pal_pta_api.c.ftl")
phypalptaApiSourceFile.setOutputName("pal_pta_api.c")
phypalptaApiSourceFile.setDestPath("driver/IEEE_802154_PHY/pal/src")
phypalptaApiSourceFile.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/pal/src")
phypalptaApiSourceFile.setType("SOURCE")
phypalptaApiSourceFile.setOverwrite(True)
phypalptaApiSourceFile.setMarkup(True)
phypalptaApiSourceFile.setEnabled(False)


