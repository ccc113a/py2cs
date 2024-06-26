import openai
import os
from langchain.llms import Groq
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from dotenv import load_dotenv
load_dotenv()
 
# 载入 API keys; 如果没有，你需要先获取。 
os.environ["GROQ_API_KEY"] = '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' # os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = 'bad5e8f36ebb8ce93c755ab8b11283ad8152a017' # os.getenv("SERPER_API_KEY")

llm = Groq(model_name="text-davinci-003" ,temperature=0)
tools = load_tools(["google-serper", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("奥利维亚·王尔德的男朋友是谁?他现在的年龄的0.23次方是多少?")
