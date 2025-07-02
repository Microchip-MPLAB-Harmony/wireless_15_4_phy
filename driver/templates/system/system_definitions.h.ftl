#include "driver/IEEE_802154_PHY/phy/inc/phy.h"
#include "driver/IEEE_802154_PHY/phy/inc/phy_tasks.h"
<#if PIC32CXBZ3 == true || PIC32CXBZ36 == true>
#include "driver/security/sxsymcrypt/trng_api.h"
#include "driver/security/sxsymcrypt/statuscodes.h"
</#if>
<#if PIC32CXBZ6 == true>
#include "driver/security/cryptosym/trng_api.h"
#include "driver/security/cryptosym/statuscodes.h"
</#if>