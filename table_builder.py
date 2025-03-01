from text_processor import extract_semantic_parts


def build_table(sentences):
    """
    Builds a table where each row corresponds to a sentence split into words.
    """
    table = []
    for sentence in sentences:
        row = extract_semantic_parts(sentence)
        table.append(row)
    return table
