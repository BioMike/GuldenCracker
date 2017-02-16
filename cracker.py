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
   if NLG.passwordtest(password):
      print("password is %s" % (password))
      exit()
   if time.time() > checkpoint_time:
      checkpoint_time = checkpoint_time + 5*60
      fuz.store_dict()
