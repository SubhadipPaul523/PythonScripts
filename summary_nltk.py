# Import the required libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Define a function to summarize text by paragraph
def summarize_by_paragraph(text):
  # Split the text into paragraphs
  paragraphs = text.split("\n\n")
  # Initialize an empty list to store the summaries
  summaries = []
  # Loop through each paragraph
  for paragraph in paragraphs:
    # Remove the stop words and tokenize the words
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(paragraph)
    words = [word for word in words if word not in stop_words]
    # Create a frequency table of words
    freq_table = {}
    for word in words:
      if word in freq_table:
        freq_table[word] += 1
      else:
        freq_table[word] = 1
    # Assign a score to each sentence based on the words it contains
    sentences = sent_tokenize(paragraph)
    sentence_scores = {}
    for sentence in sentences:
      sentence_scores[sentence] = 0
      for word in word_tokenize(sentence):
        if word in freq_table:
          sentence_scores[sentence] += freq_table[word]
    # Find the average score of the sentences
    average_score = sum(sentence_scores.values()) / len(sentence_scores)
    # Select the sentences that have a score above the average
    summary = ""
    for sentence in sentences:
      if sentence_scores[sentence] > average_score:
        summary += sentence + " "
    # Append the summary to the list of summaries
    summaries.append(summary)
  # Return the list of summaries
  return summaries

text=input("Enter text: ")
summary=summarize_by_paragraph(text)
print("Summary: ", summary)

