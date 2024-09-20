import streamlit as st
from sentiment_analysis import SentimentAnalyserBot
import pandas as pd
import altair as alt
import re
st.set_page_config(
    layout="wide",
    page_title="Sentiment Analyser Bot",
    page_icon="sentiment.jpg",
)

with st.sidebar:
    st.title('Sentiment Analyser Bot')

def extract_percentages(response_text):
    """Extract sentiment percentages from the response text, allowing for any order."""
    
    matches = re.findall(r"(?i)(Positive|Neutral|Negative)\s*\((\d+)%\)", response_text)
    percentages = {"Positive": 0, "Neutral": 0, "Negative": 0}
    for sentiment, value in matches:
        percentages[sentiment.capitalize()] = int(value)
    return percentages

if "Memory" not in st.session_state:
    st.session_state.Memory = []

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'charts' not in st.session_state:
    st.session_state['charts'] = []

for i, message in enumerate(st.session_state.messages):
    if message["role"] == 'assistant':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if i//2 < len(st.session_state.charts):
                st.altair_chart(st.session_state.charts[i//2], use_container_width=True)
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if query := st.chat_input("Ask me anything"):
    bot = SentimentAnalyserBot()
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = st.write_stream(bot.get_response_from_ai(query))
        st.session_state.messages.append({"role": "assistant", "content": response })
        sentiment_percentages = extract_percentages(response)

        df = pd.DataFrame({
            'Sentiment': ['Positive', 'Neutral', 'Negative'],
            'Percentage': [sentiment_percentages['Positive'], sentiment_percentages['Neutral'], sentiment_percentages['Negative']],
            'Color': ['green', 'yellow', 'red']
        })
        
        chart = alt.Chart(df).mark_bar().encode(
            x='Sentiment',
            y='Percentage',
            color=alt.Color('Color', scale=None)
        ).properties(
            width=alt.Step(80)
        )
        st.session_state.charts.append(chart)
        st.altair_chart(chart, use_container_width=True)