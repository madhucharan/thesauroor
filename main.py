import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from system_prompt import SYSTEM_PROMPT
load_dotenv()

# Initialize OpenAI client
@st.cache_resource
def init_client():
    try:
        return OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {str(e)}")
        st.error("Please make sure your GEMINI_API_KEY is set in your .env file")
        return None

client = init_client()


# Page Setup 
st.set_page_config(
        page_title="Thesauroor",
        page_icon="tharoor.png",
        layout="centered",
        )
st.logo(
        "tharoor.png",
        size="large"
    )
st.title("Thesauroor", anchor=False)
st.caption("_Your Grandiloquent Guide Through the Gordian Knots of Technology_", help="i have no idea what it means")


def main():
    # initialising session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "Hello, I am Thesauroor, your sesquipedalian guide through the labyrinthine realms of technology. How may I assist you today?"}
        ]
    
    if "processing" not in st.session_state:
        st.session_state.processing = False

    # st.divider()

    # Chatbot interface
    # Chat container
    chat_container = st.container(height=500, border=True)

    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "system":
                continue
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input(
                "",
                placeholder="What technological tempest troubles you?",
                label_visibility="collapsed",
                disabled=st.session_state.processing
            )
        
        with col2:
            send_button = st.form_submit_button(
                ":rocket:", 
                use_container_width=True,
                disabled=st.session_state.processing
            )
    # handle submit
    if send_button and user_input.strip() and not st.session_state.processing:
        if client is None:
            st.error("AI Client not initialized. Please check your API key and configuration.")
        else:
            st.session_state.processing = True
            st.session_state.messages.append({"role": "user", "content": user_input.strip()})
            

            # AI response
            try:
                with st.spinner("Processing your query with the eloquence of a thousand thesauri..."):
                    with chat_container:
                        with st.chat_message("user"):
                            st.markdown(user_input.strip())
                            
                        with st.chat_message("assistant"):
                            stream = client.chat.completions.create(
                                model="gemini-2.0-flash",
                                messages=st.session_state.messages,
                                stream=True,
                                max_tokens=500,
                            )

                            response = st.write_stream(stream)

                        st.session_state.messages.append({"role": "assistant", "content": response})

            except Exception as e:
                st.error(f"An error occurred while processing your request: {e}")
            finally:
                st.session_state.processing = False


if __name__ == "__main__":
    main() 