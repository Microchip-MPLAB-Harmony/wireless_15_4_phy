# coding: utf-8
##############################################################################
# Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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
def instantiateComponent(ieee802154phy):
    print("IEEE 802.15.4 PHY Standlone library driver component")
    configName = Variables.get("__CONFIGURATION_NAME")
    print configName
    # === Activate required components automatically
    global requiredComponents
    requiredComponents = [
        "HarmonyCore",
        "sys_time",
        "pic32cx_bz2_devsupport",
        "RTOS"
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
    global phyRtosConfig
    phyRtosConfig = ieee802154phy.createMenuSymbol("PHY_RTOS_CONFIG", None)
    phyRtosConfig.setLabel("PHY RTOS Configuration")
    phyRtosConfig.setVisible(True)

    global createPhyRtosTask
    # === Create PHY RTOS Task
    createPhyRtosTask = ieee802154phy.createBooleanSymbol('CREATE_PHY_RTOS_TASK', phyRtosConfig)
    createPhyRtosTask.setLabel('Create PHY RTOS Task')
    createPhyRtosTask.setDefaultValue(True)
    
    global createPhySemaphore
    # === Create PHY Semaphore
    createPhySemaphore = ieee802154phy.createBooleanSymbol('CREATE_PHY_SEMAPHORE', phyRtosConfig)
    createPhySemaphore.setLabel('Create PHY Semaphore')
    createPhySemaphore.setVisible(False)
    createPhySemaphore.setDefaultValue(True)

    
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
        ["phy/inc/phy.h", conditionAlwaysInclude],
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
    srcPal = [
        ["pal/src/pal.c", conditionAlwaysInclude]
    ]
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
    for srcFileEntry in srcPal:
        importSrcFile(ieee802154phy, configName, srcFileEntry)
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
    libIeee802154Phy.setDestPath("lib")
    libIeee802154Phy.setSourcePath("/driver/software/phy/pic32cx_bz/lib/lib-ieee802154_phy_pic32cxbz-v1.0.0.a")
    libIeee802154Phy.setOutputName("lib-ieee802154_phy_pic32cxbz-v1.0.0.a")
#end instantiateComponent

def finalizeComponent(ieee802154phy):
    pass
#end finalizeComponent

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
    incFileSym.setDestPath("IEEE_802154_PHY/" + secDName + "")
    incFileSym.setProjectPath("config/" + configName + "/IEEE_802154_PHY/"+ secDName + "")
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
    srcFileSym.setDestPath("IEEE_802154_PHY/" + secDName + "")
    srcFileSym.setProjectPath("config/" + configName + "/IEEE_802154_PHY/"+ secDName + "")
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
    incPathSym.setValue("../src/config/" + configName + incPath + ";")
    incPathSym.setCategory("C32")
    incPathSym.setKey("extra-include-directories")
    incPathSym.setAppend(True, ";")
    incPathSym.setEnabled(isEnabled)
    incPathSym.setDependencies(callback, dependencies)
    
    incPathSymCpp = component.createSettingSymbol("IEEE802154PHY_INC_PATH_CPP" + incPath.replace(".", "_").replace("/", "_").upper(), None)
    incPathSymCpp.setValue("../src/config/" + configName + incPath + ";")
    incPathSymCpp.setCategory("C32CPP")
    incPathSymCpp.setKey("extra-include-directories")
    incPathSymCpp.setAppend(True, ";")
    incPathSymCpp.setEnabled(isEnabled)
    incPathSymCpp.setDependencies(callback, dependencies)
#end setIncPath

#
# Dependency functions
#
def phyCommentBmmLargeBuffersDepend(sourceSymbol, event):
    totalMem = phyConstLargeBufferSize * phyIntegerBmmLargeBuffers.getValue()
    phyCommentBmmLargeBuffers.setLabel("Memory occupied: ~%d bytes" %totalMem)
#end phyCommentBmmLargeBuffersDepend

def phyCommentBmmSmallBuffersDepend(sourceSymbol, event):
    totalMem = phyConstSmallBufferSize * phyIntegerBmmSmallBuffers.getValue()
    phyCommentBmmSmallBuffers.setLabel("Memory occupied: ~%d bytes" %totalMem)
#end phyCommentBmmSmallBuffersDepend

def destroyComponent(ieee802154phy):
    Database.deactivateComponents(requiredComponents)
