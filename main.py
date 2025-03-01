import spacy

nlp = spacy.load("ru_core_news_md")


def extract_sentences(text):
    """
    Разбивает текст на отдельные предложения с помощью spaCy.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]


def extract_semantic_parts(sentence):
    """
    Для данного предложения пытается выделить 5 смысловых блоков:
      1. Обращение или вводная фраза (до первой запятой, если есть)
      2. Субъект (главный подлежащий, dep == 'nsubj' или 'nsubj:pass')
      3. Предикативная часть (основной глагол и его ближайшее окружение, исключая найденные субъект и объект)
      4. Объект (прямое дополнение, dep == 'obj' или 'dobj')
      5. Модификаторы/дополнения (обстоятельства, nmod, advmod, obl)
    Если какая-то часть не найдена, возвращается пустая строка.

    Данное решение носит эвристический характер и опирается на синтаксический разбор.
    """
    doc = nlp(sentence)

    # 1. Обращение / вводная фраза: берем часть до первой запятой
    address = ""
    for token in doc:
        if token.text == ",":
            address = doc[0:token.i].text.strip()
            break

    # 2. Субъект: ищем первый токен с зависимостью nsubj или nsubj:pass
    subject = ""
    for token in doc:
        if token.dep_ in ("nsubj", "nsubj:pass"):
            subject = " ".join(t.text for t in token.subtree).strip()
            break

    # 3. Предикат: берем основной глагол (корень) и его окрестности, исключая уже найденный субъект и объект
    predicate = ""
    root = None
    for token in doc:
        if token == token.head:
            root = token
            break
    if root:
        # Временами subtree корня включает субъект или объект, поэтому отфильтруем их
        pred_tokens = []
        subject_tokens = set()
        for token in doc:
            if token.text in subject.split():
                subject_tokens.add(token.i)
        # Собираем все токены из поддерева корня, исключая знаки препинания и субъекты
        for t in root.subtree:
            if t.pos_ not in ("PUNCT",) and t.i not in subject_tokens:
                pred_tokens.append(t.text)
        predicate = " ".join(pred_tokens).strip()

    # 4. Объект: ищем токен с зависимостью 'obj' или 'dobj'
    obj = ""
    for token in doc:
        if token.dep_ in ("obj", "dobj"):
            obj = " ".join(t.text for t in token.subtree).strip()
            break

    # 5. Модификаторы / дополнения: берем обстоятельства, nmod, advmod, obl,
    # которые не были включены в предыдущие блоки
    modifiers = []
    taken_spans = []
    # Добавим уже использованные части, чтобы не дублировать их
    if address:
        taken_spans.append(address)
    if subject:
        taken_spans.append(subject)
    if predicate:
        taken_spans.append(predicate)
    if obj:
        taken_spans.append(obj)

    for token in doc:
        if token.dep_ in ("obl", "advmod", "nmod"):
            mod_phrase = " ".join(t.text for t in token.subtree).strip()
            # Простая проверка, чтобы не включить повторяющиеся фрагменты
            if mod_phrase and all(mod_phrase not in span for span in taken_spans):
                modifiers.append(mod_phrase)
    modifier = "; ".join(modifiers)

    return [address, subject, predicate, obj, modifier]


def build_table(text):
    """
    Из входного текста извлекает предложения, для каждого предложения вычисляет
    5 смысловых блоков и возвращает таблицу (список строк, где каждая строка – список колонок).
    """
    sentences = extract_sentences(text)
    table = []
    for sent in sentences:
        parts = extract_semantic_parts(sent)
        table.append(parts)
    return table


def print_table(table):
    """
    Выводит таблицу в консоль. Каждая строка соответствует предложению,
    а колонки – выделенным смысловым блокам.
    """
    header = " | ".join(str(i+1) for i in range(5))
    print(header)
    print("-" * len(header))
    for row in table:
        print(" | ".join(row))


if __name__ == '__main__':
    # Пример текста (доклада)
    text = (
        "Коллеги, совокупность сквозных технологий повышает вероятность нормативного регулирования опасных экспериментов. "
        "С другой стороны, совокупность сквозных технологий несёт в себе риски нормативного регулирования внезапных открытий. "
        "Тем не менее, совокупность сквозных технологий открывает новые возможности несанкционированной кастомизации опасных экспериментов.  \n\n"
        "Тем не менее, парадигма цифровой экономики открывает новые возможности практического применения цифровых следов граждан. "
        "Соответственно, совокупность сквозных технологий открывает новые возможности универсальной коммодитизации волатильных активов. "
        "Следовательно, программа прорывных исследований несёт в себе риски практического применения государственно-частных партнёрств.  \n\n"
        "Следовательно, ускорение блокчейн-транзакций расширяет горизонты универсальной коммодитизации знаний и компетенций. "
        "Вместе с тем, прагматичный подход к цифровым платформам не оставляет шанса для нормативного регулирования непроверенных гипотез. "
        "Следовательно, прагматичный подход к цифровым платформам повышает вероятность бюджетного финансирования волатильных активов."
    )

    table = build_table(text)
    print_table(table)
