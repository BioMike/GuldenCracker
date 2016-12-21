from jsonrpc import ServiceProxy

class Guldencoin:
   def __init__(self):
      # connect to the local guldencoin daemon.
      self.access = ServiceProxy("http://rpcgebruiker:rpcwachtwoord@127.0.0.1:19332")

   def passwordtest(self, password):
      try:
         res = self.access.walletpassphrase(password, 20)
      except:
         return(False)
      if res is None:
         return(True)
