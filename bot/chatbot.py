import openai
from openai import OpenAI
import os
#test
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

def chat(prompt):
    # completion = client.completions.create(model='gpt-3.5-turbo')


    # response = openai.ChatCompletion(
    #     model = "gpt-3.5-turbo",
    #     messages = [{"role":"user","content":prompt}]
    # )
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return completion.choices[0].message.content

    # return response.choices[0].message.content.strip()


