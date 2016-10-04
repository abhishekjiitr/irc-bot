from twisted.internet import protocol
from twisted.python import log
from twisted.words.protocols import irc

class TalkBackBotFactory(protocol.ClientFactory):
	# instantiate the Talkback IRC protocol
	
	def __init__(self, settings):
		"""Initialize the bot factory with our settings"""

class TalkBackBot(irc.IRCClient):

	def connectionMade(self):
		"""Called when a connection is made."""

	def connectionLost(self, reason):
		"""Called when a connection is lost. """

	# callbacks for events

	def signedOn(self):
		""" Called when bot has successfully signed on to server"""

	def joined(self, channel):
		"""Called when the bot joins the channel """

	def privmsg(self, user, channel, msg):
		"""Called when the bot receives a message"""