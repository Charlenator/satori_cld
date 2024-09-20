import streamlit as st
from chatbot import ChatBot
from config import TASK_SPECIFIC_INSTRUCTIONS


def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def main():
    st.set_page_config(
    page_title="Ship My Stuff Customer Service (Demo)",
    page_icon=":robot_face:",
    layout="wide",
    menu_items={
        'About': "Customer Service Chatbot (demo, in development, ShipMyStuff is not liable for anything the bot says :). Ask me anything about shipping!"
    }
    )
    load_css()
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    st.markdown(
    """
    <h1 style="background-image: linear-gradient(to right, #00b7ad, #008000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-color: #f0f0f0;">
        How Can I Help?
    </h1>
    <h2 style="color: #666; font-size: 1.4rem; font-weight: 400; margin-top: 0.1rem;">
        Your Shipping Questions Answered
    </h2>
    """,
    unsafe_allow_html=True
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
    bot_avatar = "https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/bot.png"
    user_avatar = "https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/user.png"
    # Display user and assistant messages skipping the first two
    for message in st.session_state.messages[2:]:
        # ignore tool use blocks
        if isinstance(message["content"], str):
            if message["role"] == "user":
                avatar_link = user_avatar
            else:
                avatar_link = bot_avatar
            with st.chat_message(message["role"], avatar=avatar_link):
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

    if user_msg := st.chat_input("Type your question here..."):
        st.chat_message("user", avatar="https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/user.png").markdown(user_msg)

        with st.chat_message("assistant", avatar="https://raw.githubusercontent.com/Charlenator/satori_cld/master/static/bot.png"):
            with st.spinner("Thinking..."):
                response_placeholder = st.empty()
                full_response = chatbot.process_user_input(user_msg)
                st.markdown(
                    f'<p class="p-6 bg-gray-100 rounded-lg">{full_response}</p>',
                    unsafe_allow_html=True,
                )


if __name__ == "__main__":
    main()
