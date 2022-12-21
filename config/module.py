######################  Harmony replaceme  ######################
def loadModule():
    print("Load Module: Harmony IEEE 802.15.4 PHY Standalone Library")    
    ieee802154phy  = Module.CreateComponent('IEEE_802154_PHY', 'IEEE 802.15.4 PHY', 'Wireless/Drivers', 'driver/config/drv_ieee802154_phy.py')
    ieee802154phy.setDisplayType('Standalone PHY Driver')
    ieee802154phy.addDependency('HarmonyCoreDependency', 'Core Service', 'Core', True, True)
    ieee802154phy.addDependency('SysTimeDependency', 'SYS_TIME', 'SYS_TIME', True, True)
    ieee802154phy.addDependency('FreeRtosDependency', 'RTOS', 'RTOS', True, True)
    print("***** CPU: ", Variables.get("__PROCESSOR"))
    if ("WBZ" in Variables.get("__PROCESSOR")) or ("PIC32CX" in Variables.get("__PROCESSOR")):
        ieee802154phy.addDependency('DeviceSupportDependency', 'Device_Support', 'Device_Support', True, True)
