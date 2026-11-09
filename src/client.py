import os
from dotenv import load_dotenv
from google import genai

def request(prompt, entrada):
    load_dotenv()

    api_key = os.getenv("GENAI_API_KEY")
    model = os.getenv("GENAI_MODEL")

    if not api_key:
        raise ValueError("Chave de API não encontrada")

    client = genai.Client(api_key = api_key)

    resposta = client.models.generate_content(
        model = model,
        contents = f"{prompt} {entrada}"
        )

    return resposta.text 