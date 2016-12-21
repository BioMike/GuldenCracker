from guldencoin import *
import random
import time
import fuzzer_class

counter = 0
pass_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

fuz = fuzzer_class.WordBuild(pass_chars)
NLG = Guldencoin()

#def get_random_word():
#    wordLen = random.randint(7, 8)
#    word = ''
#    for i in range(wordLen):
#        word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
#    return word

teller = 0
starttime = time.time()

while True:
   password = fuz.build_word(counter)
   if NLG.passwordtest(password):
      print("password is %s" % (password))
      exit()
   teller = teller + 1
   counter = counter + 1
   if teller > 100:
      teller = 0
      runtime = time.time() - starttime
      print("Run time: %i seconds" % (runtime))