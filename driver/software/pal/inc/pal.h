/*******************************************************************************
  PAL Header

  File Name:
    pal.h

  Summary:
    This file contains Platform Abstraction Layer API function declarations

  Description:
    PAL Layer provides the interface to Timers, Interrupts and other platform 
    related resources. PHY layer is using PAL for its internal operations
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

/* Prevent double inclusion */
#ifndef PAL_H
#define PAL_H

/**
 * This module acts as a wrapper layer between the Wireless stack and the Harmony
 * drivers and peripherals
 * All hardware level access to the Harmony drivers from the stack happens through
 * this module 
 */
// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************
#include "definitions.h"

// *****************************************************************************
// *****************************************************************************
// Section: Macros
// *****************************************************************************
// *****************************************************************************
/**
 * Adds two time values
 */
#define ADD_TIME(a, b)                  ((a) + (b))

/**
 * Subtracts two time values
 */
#define SUB_TIME(a, b)                  ((a) - (b))

/* Wait for 65 ns. */
#define PAL_WAIT_65_NS()                {__NOP(); __NOP();}

/* Enables the global interrupt */
#define ENABLE_GLOBAL_IRQ()                  NVIC_INT_Enable();

/* Disables the global interrupt */
#define DISABLE_GLOBAL_IRQ()                 NVIC_INT_Disable();

/* This macro saves the global interrupt status */
#define ENTER_CRITICAL_REGION()              {bool flags = NVIC_INT_Disable();

/* This macro restores the global interrupt status */
#define LEAVE_CRITICAL_REGION()              NVIC_INT_Restore(flags); }

/* This macro defines the CPU clock frequency */
#define PAL_CPU_CLOCK_FREQUENCY               CPU_CLOCK_FREQUENCY           

// *****************************************************************************
// *****************************************************************************
// Section: Types
// *****************************************************************************
// *****************************************************************************
/**
 * PAL Timer Timeout type
 */
typedef enum timeout_type_tag {
	/** The timeout is relative to the current time. */
	TIMEOUT_RELATIVE,
	/** The timeout is an absolute value. */
	TIMEOUT_ABSOLUTE
}  TimeoutType_t;

/**
 * PAL Timer Callback type
 */
typedef enum callback_type_tag {
	/** Single Shot timer. */
	CALLBACK_SINGLE,
	/** Periodic Timer. */
    CALLBACK_PERIODIC
}  CallbackType_t;

/**
 * PAL Timer Id type
 */
typedef uint8_t TimerId_t;

/**
 * PAL Return status types
 */
typedef enum pal_status_tag {
	PAL_SUCCESS                 = 0x00,
    PAL_TMR_ALREADY_RUNNING     = 0x10, /**< Timer is already running */
	PAL_TMR_NOT_RUNNING         = 0x11, /**< Timer is not running */
	PAL_TMR_INVALID_ID          = 0x12, /**< Invalid timer ID*/
	PAL_TMR_INVALID_TIMEOUT     = 0x13, /**< Requested Timeout is out of
	                                     * range or too short */
    PAL_FAILURE                 = 0x14,
} PAL_Status_t;


// *****************************************************************************
// *****************************************************************************
// Section: Externals
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: Function Prototypes
// *****************************************************************************
// *****************************************************************************

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Initialization of PAL
 *
 * This function initializes the PAL. .
 *
 * @return PAL_SUCCESS  if PAL initialization is successful, PAL_FAILURE otherwise
 */
PAL_Status_t PAL_Init(void);

/**
 * @brief Start regular timer
 *
 * This function starts a regular timer and installs the corresponding
 * callback function handle the timeout event.
 *
 * @param timer_id Timer identifier
 * @param timer_count Timeout in microseconds
 * @param timeout_type @ref TIMEOUT_RELATIVE or @ref TIMEOUT_ABSOLUTE
 * @param timer_cb Callback handler invoked upon timer expiry
 * @param param_cb Argument for the callback handler
 * @param callback_type @ref CALLBACK_SINGLE or @ref CALLBACK_PERIODIC
 *
 * @return
 *          - @ref PAL_TMR_INVALID_ID  if the timer identifier is undefined,
 *          - @ref PAL_INVALID_PARAMETER if the callback function for this timer
 *                 is NULL,
 *          - @ref PAL_TMR_ALREADY_RUNNING if the timer is already running.
 *          - @ref PAL_SUCCESS if timer is started or
 *          - @ref PAL_TMR_INVALID_TIMEOUT if timeout is not within timeout
 * range.
 */
PAL_Status_t PAL_TimerStart(TimerId_t timerId,
		uint32_t timerCount,
		TimeoutType_t timeoutType,
		void * timerCb,
		void *paramCb, 
        CallbackType_t callbackType);

/**
 * @brief Stops a running timer
 *
 * This function stops a running timer with specified timer_id
 *
 * @param timer_id Timer identifier
 *
 * @return
 *          - @ref PAL_SUCCESS if timer stopped successfully,
 *          - @ref PAL_TMR_INVALID_ID if the specifed timer id is undefined.
 */
PAL_Status_t PAL_TimerStop(TimerId_t timerId);


/**
 * @brief Gets current time
 *
 * This function returns the current time.
 *
 * @param[out] current_time Returns current system time
 */
void PAL_GetCurrentTime(uint32_t *currentTime);

/**
 * @brief Returns a timer id to be used before starting a timer
 * @param timer_id Value of the id returned by the function
 */
PAL_Status_t PAL_TimerGetId(TimerId_t *timer_id);

/**
 * @brief Checks if the timer of requested timer identifier is running
 *
 * This function checks if the timer of requested timer identifier is running.
 *
 * @param timer_id Timer identifier
 *
 * @return
 * - true if timer with requested timer id is running,
 * - false otherwise.
 */
bool PAL_TimerIsRunning(TimerId_t timer_id);

/**
 * @brief This function is used to create the blocking delay in us
 * @param delay Delay value in Microseconds
 */
void PAL_TimerDelay(uint32_t delay);

/**
 * @brief Adds two time values
 *
 * @param a Time value 1
 * @param b Time value 2
 *
 * @return Addition of a and b
 */
static inline uint32_t pal_add_time_us(uint32_t a, uint32_t b)
{
	return (ADD_TIME(a, b));
}

/**
 * @brief Subtracts two time values
 *
 * @param a Time value 1
 * @param b Time value 2
 *
 * @return Difference between a and b
 */
static inline uint32_t pal_sub_time_us(uint32_t a, uint32_t b)
{
	return (SUB_TIME(a, b));
}

/**
 * \brief Enables the transceiver main interrupt
 *
 * This macro is only available for non-single chip transceivers, since
 * in single chip transceivers there is no separation between enabling
 * transceiver interrupts at the transceiver, and setting the IRQ mask
 * at the MCU. Therefore the transceiver interrupts in single chips are
 * enabled by setting the MCU IRQ mask.
 *
 */
#define pal_trx_irq_en()                NVIC_DisableIRQ((IRQn_Type)ZB_INT0_IRQn);\
                                        NVIC_SetPriority((IRQn_Type) ZB_INT0_IRQn, 1);\
                                        NVIC_ClearPendingIRQ((IRQn_Type) ZB_INT0_IRQn);\
                                        NVIC_EnableIRQ((IRQn_Type) ZB_INT0_IRQn);

/**
 * \brief Disables the transceiver main interrupt
 *
 * This macro is only available for non-single chip transceivers, since
 * in single chip transceivers there is no separation between disabling
 * transceiver interrupts at the transceiver, and clearing the IRQ mask
 * at the MCU. Therefore the transceiver interrupts in single chips are
 * disabled by clearing the MCU IRQ mask.
 *
 */
#define pal_trx_irq_dis()               NVIC_DisableIRQ((IRQn_Type) ZB_INT0_IRQn);

/**
 * @brief Enables the global interrupt
 */
static inline void pal_global_irq_enable(void)
{
	ENABLE_GLOBAL_IRQ();
}

/**
 * @brief Disables the global interrupt
 */
static inline void pal_global_irq_disable(void)
{
	DISABLE_GLOBAL_IRQ();
}


/* ! @} */
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif  /* PAL_H */
/* EOF */
