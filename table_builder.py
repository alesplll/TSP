def build_table(sentences):
    """
    Builds a table where each row corresponds to a sentence split into words.
    """
    table = []
    for sentence in sentences:
        # Split the sentence by spaces to simulate table columns
        row = sentence.split()
        table.append(row)
    return table
