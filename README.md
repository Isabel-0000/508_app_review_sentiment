# 508_app_review_sentiment

App developers can use app reviews to look through user feedback and determine possible features to add. Negative app reviews are often more helpful to developers than positive app reviews since they often list more specific criticisms or suggest features to add. It would be helpful to have a model that classifies app reviews as positive or negative depending on specific words in the reviews. We will build a model that will mine existing app review data where each review has been manually tagged as negative or positive (the “Android App Reviews Dataset” on GitHub, which includes 10 thousand negative reviews and ten thousand positive reviews). Additionally, we will determine if positive or negative reviews are more likely to be associated with more variation or complexity in words, and if there is a correlation between the length of the review and the sentiment. Finally, it would be helpful to categorize certain words that show up in both positive and negative reviews as ambiguous. Our methods for building the model will include creating frequency distributions for the words in the reviews, remove stopwords. Using the NLTK package in python would be helpful in this process. From there, a new app review will be able to be characterized as negative or positive based on the model using the frequency distribution. We can create a score for a given review to guess if it is positive or negative.
