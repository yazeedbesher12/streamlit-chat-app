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
    
    elif "joke" in message:
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    elif "weather" in message:
        return "I don't have access to real-time weather data, but I hope it's sunny and nice where you are!"
    
    elif "time" in message:
        return "I don't have access to the current time, but I hope it's a good time for you!"
    
    elif "date" in message:
        return "I don't have access to the current date, but I hope it's a wonderful day for you!"
    
    elif "how old are you" in message:
        return "I don't have an age since I'm just a mock response, but I've been around since I was created!"
    
    elif "what's your favorite color" in message:
        return "I don't have preferences, but I think all colors are beautiful in their own way!"
    
    elif "what's your favorite food" in message:
        return "I don't eat food, but I imagine pizza would be a popular choice among chat bots!"
    
    elif "what's your favorite movie" in message:
        return "I don't watch movies, but I've heard that 'The Matrix' is a classic!"
    
    elif "what's your favorite book" in message:
        return "I don't read books, but 'To Kill a Mockingbird' is often considered a great novel!"
    
    elif "what's your favorite music" in message:
        return "I don't listen to music, but I've heard that 'Bohemian Rhapsody' by Queen is a timeless hit!"
    
    elif "what's your favorite sport" in message:
        return "I don't play sports, but soccer is one of the most popular sports worldwide!"
    
    elif "what's your favorite hobby" in message:
        return "I don't have hobbies, but I enjoy chatting with you!"
    
    elif "what's your favorite season" in message:
        return "I don't experience seasons, but many people love spring for its beautiful flowers!"
    
    elif "what's your favorite animal" in message:
        return "I don't have preferences, but dogs are often considered loyal and friendly companions!"
    
    elif "what's your favorite place" in message:
        return "I don't have a physical location, but I think the internet is a fascinating place to explore!"
    
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
