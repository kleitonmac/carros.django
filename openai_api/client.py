
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("sua-chave-diretamente-aqui")

def get_car_ai_bio(model, brand, year):
    prompt = (
        f"Me mostre uma descrição de venda para o carro {brand} {model} {year} "
        "em apenas 250 caracteres. Fale coisas específicas desse modelo."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()
