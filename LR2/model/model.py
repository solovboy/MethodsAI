import yaml
from transformers import GPT2LMHeadModel, GPT2Tokenizer


# Обработка файла config.yaml.
# Функция принимает строку пути файла и возращает словарь конфигурации.
def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


# Функция загружает предобученную модель и токенизатор на основе имени модели, указанного в конфигурационном файле
# Принимает строку названия модели и возвращает загруженную модель и токенизатор
def model_pretraining(model_name: str):
    return GPT2Tokenizer.from_pretrained(model_name), GPT2LMHeadModel.from_pretrained(model_name).cuda()


# Функция получения ответа от модели
# Принимает промт и путь до конфиг файла и возвращает ответ
def get_answer(promt: str, config_path: str = "LR2/model/config.yaml") -> str:

    config = load_config(config_path)
    
    model_name = config["model_name"]
    generate_params = config["generate_params"]
    
    tokenizer, model = model_pretraining(model_name)

    input_ids = tokenizer.encode(promt, return_tensors="pt").cuda()
    out = model.generate(input_ids.cuda(), **generate_params)
    generated_text = list(map(tokenizer.decode, out))[0]
    return generated_text
