from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()



# ایجاد یک نمونه از کلاینت با کلید API خود
client = OpenAI(base_url='https://api.gapgpt.app/v1', api_key=os.environ.get("api_key"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "سلام!"}
    ]
)

print(response.choices[0].message.content)



def main():
    print("Hello from langchain-course!")
    print(os.environ.get("api_key"))

if __name__ == "__main__":
    main()
