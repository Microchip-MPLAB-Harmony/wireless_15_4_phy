# coding: utf-8
##############################################################################
# Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ IEEE 802.15.4 PHY CONFIGURATIONS ~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMPONENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-------------------------------------------------------------------------------
pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                      'PIC32CX1012BZ25032',
                      'PIC32CX1012BZ24032',
                      'WBZ451',
                      'WBZ450',
                      'WBZ451H'
                      }
                      
pic32cx_bz2_hpa_family = {
                      'WBZ451H'
                      }
                      
global customTxMaxFHSSVal1
global customGainValue1
customTxMaxFHSSVal1 = 14
customGainValue1 = 2

global deviceName
deviceName = Variables.get("__PROCESSOR")


def instantiateComponent(ieee802154phy):
    print("IEEE 802.15.4 PHY Standalone library driver component")
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    # === Activate required components automatically
    global requiredComponents
    if (deviceName in pic32cx_bz2_family):
          requiredComponents = [
              "HarmonyCore",
              "sys_time",
              "RTOS",
              "trng"
          ]
    
    conditionAlwaysInclude = [True, None, []]
    
    global phyConstLargeBufferSize
    phyConstLargeBufferSize = 144
    global phyConstSmallBufferSize
    phyConstSmallBufferSize = 48
    
    res = Database.activateComponents(requiredComponents)
    
    Database.setSymbolValue("core", "ZIGBEE_CLOCK_ENABLE", True)

    # === Interfaces

    # === PHY RTOS Configuration
    phyRtosConfig = ieee802154phy.createMenuSymbol("PHY_RTOS_CONFIG", None)
    phyRtosConfig.setLabel("PHY RTOS Configuration")
    phyRtosConfig.setVisible(True)

    # === Create PHY RTOS Task
    createPhyRtosTask = ieee802154phy.createBooleanSymbol('CREATE_PHY_RTOS_TASK', phyRtosConfig)
    createPhyRtosTask.setLabel('Create PHY RTOS Task')
    createPhyRtosTask.setDefaultValue(True)
    
    # === Create PHY Semaphore
    createPhySemaphore = ieee802154phy.createBooleanSymbol('CREATE_PHY_SEMAPHORE', phyRtosConfig)
    createPhySemaphore.setLabel('Create PHY Semaphore')
    createPhySemaphore.setVisible(False)
    createPhySemaphore.setDefaultValue(True)

    # === PHY RTOS Priority Configuration
    global phyRtosTaskPriority
    phyRtosTaskPriority = ieee802154phy.createIntegerSymbol('PHY_TASK_PRIORITY', phyRtosConfig)
    phyRtosTaskPriority.setLabel('PHY RTOS Task Priority')
    phyRtosTaskPriority.setMin(1)
    phyRtosTaskPriority.setMax(5)
    phyRtosTaskPriority.setDefaultValue(1)
    
    # Custom Antenna Gain Enabled
    customAntennaSpecified = ieee802154phy.createBooleanSymbol('USE_CUSTOM_ANT_GAIN', None)
    customAntennaSpecified.setVisible(False)
    customAntennaSpecified.setReadOnly(True)
    customAntennaSpecified.setValue(False)

    # PIC32CX_BZ2 
    global BZ2Symbol
    BZ2Symbol = ieee802154phy.createBooleanSymbol("PIC32CXBZ2", None)
    BZ2Symbol.setDefaultValue(False)
    BZ2Symbol.setVisible(False)
    
    global BZ2HPASymbol
    BZ2HPASymbol = ieee802154phy.createBooleanSymbol("PIC32CXBZ2_HPA", None)
    BZ2HPASymbol.setDefaultValue(False)
    BZ2HPASymbol.setVisible(False)

    if (deviceName in pic32cx_bz2_family):
        BZ2Symbol.setDefaultValue(True)
    if (deviceName in pic32cx_bz2_hpa_family):
        BZ2HPASymbol.setDefaultValue(True)

    # Custom Antenna Gain
    global customAntennaGain
    customAntennaGain = ieee802154phy.createIntegerSymbol('CUSTOM_ANT_GAIN', None)
    customAntennaGain.setVisible(False)
    customAntennaGain.setReadOnly(True)
    if(deviceName == 'WBZ450'):
        customAntennaGain.setValue(5)
    elif(deviceName == 'WBZ451H'):
        customAntennaGain.setValue(4)
    else:
        customAntennaGain.setValue(3)
        
    customAntennaGain.setDependencies(powerRegionCheck, ["CUSTOM_ANT_GAIN"])
        
    # Custom tx power max
    global customTxMaxFHSSVal
    customTxMaxFHSSVal = ieee802154phy.createIntegerSymbol('TX_PWR_MAX_NON_FHSS', None)
    customTxMaxFHSSVal.setVisible(False)
    customTxMaxFHSSVal.setReadOnly(True)
    customTxMaxFHSSVal.setValue(customTxMaxFHSSVal1)
    
    global phyTxPwrConfig
    phyTxPwrConfig = ieee802154phy.createMenuSymbol("PHY_TX_POWER_CONFIG", None)
    phyTxPwrConfig.setLabel("PHY Tx Power Configuration")
    phyTxPwrConfig.setVisible(False)
    
    # Power Channel 
    global  appPowerRegion
    appPowerRegion = ieee802154phy.createIntegerSymbol("APP_TX_POWER", phyTxPwrConfig)
    appPowerRegion.setLabel("Tx Power Set")
    if (deviceName == "PIC32CX1012BZ25048"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-11)
        appPowerRegion.setMax(15)
    elif(deviceName == "PIC32CX1012BZ25032"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-11)
        appPowerRegion.setMax(6)
    elif (deviceName == "PIC32CX1012BZ24032"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-16)
        appPowerRegion.setMax(6)
    elif(deviceName == "WBZ451"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-11)
        appPowerRegion.setMax(15)
    elif(deviceName == "WBZ451H"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-26)
        appPowerRegion.setMax(20)
    elif(deviceName == "WBZ450"):
        appPowerRegion.setDefaultValue(3)
        appPowerRegion.setMin(-11)
        appPowerRegion.setMax(6)
    else:
        appPowerRegion.setDefaultValue(5)
     
    appPowerRegion.setDependencies(powerRegionCheck, ["TX_PWR_MAX_NON_FHSS"])
    appPowerRegion.setDefaultValue(appPowerRegion.getMax())
    
    # === Radio menu
    execfile(Module.getPath() + "/driver/config/drv_ieee802154_phy_bmm.py")
    
    # === Header Files
    
    includePal = [
        ["pal/inc/pal.h", conditionAlwaysInclude],
    ]
    includeResources = [
        ["resources/buffer/inc/bmm.h", conditionAlwaysInclude],
        ["resources/queue/inc/qmm.h", conditionAlwaysInclude],
    ]
    includePhy = [
        ["phy/inc/phy_tasks.h", conditionAlwaysInclude],
        ["phy/inc/phy_constants.h", conditionAlwaysInclude],
        ["phy/inc/ieee_phy_const.h", conditionAlwaysInclude]

    ]


    # === Import the header files
    for incFileEntry in includePal:
        importIncFile(ieee802154phy, configName, incFileEntry)
    for incFileEntry in includeResources:
        importIncFile(ieee802154phy, configName, incFileEntry)
    for incFileEntry in includePhy:
        importIncFile(ieee802154phy, configName, incFileEntry)

    # === Source files
    srcResources = [
        ["resources/buffer/src/bmm.c", conditionAlwaysInclude],
        ["resources/queue/src/qmm.c", conditionAlwaysInclude]
    ]
    srcPhy = [
        ["phy/src/phy_task.c", conditionAlwaysInclude],
        ["phy/src/phy_ed_end_cb.c", conditionAlwaysInclude],
        ["phy/src/phy_rx_frame_cb.c", conditionAlwaysInclude],
        ["phy/src/phy_tx_frame_done_cb.c", conditionAlwaysInclude],
    ]

    # === Import the source files
    for srcFileEntry in srcResources:
        importSrcFile(ieee802154phy, configName, srcFileEntry)
    for srcFileEntry in srcPhy:
        importSrcFile(ieee802154phy, configName, srcFileEntry)

    # === Include path setting
    includePathsPhy = [
        ["/IEEE_802154_PHY/pal/inc", conditionAlwaysInclude],
        ["/IEEE_802154_PHY/phy/inc/", conditionAlwaysInclude],
        ["/IEEE_802154_PHY/resources/buffer/inc/", conditionAlwaysInclude],
        ["/IEEE_802154_PHY/resources/queue/inc/", conditionAlwaysInclude],
    ]
    for incPathEntry in includePathsPhy:
        setIncPath(ieee802154phy, configName, incPathEntry)

    # === Compiler macros
    preprocessorCompiler = ieee802154phy.createSettingSymbol("IEEE802154PHY_XC32_PREPRECESSOR", None)
    preprocessorCompiler.setValue("ENABLE_LARGE_BUFFER;ENABLE_QUEUE_CAPACITY")
    preprocessorCompiler.setCategory("C32")
    preprocessorCompiler.setKey("preprocessor-macros")
    preprocessorCompiler.setAppend(True, ";")
    preprocessorCompiler.setEnabled(True)

    # === File templates processing
    phyConfHeader = ieee802154phy.createFileSymbol("PHY_CONF_HEADER", None)
    phyConfHeader.setSourcePath("/driver/templates/stack_config.h.ftl")
    phyConfHeader.setOutputName("stack_config.h")
    phyConfHeader.setDestPath('../../')
    phyConfHeader.setProjectPath('')
    phyConfHeader.setType("HEADER")
    phyConfHeader.setOverwrite(True)
    phyConfHeader.setMarkup(True)
    
    phyConfHeader = ieee802154phy.createFileSymbol("APP_CONF_HEADER", None)
    phyConfHeader.setSourcePath("/driver/templates/app_config.h.ftl")
    phyConfHeader.setOutputName("app_config.h")
    phyConfHeader.setDestPath('../../')
    phyConfHeader.setProjectPath('')
    phyConfHeader.setType("HEADER")
    phyConfHeader.setOverwrite(True)
    phyConfHeader.setMarkup(True)
    
    phyApiHeader = ieee802154phy.createFileSymbol("PHY_HEADER", None)
    phyApiHeader.setSourcePath("/driver/templates/phy.h.ftl")
    phyApiHeader.setOutputName("phy.h")
    phyApiHeader.setDestPath("driver/IEEE_802154_PHY/phy/inc")
    phyApiHeader.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/phy/inc")
    phyApiHeader.setType("HEADER")
    phyApiHeader.setOverwrite(True)
    phyApiHeader.setMarkup(True)
    
    palSource = ieee802154phy.createFileSymbol("PAL_SOURCE", None)
    palSource.setSourcePath("/driver/templates/pal.c.ftl")
    palSource.setOutputName("pal.c")
    palSource.setDestPath("driver/IEEE_802154_PHY/pal/src")
    palSource.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/pal/src")
    palSource.setType("SOURCE")
    palSource.setOverwrite(True)
    palSource.setMarkup(True)

    phyDefinitionsH = ieee802154phy.createFileSymbol('IEEE802154PHY_DEFINITIONS_H', None)
    phyDefinitionsH.setType('STRING')
    phyDefinitionsH.setOutputName('core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES')
    phyDefinitionsH.setSourcePath('driver/templates/system/system_definitions.h.ftl')
    phyDefinitionsH.setMarkup(True)
    
    phyInitC = ieee802154phy.createFileSymbol('IEEE802154PHY_INITIALIZATION_C', None)
    phyInitC.setType('STRING')
    phyInitC.setOutputName('core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE')
    phyInitC.setSourcePath('driver/templates/system/system_initialize_middleware.c.ftl')
    phyInitC.setMarkup(True)
    
    phyTasksC = ieee802154phy.createFileSymbol('IEEE802154PHY_TASKS_C', None)
    phyTasksC.setType('STRING')
    phyTasksC.setOutputName('core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS')
    phyTasksC.setSourcePath('driver/templates/system/system_tasks.c.ftl')
    phyTasksC.setMarkup(True)
    
    phyInitDataC = ieee802154phy.createFileSymbol('IEEE802154PHY_INITIALIZATION_DATA_C', None)
    phyInitDataC.setType('STRING')
    phyInitDataC.setOutputName('core.LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA')
    phyInitDataC.setSourcePath('driver/templates/system/system_initialize_data.c.ftl')
    phyInitDataC.setMarkup(True)
    
    phyTasksDefC = ieee802154phy.createFileSymbol('IEEE802154PHY_TASK_INITIALIZATION_C', None)
    phyTasksDefC.setType('STRING')
    phyTasksDefC.setOutputName('core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS')
    phyTasksDefC.setSourcePath('driver/templates/system/system_tasks_def.c.ftl')
    phyTasksDefC.setMarkup(True)
    

    # === Setting the required heap size for the application
    Database.sendMessage("core", "HEAP_SIZE", {"heap_size":1024})

    # === Treat warnings as errors
    phyWarnAsErr = ieee802154phy.createSettingSymbol("IEEE802154PHY_GCC_WARN_ERROR", None)
    phyWarnAsErr.setValue("false")
    phyWarnAsErr.setCategory("C32")
    phyWarnAsErr.setKey("make-warnings-into-errors")

    # === Set optimization level
    phyOptLevel = ieee802154phy.createSettingSymbol("PET_LEVEL", None)
    phyOptLevel.setValue("-O2")
    phyOptLevel.setCategory("C32")
    phyOptLevel.setKey("optimization-level")

    # === Library
    libIeee802154Phy = ieee802154phy.createLibrarySymbol("IEEE802154PHY_LIB_FILE", None)
    libIeee802154Phy.setDestPath("/driver/lib")
    if (deviceName in pic32cx_bz2_family):
          libIeee802154Phy.setSourcePath("/driver/software/phy/pic32cx_bz/lib/lib-ieee802154_phy_pic32cxbz-v1.2.0.a")
          libIeee802154Phy.setOutputName("lib-ieee802154_phy_pic32cxbz-v1.2.0.a")
#end instantiateComponent

def finalizeComponent(ieee802154phy):
    ###########################################################################
    ## Auto Activate and Dependent components
    ###########################################################################
    if (deviceName in pic32cx_bz2_family):
      activeComponents = Database.getActiveComponentIDs()
      
      requiredComponents = ["pic32cx_bz2_devsupport"]
      for r in requiredComponents:
          if r in activeComponents:
              print("require component '{}' - de-activating it".format(r))
              res = Database.deactivateComponents([r])

      activeComponents = Database.getActiveComponentIDs()
      
      requiredComponents = ["pic32cx_bz2_devsupport"]
      for r in requiredComponents:
          if r not in activeComponents:
              print("require component '{}' - activating it".format(r))
              res = Database.activateComponents([r])
      
    print("Finalized Componenet Deactivation / activation Process - completed **********************")
    
#end finalizeComponent

#
# Dependency functions
#
def powerRegionCheck(symbol, event):

    # symbol.setVisible(True)

    minBoundaries = 0
    if(deviceName == "WBZ451"):
        minBoundaries  = -14
    elif(deviceName == "WBZ450"):
        minBoundaries  = -16
    elif(deviceName in pic32cx_bz2_hpa_family):
        minBoundaries  = -26
    
    customGainValue1 = customAntennaGain.getValue()
    TxMinPwr =  minBoundaries + customGainValue1
    appPowerRegion.setMin(TxMinPwr)
    customTxMaxFHSSVal2 = customTxMaxFHSSVal.getValue()
    appPowerRegion.setMax(customTxMaxFHSSVal2)
    

#end powerRegionCheck

def handleMessage(messageID, args):
    # Log.writeInfoMessage('drv_ieee802154_phy:handleMessage ID={} argLen={}'.format(messageID, len(args)))
    ''' This message handler is designed to process messages
        sent from the driver/pic32cx-bz/config/device_support.py
        script.
    '''
    if(messageID == 'ANTENNA_GAIN_CHANGE'):
        component = Database.getComponentByID(args['target'])
        if (component):
            customGainEnabled = component.getSymbolByID('USE_CUSTOM_ANT_GAIN')
            customAntennaGain = component.getSymbolByID('CUSTOM_ANT_GAIN')
            customTxMaxFHSSVal = component.getSymbolByID('TX_PWR_MAX_NON_FHSS')
            
            Log.writeInfoMessage('{:<17}: Handling - target={}'.format('drv_ieee802154_phy.py', args['target']))
            for arg in args:
                Log.writeInfoMessage('{:<17}: {}: {}'.format('', arg, args[arg]))
                if('CUSTOM_ANT_ENABLE' == arg):
                    customGainEnabled.setValue(args[arg])
                if('CUSTOM_ANT_GAIN' == arg):
                    customAntennaGain.setValue(args[arg])
                if('TX_PWR_MAX_NON_FHSS' == arg):
                    customTxMaxFHSSVal.setValue(args[arg])

#end handleMessage       

def phyCommentBmmLargeBuffersDepend(sourceSymbol, event):
    totalMem = phyConstLargeBufferSize * phyIntegerBmmLargeBuffers.getValue()
    phyCommentBmmLargeBuffers.setLabel("Memory occupied: ~%d bytes" %totalMem)
#end phyCommentBmmLargeBuffersDepend

def phyCommentBmmSmallBuffersDepend(sourceSymbol, event):
    totalMem = phyConstSmallBufferSize * phyIntegerBmmSmallBuffers.getValue()
    phyCommentBmmSmallBuffers.setLabel("Memory occupied: ~%d bytes" %totalMem)
#end phyCommentBmmSmallBuffersDepend             

def importIncFile(component, configName, incFileEntry, firmwarePath = None):
    incFilePath  = incFileEntry[0]
    isEnabled    = incFileEntry[1][0]
    callback     = incFileEntry[1][1]
    dependencies = incFileEntry[1][2]

    incFilePathTup = incFilePath.rsplit("/", 1)

    if len(incFilePathTup) == 1:
        secName = ""
        incFile = incFilePathTup[0]
    else :
        secName = incFilePathTup[0]
        incFile = incFilePathTup[1]

    symName = incFile.replace(".", "_").upper()
    secSName = secName + "/"
    secDName = secSName
    print("importIncFile: ", secDName)

    incFileSym = component.createFileSymbol(symName, None)
    incFileSym.setSourcePath("driver/software/" + secSName + "/" + incFile)
    incFileSym.setOutputName(incFile)
    incFileSym.setDestPath("driver/IEEE_802154_PHY/" + secDName + "")
    incFileSym.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/"+ secDName + "")
    incFileSym.setType("HEADER")
    incFileSym.setOverwrite(True)
    incFileSym.setEnabled(isEnabled)

    if callback and dependencies:
        incFileSym.setDependencies(callback, dependencies)
#end importIncFile

def importSrcFile(component, configName, srcFileEntry, firmwarePath = None):
    srcFilePath  = srcFileEntry[0]
    isEnabled    = srcFileEntry[1][0]
    callback     = srcFileEntry[1][1]
    dependencies = srcFileEntry[1][2]

    srcFilePathTup = srcFilePath.rsplit("/", 1)

    if len(srcFilePathTup) == 1:
        secName = ""
        srcFile = srcFilePathTup[0]
    else:
        secName = srcFilePathTup[0]
        srcFile = srcFilePathTup[1]

    srcFilePrefix   = ""
    symName = srcFile.replace(".", "_").upper()
    secSName = secName + "/"
    secDName = secSName
    print("******", secDName)

    srcFileSym = component.createFileSymbol(symName, None)
    srcFileSym.setSourcePath("driver/software/" + secSName + srcFile)
    srcFileSym.setOutputName(srcFile.rsplit("/", 1)[-1])
    srcFileSym.setDestPath("driver/IEEE_802154_PHY/" + secDName + "")
    srcFileSym.setProjectPath("config/" + configName + "/driver/IEEE_802154_PHY/"+ secDName + "")
    srcFileSym.setType("SOURCE")
    srcFileSym.setEnabled(isEnabled)

    if callback and dependencies:
        srcFileSym.setDependencies(callback, dependencies)
#end importSrcFile

def setIncPath(component, configName, incPathEntry):
    incPath      = incPathEntry[0]
    isEnabled    = incPathEntry[1][0]
    callback     = incPathEntry[1][1]
    dependencies = incPathEntry[1][2]
    incPathSym = component.createSettingSymbol("IEEE802154PHY_INC_PATH" + incPath.replace(".", "_").replace("/", "_").upper(), None)
    incPathSym.setValue("../src/config/" + configName + "/driver/" + incPath + ";")
    incPathSym.setCategory("C32")
    incPathSym.setKey("extra-include-directories")
    incPathSym.setAppend(True, ";")
    incPathSym.setEnabled(isEnabled)
    incPathSym.setDependencies(callback, dependencies)
    
    incPathSymCpp = component.createSettingSymbol("IEEE802154PHY_INC_PATH_CPP" + incPath.replace(".", "_").replace("/", "_").upper(), None)
    incPathSymCpp.setValue("../src/config/" + configName + "/driver/" + incPath + ";")
    incPathSymCpp.setCategory("C32CPP")
    incPathSymCpp.setKey("extra-include-directories")
    incPathSymCpp.setAppend(True, ";")
    incPathSymCpp.setEnabled(isEnabled)
    incPathSymCpp.setDependencies(callback, dependencies)
#end setIncPath

def onAttachmentConnected(source, target):
    if (deviceName in pic32cx_bz2_family):
         remoteComponent = Database.getComponentByID("trng")
         if (remoteComponent):
               print('Printing TRNG remoteComponent Value')
               remoteComponent.getSymbolByID("trngEnableInterrupt").setReadOnly(True)
               remoteComponent.getSymbolByID("trngEnableEvent").setReadOnly(True)
               remoteComponent.getSymbolByID("TRNG_STANDBY").setReadOnly(True)  

def destroyComponent(ieee802154phy):
    for component in requiredComponents:
         Database.deactivateComponents([component])
