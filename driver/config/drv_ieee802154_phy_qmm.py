# === Queue Configuration
#
# Interface
#
global phyMenuQmm
phyMenuQmm = ieee802154phy.createMenuSymbol("PHY_MENU_QMM", None)
phyMenuQmm.setLabel("Queue Configuration")
phyMenuQmm.setVisible(True)

global phyBooleanQmmEnableQueue
phyBooleanQmmEnableQueue = ieee802154phy.createBooleanSymbol("PHY_BOOLEAN_QMMENABLEQUEUE", phyMenuQmm)
phyBooleanQmmEnableQueue.setLabel("Enable Queueing")
phyBooleanQmmEnableQueue.setVisible(True)
phyBooleanQmmEnableQueue.setDefaultValue(False)
phyBooleanQmmEnableQueue.setReadOnly(True)
phyBooleanQmmEnableQueue.setDescription("Enable multi-packet queueing at PHY")

global phyIntegerQmmQueueCapacity
phyIntegerQmmQueueCapacity = ieee802154phy.createIntegerSymbol("PHY_INTEGER_QMMQUEUECAPACITY", phyBooleanQmmEnableQueue)
phyIntegerQmmQueueCapacity.setLabel("Incoming Frame Queue Capacity")
phyIntegerQmmQueueCapacity.setMin(1)
phyIntegerQmmQueueCapacity.setMax(50)
phyIntegerQmmQueueCapacity.setDefaultValue(1)
phyIntegerQmmQueueCapacity.setVisible(False)
phyIntegerQmmQueueCapacity.setDependencies(phyIntegerQmmQueueCapacityDepend, ["PHY_BOOLEAN_QMMENABLEQUEUE"])
