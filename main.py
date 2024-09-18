import streamlit as st
from sentiment_analysis import SentimentAnalyserBot


with st.sidebar:
    st.title('Sentiment Analyser Bot')

if "Memory" not in st.session_state:
    st.session_state.Memory = []

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    if message["role"] == 'assistant':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
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