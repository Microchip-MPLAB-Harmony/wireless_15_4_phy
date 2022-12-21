<#if HarmonyCore.SELECT_RTOS == "BareMetal">
    /* Call the IEEE_802154_PHY Task Handler function */
	PHY_TaskHandler();
<#else>
<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
    /* Create FreeRTOS task for IEEE_802154_PHY */
	 xTaskCreate((TaskFunction_t) _PHY_Tasks,
                "PHY_Tasks",
                1024,
                NULL,
                1,
                &xPHY_Tasks);
</#if>
</#if>
