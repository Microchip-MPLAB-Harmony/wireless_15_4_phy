######################  Harmony replaceme  ######################
def loadModule():
    print("Load Module: Harmony IEEE 802.15.4 PHY Standalone Library")

    pic32cx_bz2_family = {'PIC32CX1012BZ25048',
                          'PIC32CX1012BZ25032',
                          'PIC32CX1012BZ24032',
                          'WBZ451',
                          'WBZ450',
                          } 
                          
    processor = Variables.get('__PROCESSOR') 
    
    print('processor={}'.format(processor))
                          
    if (processor in pic32cx_bz2_family):                      
        ieee802154phy  = Module.CreateComponent('IEEE_802154_PHY', 'IEEE 802.15.4 PHY', 'Wireless/Drivers', 'driver/config/drv_ieee802154_phy.py')
        ieee802154phy.setDisplayType('Standalone PHY Driver')
        ieee802154phy.addDependency('HarmonyCoreDependency', 'Core Service', 'Core', True, True)
        ieee802154phy.addDependency('SysTimeDependency', 'SYS_TIME', 'SYS_TIME', True, True)
        ieee802154phy.addDependency('FreeRtosDependency', 'RTOS', 'RTOS', True, True)
        ieee802154phy.addDependency('DeviceSupportDependency', 'Device_Support', 'Device_Support', True, True)

        
