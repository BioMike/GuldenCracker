from jsonrpc import ServiceProxy
import socket

class Guldencoin:
   def __init__(self):
      # connect to the local guldencoin daemon.
      self.access = ServiceProxy("http://rpcuser:rpcpassword@127.0.0.1:9232")

   def passwordtest(self, password):
      try:
         res = self.access.walletpassphrase(password, 20)
      except socket.error as e:
         print(type(e))
         return(None)
      except Exception as e:
         return(False)
      if res is None:
         return(True)
      else:
         return(None)

   def make_test_wallet(self):
      self.access.encryptwallet("Test")