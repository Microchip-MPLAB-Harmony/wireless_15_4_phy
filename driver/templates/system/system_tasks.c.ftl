<#if HarmonyCore.SELECT_RTOS == "BareMetal">
    /* Call the IEEE_802154_PHY Task Handler function */
    PHY_TaskHandler();
<#else>
<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
<#if CREATE_PHY_RTOS_TASK == true>
    /* Create FreeRTOS task for IEEE_802154_PHY */
     (void)xTaskCreate((TaskFunction_t) _PHY_Tasks,
                "PHY_Tasks",
                512,
                NULL,
                PHY_RTOS_TASK_PRIORITY,
                &xPHY_Tasks);
</#if>
</#if>
</#if>
