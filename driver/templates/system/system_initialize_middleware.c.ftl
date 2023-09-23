    /* Initialization for IEEE_802154_PHY */
    <#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
    <#if CREATE_PHY_SEMAPHORE == true>
    OSAL_SEM_Create(&semPhyInternalHandler, OSAL_SEM_TYPE_COUNTING, 20, 0);
    </#if>
    </#if>

    PHY_Init();
    
    /* End of Initialization for IEEE_802154_PHY */
