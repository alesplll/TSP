# Multi-Microservice Text Processing Project

This project demonstrates a microservices architecture where the solution is divided into two independent services:

- **Text Processing Service**: Uses spaCy with the Russian language model to split text into sentences.
- **Table Builder Service**: Builds a table from the processed sentences by splitting each sentence into words.

A gateway script coordinates the workflow by sending requests between the services.

## Project Structure

Project/
├── environment.yml # Conda environment file with required dependencies
├── README.md # This file
├── gateway.py # Script to call the microservices and display the table
├── service_text_processor/ # Text processing microservice
│ ├── app.py # Flask app exposing text processing endpoints
│ └── text_processor.py # Module with text processing logic using spaCy
└── service_table_builder/ # Table building microservice
├── app.py # Flask app exposing table building endpoints
└── table_builder.py # Module with table building functions

## Setup Instructions

1. **Environment Setup**

   - Create and activate the conda environment:
     ```bash
     conda env create -f environment.yml
     conda activate task6_env
     ```
   - Install the spaCy Russian model:
     ```bash
     python -m spacy download ru_core_news_md
     ```

2. **Running the Microservices**

   - **Text Processing Service**

     1. Open a terminal and navigate to the `service_text_processor` directory.
     2. Run the service:
        ```bash
        flask run --port=5001
        ```
        Or:
        ```bash
        python app.py
        ```

   - **Table Builder Service**
     1. Open a second terminal and navigate to the `service_table_builder` directory.
     2. Run the service:
        ```bash
        flask run --port=5002
        ```
        Or:
        ```bash
        python app.py
        ```

3. **Running the Gateway**

   - In a third terminal, run the gateway script to trigger the complete processing:
     ```bash
     python gateway.py
     ```

## How It Works

1. **Text Processing**:  
   The text processing service receives a text payload via a POST request at `/process`, uses spaCy to split the text into sentences, and returns the list of sentences.

2. **Table Building**:  
   The table building service accepts a list of sentences via a POST request at `/build_table`, splits each sentence into words (simulating a table), and returns the table data.

3. **Gateway Coordination**:  
   The gateway script sends the sample text to the text processor and then passes the resulting sentences to the table builder. The resulting table is printed in the console.
