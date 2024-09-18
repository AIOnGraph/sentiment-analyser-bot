# Sentiment Analyser Bot

## Overview

The Sentiment Analyser Bot is a web application built with Streamlit and LangChain that performs sentiment analysis on user input using a large language model via the Groq API. This bot provides real-time sentiment analysis responses and displays them in a chat-like interface.

## Project Structure

1. **`main.py`**: The main file that sets up the Streamlit web app interface and handles user interactions. It uses the `SentimentAnalyserBot` class from `sentiment_analysis.py` to get responses from the AI and displays them in the chat interface.
   
2. **`sentiment_analysis.py`**: Contains the `SentimentAnalyserBot` class, which is responsible for performing sentiment analysis using the Groq API. It sets up the chat prompt template and communicates with the API to get and stream responses.
3. **`prompt.py`**: contain the prompt template for sentiment analysis


### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/AIOnGraph/sentiment-analyser-bot.git
    cd sentiment-analyser-bot
    ```

2. **Create and activate a virtual environment:**

    - **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

    - **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Secrets**

    Create a `.streamlit/secrets.toml` file with the following content:

    ```toml
    GROQ_API_KEY = "your_groq_api_key_here"
    ```

## Usage

1. **Run the Application**

    ```sh
    streamlit run main.py
    ```

2. **Interact with the Bot**

    Open your web browser and navigate to `http://localhost:8501`. You can input text into the chat interface, and the bot will provide sentiment analysis responses in real-time.


