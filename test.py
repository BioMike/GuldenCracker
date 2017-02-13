#!/bin/env python3

import fuzzer_class

fuz = fuzzer_class.WordBuild("abcdefghijkl")

num = 0
while num <= 10:
   fuz.cnt_increase()
   word = fuz.build_word()
   fuz.print_cnt_dict()
   print(word)
   num += 1

fuz.store_dict()
