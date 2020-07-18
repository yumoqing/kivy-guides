
from kivy.factory import Factory

from appPublic.sockPackage import get_free_local_addr

from kivyblocks.vplayer import OSC_VPlayer, Swipe_VPlayer, VPlayer
from kivyblocks.baseWidget import device_type
import socket

DEVICE_TYPE = device_type()

if DEVICE_TYPE == 'tablet':
	BASE = OSC_VPlayer
else:
	BASE = Swipe_VPlayer

class IPTVPlayer(OSC_VPlayer):
	def __init__(self, vfile=None, loop=False, mute=False):
		BASE.__init__(self, vfile=vfile, loop=loop, mute=mute)
		if BASE == OSC_VPlayer:
			self.map('/menu',self.menu)
		else:
			self.bind(on_context_menu=self.menu)

	def menu(self,*args):
			pass

Factory.register('IPTVPlayer',IPTVPlayer)
			
