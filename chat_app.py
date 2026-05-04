import streamlit as st 

st.set_page_config(page_title="Chat App", page_icon=":speech_balloon:",layout="centered")

def generate_mock_response(user_message : str) -> str:
    message = user_message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in message:
        return "I'm just a mock response, but I'm doing great! How about you?"
    
    elif "what's your name" in message or "who are you" in message:
        return "I'm a simple chat app created using Streamlit. I don't have a name, but you can call me ChatBot!"
    
    elif "help" in message:
        return "Sure! I'm here to help. You can ask me anything or just chat with me!"  
    
    elif "thank you" in message or "thanks" in message:
        return "You're welcome! If you have any more questions, feel free to ask."  
    
    elif "what can you do" in message:
        return "I can chat with you, answer simple questions, and provide mock responses. I'm here to make your day better!"
    

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a great day!"
    

st.title("Chat App :speech_balloon:")

st.caption("Welcome to the Chat App! Type your message below and see the mock response.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "Assistant",
            "content": "Hello! I'm your friendly chat bot. How can I assist you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_prompt = st.chat_input("Type your message here...")

if user_prompt:
    st.session_state.messages.append({"role": "User", "content": user_prompt})

    with st.chat_message("User"):
        st.write(user_prompt)   

    
    assistant_response = generate_mock_response(user_prompt)
    st.session_state.messages.append({"role": "Assistant", "content": assistant_response})

    with st.chat_message("Assistant"):
        st.write(assistant_response)


with st.sidebar:
    st.header("About This App")
    st.write(
        """
        This is a simple chat application built using Streamlit. It generates mock responses based on user input. 
        You can ask it basic questions or just have a casual conversation. 
        Feel free to explore and have fun chatting!
        """
    )
