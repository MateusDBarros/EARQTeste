import requests
import pandas as pd

inicio = "06/04/2025"
fim = "07/04/2025"

series = {
    1: ["Dolar", "Compra"],
    2: ["Dolar", "Venda"],
    21619: ["Euro", "Compra"],
    21620: ["Euro", "Venda"]
}

for codigo in series:
    moeda, tipo = series[codigo]
    print(f"Coletando dados...")

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={inicio}&dataFinal={fim}"

    try:
        resposta = requests.get(url, timeout=20)
        dados = resposta.json()
        df = pd.DataFrame(dados)
        df["moeda"] = moeda
        df["tipo"] = tipo

        nome_arquivo = f"{moeda}_{tipo}.csv"
        df.to_csv(nome_arquivo, index=False)
        print(f"Arquivo salvo: {nome_arquivo}\n")

    except Exception as erro:
        print(f"Erro ao coletar dados de {moeda} - {tipo}")
