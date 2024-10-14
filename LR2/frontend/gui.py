import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, Scrollbar, END, INSERT, TclError
from model.model import get_answer


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Иван\MethodsAI\LR2\frontend\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Функция получения промта
def get_promt() -> str:
    promt = entry.get("1.0", END)
    return promt


# Функция получения ответа на промпт из entry блока и вывода в интерфейс
def get_answer_from_model():
    output.delete("1.0", END)
    promt = get_promt()
    answer = get_answer(promt)
    output.insert(END, answer)


# Создание окна
window = Tk()

window.geometry("900x510")
window.configure(bg = "#3C346C")


# Интерфейс окна
canvas = Canvas(
    window,
    bg = "#3C346C",
    height = 510,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


# Текст ruGPT3
canvas.place(x = 0, y = 0)
canvas.create_text(
    412.0,
    20.0,
    anchor="nw",
    text="ruGPT3",
    fill="#FFFFFF",
    font=("Rubik Bold", 20 * -1)
)


# Функции для работы с буфером обмена
def copy_text(event=None):
    window.clipboard_clear()
    window.clipboard_append(entry.selection_get())


def paste_text(event=None):
    try:
        entry.insert(INSERT, window.clipboard_get())
    except TclError:
        pass


def cut_text(event=None):
    copy_text()
    entry.delete("sel.first", "sel.last")


# Интерфейс блока ввода
entry_image = PhotoImage(
    file=relative_to_assets("promt.png")
)

entry_bg = canvas.create_image(
    230.0,
    257.0,
    image=entry_image
)

entry = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    wrap="word",  # Для автоматического переноса строк
    font=("Rubik Bold", 18 * -1)
)

entry.place(
    x=52.0,
    y=81.0,
    width=356.0,
    height=350.0
)

# Привязка горячих клавиш для копирования, вставки и вырезания
entry.bind_class("Text", "<Control-c>", copy_text)
entry.bind_class("Text", "<Control-v>", paste_text)
entry.bind_class("Text", "<Control-x>", cut_text)

# Создание скролла блока ввода
scrollbar_1 = Scrollbar(canvas)
scrollbar_1.place(x=414, y=81, height=352)

# Привязка скроллбара к виджету Text entry1
entry.config(yscrollcommand=scrollbar_1.set)
scrollbar_1.config(command=entry.yview)


# Интерфейс блока вывода
output_image = PhotoImage(
    file=relative_to_assets("answer.png"))

output_bg = canvas.create_image(
    670.0,
    257.0,
    image=output_image
)

output = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    wrap="word",
    font=("Rubik Bold", 18 * -1)
)

output.place(
    x=492.0,
    y=81.0,
    width=356.0,
    height=350.0
)

# Создание скролла блока вывода
scrollbar_2 = Scrollbar(canvas)
scrollbar_2.place(x=853, y=81, height=352)

# Привязка скроллбара ко второму текстовому полю
output.config(yscrollcommand=scrollbar_2.set)
scrollbar_2.config(command=output.yview)


# Интерфейс кнопки получения ответа
button_image = PhotoImage(
    file=relative_to_assets("buttonGet.png"))

button = Button(
    image=button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_answer_from_model(),
    relief="flat"
)

button.place(
    x=367.0,
    y=443.0,
    width=166.0,
    height=56.0
)


# Название блока ввода промта
canvas.create_text(
    196.0,
    50.0,
    anchor="nw",
    text="Prompt",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)


# Название блока ответа
canvas.create_text(
    636.0,
    50.0,
    anchor="nw",
    text="Answer",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)

def show_gui():
    window.resizable(False, False)
    window.mainloop()
