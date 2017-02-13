from guldencoin import *
import random
import time
import fuzzer_class

pass_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

fuz = fuzzer_class.WordBuild(pass_chars)
NLG = Guldencoin()

# Write checkpoint file every 5 minutes
checkpoint_time = time.time() + 5*60

while True:
   fuz.cnt_increase()
   password = fuz.build_word()
   if NLG.passwordtest(password):
      print("password is %s" % (password))
      exit()
   teller = teller + 1
   if time.time() > checkpoint_time:
      checkpoint_time = checkpoint_time + 5*60
      fuz.store_dict()
