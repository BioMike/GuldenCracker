import pickle

class WordBuild:
   def __init__(self, word_str):
      self.cnt_dict = {}
      self.load_dict()
 
      if not 'word_string' in self.cnt_dict:
         self.cnt_dict['word_string'] = ""
 
      if self.cnt_dict['word_string'] == word_str:
         print("Continueing searching with checkpoint %s." % (str(self.cnt_dict), ))
      else:
         print("Starting new search with characters %s." % (word_str, ))
         self.cnt_dict = {}
         self.cnt_dict['word_string'] = word_str

   def store_dict(self):
      with open('checkpoint.data', 'wb') as file_obj:
         pickle.dump(self.cnt_dict, file_obj, pickle.HIGHEST_PROTOCOL)

   def load_dict(self):
      try:
         with open('checkpoint.data', 'rb') as file_obj:
            self.cnt_dict = pickle.load(file_obj)
      except:
         pass

   def cnt_increase(self, idx = 0):
      try:
         self.cnt_dict[idx] = self.cnt_dict[idx] + 1
      except:
         self.cnt_dict[idx] = 0
      if self.cnt_dict[idx] >= len(self.cnt_dict['word_string']):
         up_one = idx + 1
         self.cnt_increase(up_one)
         self.cnt_dict[idx] = 0

   def print_cnt_dict(self):
      print(self.cnt_dict)

   def build_word(self):
      word_string = self.cnt_dict['word_string']
      result = ""
      for x in self.cnt_dict:
         if x != 'word_string':
            #print("%i, %i" % (x, counter_array[x]))
            idx = self.cnt_dict[x]
            result += word_string[idx]
      # Invert the string while returning it.
      return(result[::-1])
