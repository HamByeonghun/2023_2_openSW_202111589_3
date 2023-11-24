import telegram
import asyncio
from openai import OpenAI

client = OpenAI(
    api_key="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"
)


def ChatGPT():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )
    return completion.choices[0].message.content


def job(answer):
    token = "6737444059:AAEaI28MZZY0hzoHS4Y8H9Oi1rMK2QOcgFA"
    bot = telegram.Bot(token = token)
    public_chat_name = '@k_2023_opensw'
    id_channel = asyncio.run(bot.sendMessage(chat_id=public_chat_name,text=answer)).chat_id
    print(id_channel)

job(ChatGPT())