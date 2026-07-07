import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="Conversational Workforce Analytics Assistant",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Conversational Workforce Analytics Assistant")

st.caption(
    "Ask questions about employee attrition, workforce demographics, compensation, and retention trends."
)

st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input(
    "Ask anything about your HR dataset..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing workforce data..."):

            answer = get_answer(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

st.caption(
    "Built by Ramit Sakhuja | SQL • SQLite • Streamlit • Groq AI"
)