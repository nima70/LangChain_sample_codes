import os
from math import pi
from langchain.agents import create_openai_functions_agent
from langchain import hub
from langchain.tools import tool
from langchain.agents import AgentExecutor
from langchain_openai.chat_models import ChatOpenAI

@tool
def CircumferenceTool(r) -> str:
    """calculate the circumference of a circle given the radius"""
    return 2*r*pi



def main():
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-0613")
  
    prompt = hub.pull("hwchase17/openai-functions-agent")
    # print(prompt.messages)
    print(CircumferenceTool.args)
    agent = create_openai_functions_agent(llm, [CircumferenceTool],prompt)
    tools = [CircumferenceTool]
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({"input": "calculate the circumference of a circle with a radius of 5."})

main()
