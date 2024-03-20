<#if HarmonyCore.SELECT_RTOS == "FreeRTOS">
<#if CREATE_PHY_RTOS_TASK == true>
#define PHY_RTOS_TASK_PRIORITY            ${PHY_TASK_PRIORITY}

/* Handle for the APP_Tasks. */
TaskHandle_t xPHY_Tasks;

static void _PHY_Tasks(  void *pvParameters  )
{     
    while(true)
    {
        PHY_Tasks();
    }
}

</#if>
</#if>


