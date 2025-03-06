import pandas as pd

dados = [{"Título": "Analista de Dados", "Empresa": "Empresa X", "Link": "https://vaga.com"}]
df = pd.DataFrame(dados)
df.to_csv("vagas.csv", index=False)


