# -*- coding: utf-8 -*-
from modules import service_functions
from modules.kodi_utils import Thread, xbmc_monitor, logger

on_notification_actions = service_functions.OnNotificationActions()

class FenLightMonitor(xbmc_monitor):
	def __init__ (self):
		xbmc_monitor.__init__(self)
		self.startUpServices()

	def startUpServices(self):
		service_functions.CheckSettings().run()
		Thread(target=service_functions.TraktMonitor().run).start()
		Thread(target=service_functions.CustomActions().run).start()
		Thread(target=service_functions.CustomFonts().run).start()
		service_functions.RemoveOldDatabases().run()
		service_functions.AutoRun().run()

	def onNotification(self, sender, method, data):
		on_notification_actions.run(sender, method, data)

logger('Fen Light', 'Main Monitor Service Starting')
logger('Fen Light', 'Settings Monitor Service Starting')
FenLightMonitor().waitForAbort()
logger('Fen Light', 'Settings Monitor Service Finished')
logger('Fen Light', 'Main Monitor Service Finished')