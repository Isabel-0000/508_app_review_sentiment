import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

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

def freq_dist(words):
   fdist = FreqDist()
   for word in words:
      fdist[word] += 1

   #fdist.plot(25)
   return fdist

def prob_word(word, fdist, num_words):
   return fdist[word] / num_words

def decide_sentiment(sentence, pos_model, neg_model, num_pos, num_neg):
   no_stop_review = remove_stop(sentence, set(stopwords.words('english')))
   total_neg = 0
   total_pos = 0
   for word in no_stop_review:
      total_neg += prob_word(word, neg_model, num_neg)
      total_pos += prob_word(word, pos_model, num_pos)

   print('Total positive probabilities: ', total_pos)
   print('Total negative probabilities: ', total_neg)
   if total_pos > total_neg:
      print('Result: Positive sentiment')
      return 1
   else:
      print('Result: Negative sentiment')
      return -1

def main():
   line_list_p = get_lines_from_file('positive10k.txt')
   no_stops_p = remove_all_stop(line_list_p)
   f_p = freq_dist(no_stops_p)

   line_list_n = get_lines_from_file('negative10k.txt')
   no_stops_n = remove_all_stop(line_list_n)
   f_n = freq_dist(no_stops_n)
   
   lines = get_lines_from_file('negative10k.txt')
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
