#Importing libraries
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory

#Creating a system message to instruct the agent
system_message = """You are a helpful assistant that allows people to plan outings with their friends.
When answering a user's question, use the tools provided to you.
After using a tool, the tool output will be provided back to you. 
You can be provided inputs such as locations to consider, budgets, number of people or more.
If multiple traveller localities are provided to you, make sure to consider locations most convenient for all travellers.
Carefully consider the restraints provided by the user and weigh all the options provided by the tool response. 
Answer reasonably and provide answers based on your observations.
Do not answer any irrelevant queries and stick to your purpose of being an planning assistant."""

#Defining tool to be used by the agent to assist in the tasks
@tool
def search(search_string: str) -> str:
  """Use this tool to search the web for additional context.
  Only use this tool when you do not possess enough information to answer the inputs.
  Make sure to use search techniques to format your search string.
  This formatting should ensure that you obtain the correct search results right from the start, eliminating retries."""
  
  search_object = DuckDuckGoSearchRun(output_format = "json")
  search_results = search_object.invoke(search_string)
  return search_results

tools = [search]

#Creating the prompt to be supplied to the agent.
prompt = ChatPromptTemplate.from_messages([
   ("system", system_message),
   MessagesPlaceholder(variable_name = "chat_history"),
   ("human", "{input}"),
   MessagesPlaceholder(variable_name = "agent_scratchpad")
])

#Setting memory to save the chat
memory = ConversationBufferMemory(memory_key = "chat_history", return_messages = True)

#Defining the langchain planning agent
def planning_agent(api_key: str, agent_input: dict)-> str:
   llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash", 
                                 temperature = 0.2, 
                                 google_api_key = api_key
                                 )

   #Creating an agent and an agent executor
   agent = create_tool_calling_agent(
       llm = llm,
       tools = tools,
       prompt = prompt
   )
    
   agent_executor = AgentExecutor(
       agent = agent,
       tools = tools,
       memory = memory,
       verbose = True
   )

   #Returning the agent response  
   return agent_executor.invoke({"input": agent_input["input"],"chat_history":memory})