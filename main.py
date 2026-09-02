from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import os
load_dotenv()








def main():
    print("Hello from langchain-course!")
    loader = PyPDFLoader(r"C:\Users\Yaser\Downloads\Documents\example.pdf")
    pages = loader.load()
    information = "\n".join(page.page_content for page in pages)
    summary_template = """
    Summarize the following document: {information}
    Give me:
    the most important points """ 

    summary_prompt_template = PromptTemplate(input_variables= ["information"], template = summary_template)
    llm = ChatOpenAI(temperature=0, model="gpt-5.6-luna",api_key=os.getenv("OPENAI_API_KEY"))
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information" : information})
    print(response.content)
if __name__ == "__main__":
    main()
