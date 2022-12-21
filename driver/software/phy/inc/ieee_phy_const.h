/*******************************************************************************
    IEEE PHY Constants

  File Name:
    ieee_phy_constants.h

  Summary:
    IEEE PHY constants and Attributes definitions
  Description:
    This header holds all IEEE 802.15.4-2015 constants and attribute
    identifiers.

 *******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
//DOM-IGNORE-END

/* Prevent double inclusion */
#ifndef IEEE_PHY_CONST_H
#define IEEE_PHY_CONST_H

/**
 *
 * \defgroup group_inc Common WL Definitions
 * All General Definitions  used by the Wireless Stack applications are defined
 * in this module.
 *
 */

/**
 * \ingroup group_inc
 * \defgroup group_ieee IEEE Constants
 * Includes IEEE Constant Definitions
 * @{
 *
 */

/* === Includes ============================================================= */

/* === Macros =============================================================== */

/**
 * Minimum size of a valid frame other than an Ack frame
 */
#define MIN_FRAME_LENGTH                (8)

/**
 * Maximum size of the management frame(Association Response frame)
 */
#define MAX_MGMT_FRAME_LENGTH           (30)

/* === MAC Constants ======================================================== */

/**
 * Maximum size of PHY packet
 * @ingroup apiMacConst
 */
#define aMaxPHYPacketSize               (127)

/**
 * Maximum turnaround Time of the radio to switch from Rx to Tx or Tx to Rx
 * in symbols
 * @ingroup apiMacConst
 */
#define aTurnaroundTime                 (12)

/* 7.4.1 MAC Layer Constants */
/**
 * The maximum size of an MPDU, in octets, that can be followed by a SIFS
 * period.
 * @ingroup apiMacConst
 */
#define aMaxSIFSFrameSize               (18)

/**
 * The minimum number of octets added by the MAC sublayer to the PSDU.
 * @ingroup apiMacConst
 */
#define aMinMPDUOverhead                 (9)

/**
 * The number of slots contained in any superframe.
 * @ingroup apiMacConst
 */
#define aNumSuperframeSlots             (16)

/**
 * The number of symbols forming the basic time period
 * used by the CSMA-CA algorithm.
 * @ingroup apiMacConst
 */
#define aUnitBackoffPeriod              (20)


/**
 * The number of symbols forming a superframe slot
 * when the superframe order is equal to 0.
 * @ingroup apiMacConst
 */
#define aBaseSlotDuration               (60)

/**
 * The number of symbols forming a superframe when
 * the superframe order is equal to 0.
 * @ingroup apiMacConst
 */
#define aBaseSuperframeDuration         (aBaseSlotDuration * \
	aNumSuperframeSlots)

/* PHY PIB Attributes */

/**
 * @ingroup apiPhyPib
 * @{
 */

/* Standard PIB attributes */

/**
 * The RF channel to use for all following transmissions and receptions.
 */
#define phyCurrentChannel               (0x00)

/**
 * The 5 most significant bits (MSBs) (b27, ..., b31) of phyChannelsSupported
 * shall be reserved and set to 0, and the 27 LSBs (b0, b1, ..., b26) shall
 * indicate the status (1 = available, 0 = unavailable) for each of the 27 valid
 * channels (bk shall indicate the status of channel k).
 */
#define phyChannelsSupported            (0x01)

/**
 * The 2 MSBs represent the tolerance on the transmit power: 00 = 1 dB
 * 01 = 3 dB 10 = 6 dB The 6 LSBs represent a signed integer in
 * twos-complement format, corresponding to the nominal transmit power of the
 * device in decibels relative to 1 mW. The lowest value of phyTransmitPower
 * shall be interpreted as less than or equal to 32 dBm.
 */
#define phyTransmitPower                (0x02)

/**
 * The CCA mode
 *  - CCA Mode 1: Energy above threshold. CCA shall report a busy medium
 * upon detecting any energy above the ED threshold.
 *  - CCA Mode 2: Carrier sense only. CCA shall report a busy medium only upon
 * the detection of a signal with the modulation and spreading characteristics
 * of IEEE 802.15.4. This signal may be above or below the ED threshold.
 *  - CCA Mode 3: Carrier sense with energy above threshold. CCA shall report a
 * busy medium only upon the detection of a signal with the modulation and
 * spreading characteristics of IEEE 802.15.4 with energy above the ED
 * threshold. */
#define phyCCAMode                      (0x03)

/**
 * This is the current PHY channel page. This is used in conjunction with
 * phyCurrentChannel to uniquely identify the channel currently being used.
 */
#define phyCurrentPage                  (0x04)

/**
 * The maximum number of symbols in a frame:
 * = phySHRDuration + ceiling([aMaxPHYPacketSize + 1] x phySymbolsPerOctet)
 */
#define phyMaxFrameDuration             (0x05)

/**
 * The duration of the synchronization header (SHR) in symbols for the current
 * PHY.
 */
#define phySHRDuration                  (0x06)

/**
 * The number of symbols per octet for the current PHY.
 */
#define phySymbolsPerOctet              (0x07)

/**
 * Number of octets added by the PHY: 4 sync octets + SFD octet.
 */
#define PHY_OVERHEAD                    (5)

/*@}*//* apiPhyPib */

/* 7.4.2 MAC PIB Attributes */

/**
 * The maximum number of symbols to wait for an acknowledgment frame to arrive
 * following a transmitted data frame. This value is dependent on the currently
 * selected logical channel. For 0 <= phyCurrentChannel <= 10, this
 * value is equal to 120. For 11 <= phyCurrentChannel <= 26, this  value is
 * equal to 54.
 *
 * - @em Type: Integer
 * - @em Range: 54 or 120
 * - @em Default: 54
 */
#define macAckWaitDuration              (0x40)


/**
 * The maximum number of backoffs the CSMA-CA algorithm will
 * attempt before declaring a channel access failure.
 *
 * - @em Type: Integer
 * - @em Range: 0 - 5
 * - @em Default: 4
 */
#define macMaxCSMABackoffs              (0x4E)

/**
 * Default value for PIB macMaxCSMABackoffs
 */
#define macMaxCSMABackoffs_def          (4)

/**
 * The minimum value of the backoff exponent in the CSMA-CA algorithm.
 * Note that if this value is set to 0, collision avoidance is disabled
 * during the first iteration of the algorithm. Also note that for the
 * slotted version of the CSMACA algorithm with the battery life extension
 * enabled, the minimum value of the backoff exponent will be the lesser of
 * 2 and the value of macMinBE.
 *
 * - @em Type: Integer
 * - @em Range: 0 - 3
 * - @em Default: 3
 */
#define macMinBE                        (0x4F)

/**
 * The 16 bit identifier of the PAN on which the device is operating. If this
 * value is 0xffff, the device is not associated.
 *
 * - @em Type: Integer
 * - @em Range: 0x0000 - 0xffff
 * - @em Default: 0xffff
 */
#define macPANId                        (0x50)

/**
 * Default value for PIB macPANId
 */
#define macPANId_def                    (0xFFFF)

/**
 * This indicates whether the MAC sublayer is in a promiscuous (receive all)
 * mode. A value of true indicates that the MAC sublayer accepts all frames
 * received from the PHY.
 *
 * - @em Type: Boolean
 * - @em Range: true or false
 * - @em Default: false
 */
#define macPromiscuousMode              (0x51)



/**
 * The 16 bit address that the device uses to communicate in the PAN.
 * If the device is a PAN coordinator, this value shall be chosen before a
 * PAN is started. Otherwise, the address is allocated by a coordinator
 * during association. A value of 0xfffe indicates that the device has
 * associated but has not been allocated an address. A value of 0xffff
 * indicates that the device does not have a short address.
 *
 * - @em Type: Integer
 * - @em Range: 0x0000 - 0xffff
 * - @em Default: 0xffff
 */
#define macShortAddress                 (0x53)

/**
 * Default value for PIB macShortAddress
 */
#define macShortAddress_def             (0xFFFF)

/**
 * The maximum value of the backoff exponent, BE, in the CSMA-CA algorithm.
 * See 7.5.1.4 for a detailed explanation of the backoff exponent.
 *
 * - @em Type: Integer
 * - @em Range: 3 - 8
 * - @em Default: 5
 */
#define macMaxBE                        (0x57)


/**
 * The maximum number of retries allowed after a transmission failure.
 *
 * - @em Type: Integer
 * - @em Range: 0 - 7
 * - @em Default: 3
 */
#define macMaxFrameRetries              (0x59)


/*
 * PIB attribute without relevant index, i.e. PIB attribute not
 * contained in 802.15.4-2006 table 88.
 */
#define NO_PIB_INDEX                    (0)

/**
 * The minimum number of symbols forming a LIFS period.
 *
 * - @em Type: Integer
 * - @em Range: See Table 3 in Clause 6 (40 symbols)
 * - @em Default: Dependent on currently selected PHY, indicated by
 * phyCurrentPage
 */
#define macMinLIFSPeriod                (0x5E)

/**
 * Default value for PIB macMinLIFSPeriod
 */
#define macMinLIFSPeriod_def            (40)

/**
 * The minimum number of symbols forming a SIFS period.
 *
 * - @em Type: Integer
 * - @em Range: See Table 3 in Clause 6 (12 symbols)
 * - @em Default: Dependent on currently selected PHY, indicated by
 * phyCurrentPage
 */
#define macMinSIFSPeriod                (0x5F)

/**
 * Default value for PIB macMinSIFSPeriod
 */
#define macMinSIFSPeriod_def            (12)



/**
 * Private MAC PIB attribute to control the CSMA algorithm.
 */

/**
 * Private MAC PIB attribute to allow setting the MAC address in test mode.
 * @todo numbering needs to alligned with other special speer attributes
 */
#define macIeeeAddress                  (0xF0)


/* Non-standard values / extensions */

/**
 * PHY_SUCCESS in phyAutoCSMACA when received ACK frame had the pending bit set
 */
#define PHY_SUCCESS_DATA_PENDING        (0x10)

/**
 * ED scan/sampling duration
 */
#define ED_SAMPLE_DURATION_SYM          (8)


/**
 * Defines the beacon frame type. (Table 65 IEEE 802.15.4 Specification)
 */
#define FCF_FRAMETYPE_BEACON            (0x00)

/**
 * Define the data frame type. (Table 65 IEEE 802.15.4 Specification)
 */
#define FCF_FRAMETYPE_DATA              (0x01)

/**
 * Define the ACK frame type. (Table 65 IEEE 802.15.4 Specification)
 */
#define FCF_FRAMETYPE_ACK               (0x02)

/**
 * Define the command frame type. (Table 65 IEEE 802.15.4 Specification)
 */
#define FCF_FRAMETYPE_MAC_CMD           (0x03)

/**
 * Define the LLDN frame type. See 802.15.4e-2012
 */
#define FCF_FRAMETYPE_LLDN              (0x04)

/**
 * Define the multipurpose frame type. See 802.15.4e-2012
 */
#define FCF_FRAMETYPE_MP                (0x05)

/**
 * A macro to set the frame type.
 */
#define FCF_SET_FRAMETYPE(x)            (x)

/**
 * The mask for the security enable bit of the FCF.
 */
#define FCF_SECURITY_ENABLED            (1 << 3)

/**
 * The mask for the frame pending bit of the FCF
 */
#define FCF_FRAME_PENDING               (1 << 4)

/**
 * The mask for the ACK request bit of the FCF
 */
#define FCF_ACK_REQUEST                 (1 << 5)

/**
 * The mask for the PAN ID compression bit of the FCF
 */
#define FCF_PAN_ID_COMPRESSION          (1 << 6)

/**
 * The mask for a IEEE 802.15.4-2003 compatible frame in the
 * frame version subfield
 */
#define FCF_FRAME_VERSION_2003          (0 << 12)

/**
 * The mask for a IEEE 802.15.4-2006 compatible frame in the
 * frame version subfield
 */
#define FCF_FRAME_VERSION_2006          (1 << 12)

/**
 * The mask for a IEEE 802.15.4e-2012 compatible frame in the
 * frame version subfield
 */
#define FCF_FRAME_VERSION_2012          (2 << 12)

/**
 * Shift value for the frame version subfield fcf1
 */
#define FCF1_FV_SHIFT                   (4)

/**
 * The mask for the frame version subfield fcf1
 */
#define FCF1_FV_MASK                    (3 << FCF1_FV_SHIFT)

/**
 * The mask for a IEEE 802.15.4-2003 compatible frame in the
 * frame version subfield fcf1
 */
#define FCF1_FV_2003                    (0)

/**
 * The mask for a IEEE 802.15.4-2006 compatible frame in the
 * frame version subfield fcf1
 */
#define FCF1_FV_2006                    (1)

/**
 * The mask for a IEEE 802.15.4e-2012 compatible frame in the
 * frame version subfield fcf1
 */
#define FCF1_FV_2012                    (2)

/**
 * Address Mode: NO ADDRESS
 */
#define FCF_NO_ADDR                     (0x00)

/**
 * Address Mode: RESERVED
 */
#define FCF_RESERVED_ADDR               (0x01)

/**
 * Address Mode: SHORT
 */
#define FCF_SHORT_ADDR                  (0x02)

/**
 * Address Mode: LONG
 */
#define FCF_LONG_ADDR                   (0x03)

/**
 * Defines the offset of the destination address
 */
#define FCF_DEST_ADDR_OFFSET            (10)

/**
 * Defines the offset of the source address
 */
#define FCF_SOURCE_ADDR_OFFSET          (14)

/**
 * Macro to set the source address mode
 */
#define FCF_SET_SOURCE_ADDR_MODE(x)     ((unsigned int)((x) << \
	FCF_SOURCE_ADDR_OFFSET))

/**
 * Macro to set the destination address mode
 */
#define FCF_SET_DEST_ADDR_MODE(x)       ((unsigned int)((x) << \
	FCF_DEST_ADDR_OFFSET))

/**
 * Defines a mask for the frame type. (Table 65 IEEE 802.15.4 Specification)
 */
#define FCF_FRAMETYPE_MASK              (0x07)

/**
 * Macro to get the frame type.
 */
#define FCF_GET_FRAMETYPE(x)            ((x) & FCF_FRAMETYPE_MASK)


/**
 * Generic 16 bit broadcast address
 */
#define BROADCAST                       (0xFFFF)


/**
 * Offset of Destination Addressing Mode of octet two of MHR.
 */
#define FCF_2_DEST_ADDR_OFFSET              (2)

/**
 * Offset of Source Addressing Mode of octet two of MHR.
 */
#define FCF_2_SOURCE_ADDR_OFFSET            (6)

/* Octet position within PHY_FrameInfo_t->payload array */

/**
 * Octet position of FCF octet one within payload array of PHY_FrameInfo_t.
 */
#define PL_POS_FCF_1                        (1)

/**
 * Octet position of FCF octet two within payload array of PHY_FrameInfo_t.
 */
#define PL_POS_FCF_2                        (2)

/**
 * Octet position of Sequence Number octet within payload array of PHY_FrameInfo_t.
 */
#define PL_POS_SEQ_NUM                      (3)

/**
 * Octet start position of Destination PAN-Id field within payload array of
 * PHY_FrameInfo_t.
 */
#define PL_POS_DST_PAN_ID_START             (4)

/**
 * Octet start position of Destination Address field within payload array of
 * PHY_FrameInfo_t.
 */
#define PL_POS_DST_ADDR_START               (6)

/**
 * Size of the length parameter
 */
#define LENGTH_FIELD_LEN                    (1)

/**
 * Length of the LQI number field
 */
#define LQI_LEN                             (1)

/**
 * Length of the ED value parameter number field
 */
#define ED_VAL_LEN                          (1)

/**
 * Length (in octets) of FCF
 */
#define FCF_LEN                             (2)

/**
 * Length (in octets) of FCS
 */
#define FCS_LEN                             (2)

/**
 * Length of the sequence number field
 */
#define SEQ_NUM_LEN                         (1)

/**
 * Length (in octets) of extended address
 */
#define EXT_ADDR_LEN                        (8)

/**
 * Length (in octets) of short address
 */
#define SHORT_ADDR_LEN                      (2)

/**
 * Length (in octets) of PAN ID
 */
#define PAN_ID_LEN                          (2)

/**
 * Length (in octets) of ACK payload
 */
#define ACK_PAYLOAD_LEN                     (0x03)




/**
 * @brief Converts a phyTransmitPower value to a dBm value
 *
 * @param phyTransmitPower_value phyTransmitPower value
 *
 * @return dBm using signed integer format
 */
#define CONV_phyTransmitPower_TO_DBM(phyTransmitPower_value) \
	( \
		((phyTransmitPower_value & 0x20) == 0x00) ? \
		((int8_t)(phyTransmitPower_value & 0x3F)) : \
		((-1) *	\
		(int8_t)((~((phyTransmitPower_value & \
		0x1F) - 1)) & 0x1F)) \
	)

/**
 * @brief Converts a dBm value to a phyTransmitPower value
 *
 * @param dbm_value dBm value
 *
 * @return phyTransmitPower_value using IEEE-defined format
 */
#define CONV_DBM_TO_phyTransmitPower(dbm_value)	\
	( \
		dbm_value < -32 ? \
		0x20 : \
		( \
			dbm_value > 31 ? \
			0x1F : \
			( \
				dbm_value < 0 ?	\
				(((~(((uint8_t)((-1) * \
				dbm_value)) - 1)) & 0x1F) | 0x20) : \
				(uint8_t)dbm_value \
			) \
		) \
	)

/* === Types ================================================================ */

#if !defined(DOXYGEN)
typedef enum trx_cca_mode_tag {
	TRX_CCA_MODE0 = 0, /* Carrier sense OR energy above threshold */
	TRX_CCA_MODE1 = 1, /* Energy above threshold */
	TRX_CCA_MODE2 = 2, /* Carrier sense only */
	TRX_CCA_MODE3 = 3 /* Carrier sense AND energy above threshold */
} 

/**
 * CCA Modes of the transceiver
 */
trx_cca_mode_t;
#endif
/* ! @} */

/**
 * CCA mode enumeration
 */
typedef enum cca_mode_tag {
	CCA_MODE_0_CS_OR_ED = 0,
	CCA_MODE_1_ED = 1, /* To be conform to IEEE 15.4 and TRX register */
	CCA_MODE_2_CS,
	CCA_MODE_3_CS_ED,
	CCA_MODE_4_ALOHA
}  cca_mode_t;

typedef enum ch_pg_tag {
	CH_PG_2003 = 0,
	CH_PG_2006 = 2,
	CH_PG_CHINA = 5,
	CH_PG_JAPAN = 6,
	CH_PG_MSK = 7,
	CH_PG_LRP_UWB = 8,
	CH_PG_SUN = 9,
	CH_PG_GENERIC_PHY = 10,
	CH_PG_16 = 16,
	CH_PG_18 = 18,
	CH_PG_INVALID = 0xFF
}  ch_pg_t;

/* === Externals ============================================================ */

/* === Prototypes =========================================================== */

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* IEEE_CONST_H */
/* EOF */
