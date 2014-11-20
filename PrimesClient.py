__author__ = 'kirtap'

import rpyc

server = "PrimesServer"

#c = rpyc.connect(server, port = 12345)
c = rpyc.connect_by_service("PrimesServer")
c.root
c.root.isPrime(5)