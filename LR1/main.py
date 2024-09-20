from pathlib import Path
from tkinter import *
import requests
import json
from langchain_community.chat_models.gigachat import GigaChat


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Иван\MethodsAI\LR1\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x510")
window.configure(bg = "#3C346C")


def getQuestionYandexGPT():
    questionYandexGPT = entry_3.get()
    return questionYandexGPT

def getQuestionGigaChat():
    questionYandexGPT = entry_1.get()
    return questionYandexGPT

def getAnswerYandexGPT():
    entry_4.delete("1.0", END)
    questionYandexGPT = getQuestionYandexGPT()
    prompt = {
        "modelUri": "gpt://b1go6oqtgiqom40p5k90/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "user",
                "text": questionYandexGPT
            },
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNy5cSxf869o8TS1A-8vYTneRgDLhBgQ9D5aOB"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = json.loads(response.text)
    entry_4.insert(END, result["result"]["alternatives"][0]["message"]["text"])

def getAnswerGigaChat():
    entry_2.delete("1.0", END)
    questionGigaChat = getQuestionGigaChat()
    giga = GigaChat(credentials="ODI0OWUwZjQtMDczNC00YjA0LWJmODItZDE1Y2E3NTZjMzQzOjA4ZDRmOWU1LTBiMWYtNDEyZi04ZmRhLTQ0NjZjMjQ5ZTRkOQ==", verify_ssl_certs=False)
    
    entry_2.insert(END, giga.invoke(questionGigaChat).content)

canvas = Canvas(
    window,
    bg = "#3C346C",
    height = 510,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    450.0,
    0.0,
    900.0,
    510.0,
    fill="#8D8C87",
    outline="")

canvas.create_text(
    493.0,
    189.0,
    anchor="nw",
    text="Answer",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)

canvas.create_text(
    493.0,
    60.0,
    anchor="nw",
    text="Question",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)

canvas.create_text(
    628.0,
    22.0,
    anchor="nw",
    text="GigaChat",
    fill="#FFFFFF",
    font=("Rubik Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getAnswerGigaChat(),
    relief="flat"
)
button_1.place(
    x=590.0,
    y=128.0,
    width=169.0,
    height=56.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    675.0,
    101.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Rubik Bold", 18 * -1),
    highlightthickness=0
)
entry_1.place(
    x=497.0,
    y=81.0,
    width=356.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    675.0,
    348.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Rubik Bold", 18 * -1),
    highlightthickness=0
)
entry_2.place(
    x=497.0,
    y=210.0,
    width=356.0,
    height=275.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    226.0,
    101.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Rubik Bold", 18 * -1),
    highlightthickness=0
)
entry_3.place(
    x=48.0,
    y=81.0,
    width=356.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    225.0,
    348.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=("Rubik Bold", 18 * -1),
    highlightthickness=0
)
entry_4.place(
    x=47.0,
    y=210.0,
    width=356.0,
    height=275.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getAnswerYandexGPT(),
    relief="flat"
)
button_2.place(
    x=142.0,
    y=128.0,
    width=166.0,
    height=56.0
)

canvas.create_text(
    181.0,
    22.0,
    anchor="nw",
    text="YandexGPT",
    fill="#FFFFFF",
    font=("Rubik Bold", 20 * -1)
)

canvas.create_text(
    47.0,
    60.0,
    anchor="nw",
    text="Question",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)

canvas.create_text(
    47.0,
    189.0,
    anchor="nw",
    text="Answer",
    fill="#FFFFFF",
    font=("Rubik Bold", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
