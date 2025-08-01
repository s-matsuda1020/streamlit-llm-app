from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.title("課題Webアプリ")

selected_item = st.radio(
    "専門家モードを選択してください。",
    ["健康", "都道府県"]
)

st.divider()

if selected_item == "健康":
    input_message = st.text_input(label="健康に関する質問を入力してください。")
    question = len(input_message)

else:
    input_message = st.text_input(label="都道府県に関する質問を入力してください。")
    question = len(input_message)

if st.button("実行"):
    st.divider()

    if selected_item == "健康":
        from langchain_openai import ChatOpenAI

        from langchain_core.messages import SystemMessage, HumanMessage

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content="あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"),
            HumanMessage(content=input_message),
        ]

        if input_message:
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("健康に関する質問を入力してから「実行」ボタンを押してください。")

    else:
        from langchain_openai import ChatOpenAI

        from langchain_core.messages import SystemMessage, HumanMessage

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content="あなたは都道府県に関するアドバイザーです。"),
            HumanMessage(content=input_message),
        ]
    
        if input_message:
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("都道府県に関する質問を入力してから「実行」ボタンを押してください。")


