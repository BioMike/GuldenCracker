
class WordBuild:
   def __init__(self, word_str):
      self.word_string = word_str
      self.cnt_dict = {}

   def cnt_increase(self, idx = 0):
      try:
         self.cnt_dict[idx] = self.cnt_dict[idx] + 1
      except:
         self.cnt_dict[idx] = 0
      if self.cnt_dict[idx] >= len(self.word_string):
         up_one = idx + 1
         self.cnt_increase(up_one)
         self.cnt_dict[idx] = 0

   def print_cnt_dict(self):
      print(self.cnt_dict)

   def build_word(self):
      result = ""
      for x in self.cnt_dict:
         #print("%i, %i" % (x, counter_array[x]))
         idx = self.cnt_dict[x]
         result += self.word_string[idx]
      # Invert the string while returning it.
      return(result[::-1])
