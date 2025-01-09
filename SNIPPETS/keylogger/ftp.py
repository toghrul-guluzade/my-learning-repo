from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

portal = Portal(FTPRealm("./keylogger"), [AllowAnonymousAccess()])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory) 
reactor.run()