import os
from dotenv import load_dotenv
from groq import AsyncGroq
from openai import AsyncOpenAI

load_dotenv()
client_groq = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))        # Создаем асинхронного клиента для работы с Groq API
client_openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Создаем асинхронного клиента для работы с OpenAI API

# Функция для получения ответа от модели LLaMA через Groq API
# Принимает prompt типа str и возвращает ответ типа str
async def get_answer_from_llama(prompt: str) -> str:
    response = await client_groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Ты – русский виртуальный ассистент. Отвечай на вопросы и объясняй функциоанал сервиса CobwebAI, например, конспекты лекций, базы знаний, учебные карточки, чат с виртуальным преподавателем, экспорт материалов, а также процессы регистрации, перевода аудио в текст, оплаты через СБП и Яндекс Pay, решения проблем с размером файлов. Отвечай подробно, чётко и с примерами."""

            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-70b-versatile",
        temperature=0.5,
        max_tokens=400,
        top_p=1,
        stop=None,
        stream=False,
    )

    return response.choices[0].message.content


# Функция для получения ответа от модели GPT через OpenAI API
# Принимает prompt типа str и возвращает ответ типа str
async def get_answer_from_gpt(prompt: str) -> str:
    response = await client_openai.chat.completions.create(
        messages=[
            {   
                "role": "system",
                "content": """Ты – виртуальный ассистент. Отвечай на вопросы и объясняй функциоанал сервиса CobwebAI, например, конспекты лекций, базы знаний, учебные карточки, чат с виртуальным преподавателем, экспорт материалов, а также процессы регистрации, перевода аудио в текст, оплаты через СБП и Яндекс Pay, решения проблем с размером файлов. Отвечай подробно, чётко и с примерами."""
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
        temperature=0.5,
        max_tokens=300,
        top_p=1,
        stop=None,
        stream=False,
    )
    return response.choices[0].message.content