import streamlit as st
from text_processor import extract_sentences, extract_semantic_parts
from table_builder import build_table


def main():
    st.title("Text Processing Application")

    text = st.text_area(
        "Enter text:", "Введите текст на русском языке для анализа...")

    if st.button("Process Text"):
        sentences = extract_sentences(text)

        st.subheader("Semantic Parts:")
        for s in sentences:
            parts = extract_semantic_parts(s)
            st.write(parts)

        st.subheader("Table:")
        table = build_table(sentences)
        st.dataframe(table, use_container_width=True)


if __name__ == '__main__':
    main()
