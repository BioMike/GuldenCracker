from guldencoin import *
import random
import time
import fuzzer_class

pass_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
# Test wallet's pass_chars
#pass_chars = 'Test'


fuz = fuzzer_class.WordBuild(pass_chars)
NLG = Guldencoin()

# Create a test wallet
#NLG.make_test_wallet()

# Write checkpoint file every 5 minutes
checkpoint_time = time.time() + 5*60

while True:
   fuz.cnt_increase()
   password = fuz.build_word()
   result = NLG.passwordtest(password):
   if result is None:
      print("Crypto daemon is not reachable. Does it run?")
      print("Terminating.")
      exit()
   if result:
      print("password is %s" % (password))
      exit()
   if time.time() > checkpoint_time:
      print("Saving progress now... Last tested password is: %s." % (password, ))
      checkpoint_time = checkpoint_time + 5*60
      fuz.store_dict()
