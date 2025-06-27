# Langchain Planning Agent

Description - An interactive planning agent built with Streamlit, Langchain and Gemini, aimed at solving the conundrums of planning activities with your friends. Using a web-based chat interface, the user queries are taken and the agent will search the web using DuckDuckGo for context and provides a relevant answer, while also maintaining conversation context.

This web-app is created to ease the task of planning fun activities with your friends, considering various factors such as vicinity, budget and more.

<br/>

## Workflow:
1. Interface - A Streamlit based interface that accepts a Gemini API Key to enable the conversation. Saves the chat history in the session and makes function calls to the agent, retrieving and displaying the results.

2. Agent - A Langchain based agent that makes use of:
* Search tool provide web search functionality to the agent, internally using DuckDuckGo.
* Conversation Buffer Memory to save the chat history and provide context of the conversation to the agent.
* Google's Gemini - The core of the agent, coupled with Langchain's prompt template, tool calling agent, agent executor and some prompt engineering.

There are various areas of improvement in this project and I hope to accomplish them along the way. I would be happy to receive any feedback, suggestions or improvements and inculcate them within the application.
<br/>

## References:
1. Langchain Documentation
2. Gemini API Key obtained from Google's AI Studio

**You can view the app via:** https://langchain-planning-agent.streamlit.app/
