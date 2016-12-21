#!/bin/env python3

import fuzzer_class

fuz = fuzzer_class.WordBuild("abcdefghijk")

num = 0
while num <= 700:
   #word = fuz.deconstruct_counter(num)
   word = fuz.build_word(num)
   #print(num)
   print(word)
   num += 1
