from openai import OpenAI,PermissionDeniedError
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=getenv("GPT_TOKEN"))

def ask_ai(question):
    try:
        return client.responses.create(
            store=True,
            model="gpt-4o-mini",
            input=question,
        ).output_text
    except PermissionDeniedError:
        pass
        