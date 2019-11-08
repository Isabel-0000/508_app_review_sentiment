import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from freq_dist import *
from unique import make_unique

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
   line_list_p = get_lines_from_file('positive10k.txt')
   no_stops_p = remove_all_stop(line_list_p)

   line_list_n = get_lines_from_file('negative10k.txt')
   no_stops_n = remove_all_stop(line_list_n)
   
   print('going to make unique')
   make_unique(no_stops_p, no_stops_n)
   
   f_p = freq_dist(no_stops_p)
   f_n = freq_dist(no_stops_n)
   
   lines = get_lines_from_file('positive10k.txt')
   correct = 0
   total = 0
   for line in lines:
      if decide_sentiment(line, f_p, f_n, len(no_stops_p), len(no_stops_n)) == 1:
         correct += 1
      total += 1
   percent = correct / total
   print("Positive: ", percent)

if __name__ == "__main__":
   main() 
