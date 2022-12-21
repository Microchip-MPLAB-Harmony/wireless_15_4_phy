/* Handle for the APP_Tasks. */
TaskHandle_t xPHY_Tasks;

void _PHY_Tasks(  void *pvParameters  )
{     
    while(1)
    {
        PHY_Tasks();
    }
}


