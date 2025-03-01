# service_table_builder/table_builder.py

def build_table(sentences):
    """
    Build a simple table where each row corresponds to a sentence.
    For demonstration, each sentence is split into words.
    """
    table = []
    for sentence in sentences:
        # Split the sentence by spaces to simulate columns
        row = sentence.split()
        table.append(row)
    return table


def print_table(table):
    """
    Print the table in a formatted way.
    """
    for row in table:
        print(" | ".join(row))
