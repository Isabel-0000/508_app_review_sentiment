import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_lines_from_file(filename):
   line_list = []
   with open(filename) as fp:
      line = fp.readline()
      while (line):
         line_list.append(line.rstrip("\n"))
         line = fp.readline()
   return line_list

def remove_stop(line, stopwords):
   words = word_tokenize(line);
   words_no_stops = []
   for word in words:
      if not word in stopwords:
         words_no_stops.append(word)
   return words_no_stops

def remove_all_stop(line_list):
   stop_words = set(stopwords.words('english'))
   all_non_stop = []
   for line in line_list:
      all_non_stop.extend(remove_stop(line, stop_words))
   return all_non_stop

def main():
   line_list = get_lines_from_file(sys.argv[1])
   print(remove_all_stop(line_list))

if __name__ == "__main__":
   main() 
