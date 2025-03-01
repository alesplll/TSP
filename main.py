import streamlit as st
from text_processor import extract_sentences, extract_semantic_parts
from table_builder import build_table


def main():
    st.title("Text Processing Application")

    text = st.text_area(
        "Enter text:", "Введите текст на русском языке для анализа...")

    if st.button("Process Text"):
        sentences = extract_sentences(text)

        st.subheader("Extracted Sentences:")
        for s in sentences:
            st.write(s)

        st.subheader("Semantic Parts (first 5 words of each sentence):")
        for s in sentences:
            parts = extract_semantic_parts(s)
            st.write(parts)

        st.subheader("Table (Words in each sentence):")
        table = build_table(sentences)
        st.table(table)


if __name__ == '__main__':
    main()
