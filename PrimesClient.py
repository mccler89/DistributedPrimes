__author__ = 'kirtap'

import rpyc

server = "PrimesServer"

c = rpyc.connect(server, port = 12345)
c.root.isPrime(5)