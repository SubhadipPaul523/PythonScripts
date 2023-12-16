from transformers import pipeline

summarization = pipeline("summarization")

original_text=input("Enter the text(it should be in a single para) for summerize: ")

summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)