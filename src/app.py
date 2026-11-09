from openai import OpenAI

client = OpenAI()


'''print("-" * 16)
print("Resumidor de textos")
print("-" * 16)
entrada = input("Insira o texto que deseja resumir:")
'''

resposta = client.responses.create(
    model = "gpt-4.1-nano",
    #input = f"Resuma esse texto{entrada}"
    input = "me cumprimente de forma elegante"
)


print("Resposta: ")
print(resposta)