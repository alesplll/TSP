# Text Processing Application

This project demonstrates a text processing application using Streamlit.

The project is split into several files:

- **main.py**: The main Streamlit application that displays the UI and results.
- **text_processor.py**: Contains functions to split text into sentences and to extract semantic parts.
- **table_builder.py**: Contains functions to build a table from sentences.

## Setup Instructions

1. Create and activate the conda environment:

   ```bash
   conda env create -f environment.yml
   conda activate tsp_env
   ```

2. Install the spaCy Russian model:

   ```bash
   python -m spacy download ru_core_news_md
   ```

3. Run the Streamlit app:

   ```bash
    streamlit run main.py
   ```

## How It Works

### Text Processing:

The app uses spaCy to split the input text into sentences and extracts semantic parts from each sentence.

### Table Building:

Each sentence is also split into words to simulate a table, which is displayed using Streamlit.
