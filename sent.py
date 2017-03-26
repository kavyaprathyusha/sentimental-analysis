
from google.cloud import language


language_client = language.Client()

text = 'i hate this and its bad'
document = language_client.document_from_text(text)

sentiment = document.analyze_sentiment()

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))