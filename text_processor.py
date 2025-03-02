import spacy

# Load the Russian language model
nlp = spacy.load("ru_core_news_md")

# Предполагаем, что nlp уже загружен (например, nlp = spacy.load("ru_core_news_md"))
semantic_mapping = {
    "NOUN": 1,
    "PROPN": 1,
    "VERB": 2,
    "AUX": 2,
    "CCONJ": 3,
    "SCONJ": 3,
    "ADJ": 4,
    # Остальные pos можно отнести к 0 или добавить при необходимости
}


def extract_sentences(text):
    """
    Splits the text into individual sentences using spaCy.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]


def extract_semantic_parts(sentence: str):
    """
    Обрабатывает предложение, присваивая каждому слову семантический индекс и
    объединяя соседние слова в фразы, если разница их семантических индексов не превышает 1.
    """
    doc = nlp(sentence)
    # Собираем токены с их семантическим индексом (игнорируем пунктуацию)
    tokens = []
    for token in doc:
        if token.pos_ == "PUNCT":
            continue
        sem_index = semantic_mapping.get(token.pos_, 0)
        tokens.append((token.text, sem_index))

    if not tokens:
        return []

    # Группируем соседние токены в фразы (если разница между индексами <= 1)
    phrases = []
    current_phrase = tokens[0][0]
    current_indices = [tokens[0][1]]

    for word, sem in tokens[1:]:
        # Если семантическая разница незначительная - объединяем
        if abs(sem - current_indices[-1]) <= 1:
            current_phrase += " " + word
            current_indices.append(sem)
        else:
            phrases.append(current_phrase)
            current_phrase = word
            current_indices = [sem]
    phrases.append(current_phrase)
    return phrases
