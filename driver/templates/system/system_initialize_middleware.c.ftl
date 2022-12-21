    /* Initialization for IEEE_802154_PHY */
	OSAL_SEM_Create(&semPhyInternalHandler, OSAL_SEM_TYPE_COUNTING, 20, 0);
	
	PHY_Init();
    
    /* End of Initialization for IEEE_802154_PHY */
