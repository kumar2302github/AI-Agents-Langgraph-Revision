import streamlit as st
"""
# below line defines the chat_message from the user side 
with st.chat_message("user",avatar="https://static.streamlit.io/examples/dog.jpg"):
    st.text("Hi")


# below line defines the chat_message from the assistant side
with st.chat_message("assistant"):
    st.text("Hello")

# with st.chat_message("user"): is used to show the messages 
user_input =st.chat_input("Your message")
    
# if user input something then we will take it as user input
if user_input:
    with st.chat_message("user"):
        st.text(user_input)
"""

# session state is used to store the chat history, it do not erase the chat history if we just input the query , it will keep the chat history unless we refresh the page


#chat_history=[], not useful anymore after session state knowledge

# as sstreamlit executes after the each user input the chat history will be updated, should be displayed before showing the response 

# session state is dictionary, below it is adding list as key in the session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

# dumb chat bot 
user_input =st.chat_input("Your message")
    
# if user input something then we will take it as user input
if user_input:

    #chat_history.append({"role":"user","content":user_input})
    st.session_state['message_history'].append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.text(user_input)

    #chat_history.append({"role":"assistant","content":user_input})
    st.session_state['message_history'].append({"role":"assistant","content":user_input})

    with st.chat_message("assistant"):
        st.text(user_input) # we are using the user input as the response


 