from langchain_groq.chat_models import ChatGroq
from openai import AuthenticationError
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
import time
import streamlit as st
from prompt import prompt_for_sentiment_analysis


class SentimentAnalyserBot:
    """
    A class for performing sentiment analysis using a large language model.
    """
    def __init__(self):
        """
        Initialize the SentimentAnalyserBot with a chat prompt template and LLM.

        The chat prompt template is set up with a system message (containing instructions
        for sentiment analysis) and a human message template for user input.
        The LLM is initialized with specific parameters for the Groq API.
        """
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    f"{prompt_for_sentiment_analysis}"
                ),
                HumanMessagePromptTemplate.from_template("{user_text}, ")
            ],
            input_variables=["user_text"]
        )
        self.llm = ChatGroq(
            api_key=st.secrets['GROQ_API_KEY'],
            model="llama3-70b-8192",
            temperature=0,
            max_retries=2,
            streaming=True,
            verbose=True
        )
        
    def get_response_from_ai(self, user_text):
        """
        Generate an AI response for sentiment analysis of the provided text.

        Args:
            user_text (str): The text to analyze for sentiment.

        Yields:
            str: Chunks of the AI-generated response.

        Raises:
            AuthenticationError: If there is an authentication issue with the API.
        """
        try:
            chain = (self.prompt | self.llm)
            for chunk in chain.stream({"user_text": user_text,}):
                yield chunk.content
                time.sleep(0.05)
        except AuthenticationError:
            return 'AuthenticationError'



if __name__ == "__main__":
    bot = SentimentAnalyserBot()
    user_text = input("Enter your text: ")
    if user_text:
        sentiment_response = bot.get_response_from_ai(user_text=user_text)
        text = ""
        for sentiment in sentiment_response:
            text += sentiment
        print(text)