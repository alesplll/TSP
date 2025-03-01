# service_text_processor/text_processor.py
import spacy
# Load the Russian language model
nlp = spacy.load("ru_core_news_md")


def process_text(text):
    """
    Use spaCy to split the input text into sentences.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]
