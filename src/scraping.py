import requests
from bs4 import BeautifulSoup

url = "https://www.vagas.com.br/vagas-de-dados"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
vagas = soup.find_all("div", class_="vaga")

for vaga in vagas:
    titulo = vaga.find("a").text.strip()
    link = "https://www.vagas.com.br" + vaga.find("a")["href"]
    print(f"{titulo} - {link}")
