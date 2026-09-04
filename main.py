from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama
import os
load_dotenv()

def main():
    print("Hello from langchain-course!")
    loader = PyPDFLoader(r"C:\Users\Yaser\Downloads\Documents\example.pdf")
    pages = loader.load()
    information = """What is agentic AI?
    Agentic AI is an artificial intelligence system that can accomplish a specific goal with limited supervision. It consists of AI agents—machine learning models that mimic human decision-making to solve problems in real time. In a multiagent system, each agent performs a specific subtask required to reach the goal and their efforts are coordinated through AI orchestration.

    Unlike traditional AI models, which operate within predefined constraints and require human intervention, agentic AI exhibits autonomy, goal-driven behavior and adaptability. The term “agentic” refers to these models’ agency, or, their capacity to act independently and purposefully.

    What are the advantages of agentic AI?
    Agentic systems have many advantages over their generative predecessors, which are limited by the information contained in the datasets upon which models are trained.

    Autonomous
    The most important advancement of agentic systems is that they allow for autonomy to perform tasks without constant human oversight. Agentic systems can maintain long-term goals, manage multistep problem-solving tasks and track progress over time.

    Proactive
    Agentic systems provide the flexibility of LLMs, which can generate responses or actions based on nuanced, context-dependent understanding, with the structured, deterministic and reliable features of traditional programming. This approach allows agents to “think” and “do” in a more human-like fashion.

    LLMs by themselves can’t directly interact with external tools or databases or set up systems to monitor and collect data in real time, but agents can. Agents can search the web, call application programming interfaces (APIs) and query databases, then use this information to make decisions and take actions.

    Specialized
    Agents can specialize in specific tasks. Some agents are simple, performing a single repetitive task reliably. Others can use perception and draw on memory to solve more complex problems. An agentic architecture might consist of a “conductor” model powered by an LLM that oversees tasks and decisions and supervises other, simpler agents. Such architectures are ideal for sequential workflows but are vulnerable to bottlenecks. Other architectures are more horizontal, with agents working in harmony as equals in a decentralized fashion, but this architecture can be slower than a vertical hierarchy. Different AI applications demand different architectures.

    Adaptable
    Agents can learn from their experiences, take in feedback and adjust their behavior. With the right guardrails, agentic systems can improve continuously. Multiagent systems possess the scalability to eventually handle broadly scoped initiatives.

    Intuitive
    Because agentic systems are powered by LLMs, users can engage with them with natural language prompts. This means that entire software interfaces—think of the many tabs, dropdowns, charts, sliders, pop-ups and other UI elements involved in the SaaS platform of one’s choice—can be replaced by simple language or voice commands. Theoretically, any software user experience can now be reduced to “talking” with an agent, who can fetch the information one needs and take action based on that information. This productivity benefit can barely be overstated, when one considers the time it takes for workers to learn and master new interfaces and tools.

    Join 100,000+ subscribers for the latest tech news
    Stay up to date on the most important—and intriguing—industry news on AI, automation, data, quantum, infrastructure and security with the Think Newsletter, delivered twice weekly. 
    How agentic AI works
    Agentic AI tools can take many forms and different frameworks are better suited to different problems, but here are the general steps that agentic systems take to perform their operations.

    Perception
    Agentic AI begins by collecting data from its environment through sensors, APIs, databases or user interactions. This step ensures that the system has up-to-date information to analyze and act upon.

    Reasoning
    Once the data is collected, the AI processes it to extract meaningful insights. Using natural language processing (NLP), computer vision or other AI capabilities, it interprets user queries, detects patterns and understands the broader context. This ability helps the AI determine what actions to take based on the situation.

    Goal setting
    The AI sets objectives based on predefined goals or user inputs. It then develops a strategy to achieve these goals, often by using decision trees, reinforcement learning or other planning algorithms.

    Decision-making
    AI evaluates multiple possible actions and chooses the optimal one based on factors such as efficiency, accuracy and predicted outcomes. It might use probabilistic models, utility functions or machine learning-based reasoning to determine the best course of action.
"""
    summary_template = """
      given information {information} about Agentic AI I want you to create :
      1. A short summary
      2. two interesting points about the subject
     """ 

    summary_prompt_template = PromptTemplate(input_variables= ["information"], template = summary_template)
    
    llm = ChatOpenAI(temperature=0, model="gpt-5.6-luna",api_key=os.getenv("OPENAI_API_KEY"))
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    if ((os.getenv("ALLOW_OLLAMA")=="True")|(os.getenv("ALLOW_OPENAI_API_KEY")=="True")):
        response = chain.invoke(input={"information" : information})
        print(response.content)

    else:
        print("No model has been selected !")
    

if __name__ == "__main__":
    main()
