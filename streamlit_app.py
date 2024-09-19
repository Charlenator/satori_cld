import streamlit as st
from chatbot import ChatBot
from config import TASK_SPECIFIC_INSTRUCTIONS


def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def main():
    load_css()
    st.markdown(
        """
<script src="https://cdn.tailwindcss.com"></script>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<h1 class="text-3xl font-bold mb-4">Ask me almost anything about Shipping!</h1>',
        unsafe_allow_html=True,
    )
    st.logo(
        image="https://shipmystuff-app.com/static/media/Logo_Optimised.02883188.png"
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {'role': "user", "content": TASK_SPECIFIC_INSTRUCTIONS},
            {'role': "assistant", "content": "Understood"},
        ]

    chatbot = ChatBot(st.session_state)

    # Display user and assistant messages skipping the first two
    for message in st.session_state.messages[2:]:
        # ignore tool use blocks
        if isinstance(message["content"], str):
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.markdown(
                        f'''
                        {message["content"]}
                        ''',
                        unsafe_allow_html=True,
                    )
                else:
                 # Assistant message styling
                    st.markdown(
                        f'''
                        {message["content"]}
                         ''',
                        unsafe_allow_html=True
                    )

    if user_msg := st.chat_input("Type your message here..."):
        st.chat_message("user", avatar="https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/user.png").markdown(user_msg)

        with st.chat_message("assistant", avatar="https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/bot.png"):
            with st.spinner("Thinking..."):
                response_placeholder = st.empty()
                full_response = chatbot.process_user_input(user_msg)
                st.markdown(
                    f'<p class="p-6 bg-gray-100 rounded-lg">{full_response}</p>',
                    unsafe_allow_html=True,
                )
     # Apply CSS styling
    st.markdown(
        """
<script src="https://cdn.tailwindcss.com"></script>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
