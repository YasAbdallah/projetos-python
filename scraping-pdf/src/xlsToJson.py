import pandas as pd
import json

def planilha_para_json(caminho_planilha, caminho_json):
    df = pd.read_excel(caminho_planilha)

    dados_dict = df.to_dict(orient="records")

    with open(caminho_json, 'w', encoding="utf-8") as json_file:
        json.dump(dados_dict, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    caminho_planilha = "computadores.xlsx"
    caminho_json = "computadores.json"
    planilha_para_json(caminho_planilha, caminho_json)
    print("Ok")