

import rpyc

class PrimesServer(rpyc.Service):
    ALIASES = ["foo"]
    print("ok")
    def on_connect(self):

        pass
    def on_disconnect(self):
        pass
    def exposed_isPrime(num):
        for k in range(2, num):
            if (num % k) == 0: return False
            return True

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PrimesServer, port=12345)
    t.start()
