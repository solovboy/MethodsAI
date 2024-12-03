from aiogram import Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup                        # Импорт классов для работы с состояниями
from aiogram.fsm.context import FSMContext                              # Импорт контекста состояния для работы с данными

from bot.generator import get_answer_from_llama, get_answer_from_gpt    # Импорт функций для получения ответов от моделей

router = Router()  # Создание экземпляра маршрутизатора для обработки сообщений

# Определяем состояния бота с помощью класса StatesGroup
class Generate(StatesGroup):
    text = State()
    choose_model = State()

# Кнопки для выбора модели
model_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="GPT"), KeyboardButton(text="LLaMA")]
    ],
    resize_keyboard=True
)


# Обработка команды /start, которая запускает бот
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        "Привет! 👋 Я бот сервиса CobwebAI. Я помогу вам сориентироваться в сервисе, отвечу на вопросы и решу возможные проблемы.\n\n"
        "Для начала выберите модель, с которой хотите работать:",
        reply_markup=model_buttons
    )
    await state.set_state(Generate.choose_model)  # Устанавливаем состояние "выбор модели"


# Обработка выбора модели
@router.message(Generate.choose_model)
async def choose_model(message: Message, state: FSMContext):
    chosen_model = message.text.strip().lower()
    if chosen_model in ["gpt", "llama"]:
        await state.update_data(model=chosen_model)  # Сохраняем выбранную модель
        await message.answer(
            f"Вы выбрали модель: {chosen_model.upper()}. Теперь вы можете задавать вопросы.",
            reply_markup=types.ReplyKeyboardRemove()  # Убираем кнопки
        )
        await state.set_state(Generate.text)
    else:
        await message.answer(
            "Пожалуйста, выберите модель из предложенных: GPT или LLaMA.",
            reply_markup=model_buttons
        )


# Обработка вопросов пользователя в зависимости от выбранной модели
@router.message(Generate.text)
async def generate(message: Message, state: FSMContext):
    user_data = await state.get_data()
    chosen_model = user_data.get("model", "gpt")

    if chosen_model == "gpt":
        response = await get_answer_from_gpt(message.text)
    elif chosen_model == "llama":
        response = await get_answer_from_llama(message.text)
    else:
        response = "Ошибка: модель не выбрана. Попробуйте начать заново с команды /start."

    await message.answer(response)
