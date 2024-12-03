import os                            # Модуль для работы с операционной системой, например, чтения переменных окружения
import asyncio                       # Модуль для работы с асинхронными задачами
from aiogram import Bot, Dispatcher  # Импорт необходимых компонентов для работы с Telegram API
from dotenv import load_dotenv       # Модуль для загрузки переменных окружения из файла .env
from bot.handlers import router      # Импорт маршрутизатора (router) с обработчиками событий из модуля bot.handlers


# Асинхронная функция запуска бота
async def main():
    load_dotenv()                            # Загружаем переменные окружения из файла .env
    bot = Bot(token=os.getenv("TG_TOKEN"))   # Создаем объект бота с токеном, загруженным из переменной окружения TG_TOKEN
    dp = Dispatcher()                        # Создаем диспетчер, который управляет маршрутизацией и обработкой событий
    dp.include_router(router)                # Подключаем маршрутизатор с обработчиками событий
    await dp.start_polling(bot)              # Запускаем процесс поллинга (опроса сервера Telegram для получения обновлений)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')


        