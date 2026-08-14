import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="WorkforceLens",
    layout="wide"
)

st.title("WorkforceLens")

st.caption(
    "Ask questions about employee attrition, workforce demographics, "
    "compensation, and retention trends. This assistant writes and runs "
    "its own SQL against the dataset — it isn't matched from a fixed list "
    "of questions."
)

st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("sql"):
            with st.expander("Generated SQL"):
                st.code(message["sql"], language="sql")

question = st.chat_input("Ask anything about your HR dataset...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Writing SQL and analyzing workforce data..."):
            answer, sql = get_answer(question)
            st.markdown(answer)
            if sql:
                with st.expander("Generated SQL"):
                    st.code(sql, language="sql")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sql": sql}
    )

st.caption(
    "Built by Ramit Sakhuja | Groq AI (text-to-SQL)"
)
