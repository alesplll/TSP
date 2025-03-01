import spacy

# Load the Russian language model
nlp = spacy.load("ru_core_news_md")


def extract_sentences(text):
    """
    Splits the text into individual sentences using spaCy.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]


def extract_semantic_parts(sentence):
    """
    Attempts to extract 5 semantic parts from the given sentence.
    For demonstration, returns the first 5 words.
    """
    return sentence.split()[:5]
