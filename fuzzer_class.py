

class WordBuild:
   def __init__(self, word_str):
      self.word_string = word_str

   def deconstruct_counter(self, num):
      res = {0: 0}
      factor = 0
      while len(self.word_string)**factor < num:
         factor = factor + 1
      factor = factor - 1
      while num > 0:
         if factor > 0:
            val = len(self.word_string)**factor
            times = int(num/val)
            res[factor] = times
            factor = factor - 1
            num = num - (times * val)
         else:
            res[0] = num
            num = 0
      while factor > 0:
         res[factor] = 0
         factor = factor - 1
      return(res)


   def build_word(self, num):
      counter_array = self.deconstruct_counter(num)
      result = ""
      #print(counter_array)
      for x in counter_array:
         #print("%i, %i" % (x, counter_array[x]))
         idx = counter_array[x] - 1
         result += self.word_string[idx]
         
      #while num <= self.cur_size:
         #result += self.word_string[self.track_array[num]]
         #self.track_array[num] = self.track_array[num] + 1
         #print(self.track_array)
         #if self.track_array[num] >= len(self.word_string):
         #     self.track_array[num] = 0
         #    self.cur_size += 1
         #num = num + 1
      # Invert the string while returning it.
      return(result[::-1])
