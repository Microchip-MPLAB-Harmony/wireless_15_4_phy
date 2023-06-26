<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
<#if CREATE_PHY_RTOS_TASK == true>
/* Handle for the APP_Tasks. */
TaskHandle_t xPHY_Tasks;

void _PHY_Tasks(  void *pvParameters  )
{     
    while(1)
    {
        PHY_Tasks();
    }
}

</#if>
</#if>


