# coding: utf-8
##############################################################################
# Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
###############################################################################

# === Buffer Configuration
#
# Interface
#
global phyMenuBmm
phyMenuBmm = ieee802154phy.createMenuSymbol("PHY_MENU_BMM", None)
phyMenuBmm.setLabel("Buffer Configuration")
phyMenuBmm.setVisible(True)

global phyIntegerBmmLargeBuffers
phyIntegerBmmLargeBuffers = ieee802154phy.createIntegerSymbol("PHY_INTEGER_BMMLARGEBUFFERS", phyMenuBmm)
phyIntegerBmmLargeBuffers.setLabel("Large Buffers")
phyIntegerBmmLargeBuffers.setMin(3)
phyIntegerBmmLargeBuffers.setMax(50)
phyIntegerBmmLargeBuffers.setDefaultValue(5)

global phyCommentBmmLargeBuffers
phyCommentBmmLargeBuffers = ieee802154phy.createCommentSymbol("PHY_COMMENT_BMMLARGEBUFFERS", phyIntegerBmmLargeBuffers)
phyCommentBmmLargeBuffers.setVisible(True)
timersTotalMem = phyConstLargeBufferSize * phyIntegerBmmLargeBuffers.getValue()
phyCommentBmmLargeBuffers.setLabel("Memory occupied: ~%d bytes" %timersTotalMem)
phyCommentBmmLargeBuffers.setDependencies(phyCommentBmmLargeBuffersDepend, ["PHY_INTEGER_BMMLARGEBUFFERS"])


global phyIntegerBmmSmallBuffers
phyIntegerBmmSmallBuffers = ieee802154phy.createIntegerSymbol("PHY_INTEGER_BMMSMALLBUFFERS", phyMenuBmm)
phyIntegerBmmSmallBuffers.setLabel("Small Buffers")
phyIntegerBmmSmallBuffers.setMin(3)
phyIntegerBmmSmallBuffers.setMax(50)
phyIntegerBmmSmallBuffers.setDefaultValue(3)

global phyCommentBmmSmallBuffers
phyCommentBmmSmallBuffers = ieee802154phy.createCommentSymbol("PHY_COMMENT_BMMSMALLBUFFERS", phyIntegerBmmSmallBuffers)
phyCommentBmmSmallBuffers.setVisible(True)
timersTotalMem = phyConstSmallBufferSize * phyIntegerBmmSmallBuffers.getValue()
phyCommentBmmSmallBuffers.setLabel("Memory occupied: ~%d bytes" %timersTotalMem)
phyCommentBmmSmallBuffers.setDependencies(phyCommentBmmSmallBuffersDepend, ["PHY_INTEGER_BMMSMALLBUFFERS"])
