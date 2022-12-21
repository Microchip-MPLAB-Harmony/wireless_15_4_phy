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
phyIntegerBmmLargeBuffers.setDefaultValue(3)

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
