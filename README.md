#Resumidor de texto
    Recebe um texto pelo terminal, envia para uma LLM e devolve o resumo também no terminal

##Como instalar
    Instale as bibliotecas google-genai e python-dotenv com [pip](https://pip.pypa.io/en/stable/):
    
    ```bash
    pip install google-genai
    ```
    ```bash
    pip install python-dotenv
    ```

    Faça a clonagem do repositório:
    ```bash
    git clone https://github.com/Felps1605/TrendsIT-P0
    ```

    Insira as variáveis de ambiente:
    
    Entre na pasta do repositório:
    ```bash
    cd TrendsIT-P0/src
    ```
    Abra o arquivo ".env.example", insira a chave api da LLM e o modelo(atualmente utilizando "gemini-3.5-flash-lite"), salve e renomeie o arquivo para ".env"
    



##COMO USAR
    Entre na pasta do programa: 
    ```bash
    cd TrendsIT-P0/src
    ```
    Execute o programa app.py
    ```bash
    python app.py
    ```
    Cole o texto que vc deseja resumir na tela(como uma linha só)



##FERRAMENTAS
O programa é escrito em python, utilizando as bibliotecas google-genai e python-dotenv. o script app.py é responsável por interagir com o usuário, enquanto client.py faz a requisição para a LLM e devolve a resposta utilizando as variáveis de ambiente configuradas no .env