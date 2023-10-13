from sklearn.feature_extraction.text import CountVectorizer

# Microsoft python 
# Course   Data And Features   Feature Representation   Feature Representation - Continued

corpus = [
    "If you are trying to \"featurize\" a body of text such as a webpage, a tweet, a passage from a newspaper, an entire book, or a PDF document, creating a corpus of words and counting their frequency is an extremely powerful encoding tool",
    " This is also known as the Bag of Words model, implemented with the CountVectorizer() method in SciKit-Learn. ",
    "Even though the grammar of your sentences and their word-order are completely discarded, this model has accomplished some pretty amazing things, such as being able to correctly identifying J.K. Rowling's writing from a blind line up of authors:"
]

#Another configurable parameter is 
# to have CountVectorizer() use frequencies instead of counts. 
# This is useful when you have documents of different lengths.
#  Words show up more often in the larger document than the shorter one 
# simply based on it's length; 
# so normalizing the word count by the total number of words in each document
#  create a more fair 'direct' comparison between the two. 

bow = CountVectorizer(); # implements the bag of words method
X = bow.fit_transform(corpus) # Sparse matrix 

 #SciPy implements sparse matrices as Python dictionaries: 
 # only the keys that have a value get stored, 
 # and everything else is assumed to be empty.
 #  You can always convert it back to a regular Python list 
 # by using the .toarray() method,
 #  but this converts it to a dense array, 
 # which might not be desirable due to memory usage reasons. 
 # To use your compressed, sparse, row matrix in Pandas, 
 # you're going to want to convert it to a Pandas SparseDataFrame. 
 # More notes on that in the Dive Deeper section.
print(bow.get_feature_names())
 # ['able', 'accomplished', 'also', 'amazing', 'an'

print (X.toarray())
# [[0 0 0 ...

#The bag of words model has other configurable parameters you can tune,
#  such as having it pay attention to the order of words in your text. 
# In such implementations, pairs or tuples of successive words are used 
# to build the corpus instead of individual words:

#bow.get_feature_names()
#['authman ran', 'ran faster', 'faster than', 'than harry', 'harry because',
# 'because he', 'he is', 'is an', 'an athlete', 'authman and',