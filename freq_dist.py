from nltk.probability import FreqDist
from preprocessing import remove_stop
from nltk.corpus import stopwords

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


