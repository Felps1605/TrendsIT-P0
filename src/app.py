from client import request

print("-" * 16)
print("RESUMIDOR DE TEXTO")
print("-" * 16)
entrada = input("Insira sua entrada: ")

prompt = "resuma esse texto:"
resposta = request(prompt, entrada, detalhes = False)

print("-" * 16)
print("RESUMO:")
print(resposta)

