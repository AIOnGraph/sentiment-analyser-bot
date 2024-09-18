from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
from openai import AuthenticationError
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
import os
import time
from prompt import prompt_for_sentiment_analysis
load_dotenv()

class SentimentAnalyserBot:
    def __init__(self):
        self.news_content = []
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
            api_key=os.getenv('GROQ_API_KEY'),
            model="llama3-70b-8192",
            temperature=0,
            max_retries=2,
            streaming=True,
            verbose=True
        )
        
    def get_response_from_ai(self, user_text):

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