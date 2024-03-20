import openai

chave_api = ''
openai.api_key = chave_api

def conversa(mensagem, lista_mensagem = []):
    lista_mensagem.append(
        {'role':"user", 'content': mensagem}
    )
    resposta = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagem
    )

    return resposta.choices[0].message.content

lista_mensagem = []

while True:
    texto = input("Digite aqui: ")

    if texto == "sair":
        break
    else:
        resposta = conversa(texto, lista_mensagem)
        lista_mensagem.append({'role': 'user', 'content': resposta})
        print("Chatbot:", resposta)