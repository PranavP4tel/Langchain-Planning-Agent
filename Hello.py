import streamlit as st
from agent import planning_agent

#Setting the page configurations and page information
st.set_page_config(page_title = "Apna Plan!", page_icon="")
st.title("Apna Plan")
st.markdown("Your personal app to plan outings with your college buddies")
st.write("Sample Prompt: What are some local hotspots I can visit in Mumbai that are easily accessible from Dadar, suitable for a group of 5.")

#Setting the chat history in the session
if "messages" not in st.session_state:
    st.session_state.messages = []

#Taking the Gemini API Key from the user 
with st.sidebar:
    st.markdown("Enter your Gemini API Key \n\n (You can get one from Google's AI Studio)")
    GOOGLE_API_KEY = st.text_input(label = "API Key",type="password")

#Printing the entire chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

#User input
prompt = st.chat_input("What do you have in mind?")

#If prompt is provided
if prompt and GOOGLE_API_KEY:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #Append user input in session chat history with role
    st.session_state.messages.append({"role":"user","content":prompt})

    #Giving output
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            #Obtain the response from the agent and append to chat history. Also print it.
            response = planning_agent(api_key = GOOGLE_API_KEY, agent_input= {"input":prompt})
            st.session_state.messages.append({"role":"assistant", "content": response["output"]})
            #st.markdown(response["output"])

            for chunk in response["output"]:
                    full_response += chunk
                    placeholder.markdown(full_response)

        except Exception as e:
            st.markdown(f"Exception: {e}")

else:
    st.warning('Please provide a prompt and an API Key (in the sidebar)', icon="⚠️")


