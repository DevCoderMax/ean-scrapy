import requests
from bs4 import BeautifulSoup
import pandas as pd
import googlesearch
import os
import sys
import json
import lxml.html  

# lista de sites permitidos pra scraping no arquivo sites_to_scrape.txt


def carregar_elementos():
    with open(os.path.join("core", "elements.json"), "r") as f:
        return json.load(f)


class EANScraper:
    def __init__(self, ean):
        self.ean = ean
        self.base_url = list(googlesearch.search(self.ean, num_results=30))
        self.session = requests.Session()
        self.elementos = carregar_elementos()

    def scrape(self):
        resultados = []
        for url in self.base_url:
            if "americanas.com.br" in url:
                print(f"[LOG] Encontrado link da Americanas: {url}")
                response = self.session.get(url)
                print(f"[LOG] Status code: {response.status_code}")
                tree = lxml.html.fromstring(response.content)
                seletores = self.elementos["americanas"]

                def extrair_campo(tree, seletor):
                    if not seletor or not seletor.get("type") or not seletor.get("value"):
                        return None
                    tipo = seletor["type"]
                    valor = seletor["value"]
                    if tipo == "xpath":
                        resultado = tree.xpath(valor)
                        return resultado[0].strip() if resultado else None
                    elif tipo == "css":
                        resultado = tree.cssselect(valor)
                        return resultado[0].text_content().strip() if resultado else None
                    elif tipo == "class_name":
                        resultado = tree.xpath(f'//*[contains(@class, "{valor}")]')
                        return resultado[0].text_content().strip() if resultado else None
                    else:
                        return None

                # Monta o resultado dinamicamente com base nos seletores do JSON
                resultado = {"url": url}
                for campo, seletor in seletores.items():
                    resultado[campo] = extrair_campo(tree, seletor)

                # Complementa usando JSON-LD se faltar algum campo
                if any(resultado.get(campo) is None for campo in seletores.keys()):
                    soup = BeautifulSoup(response.text, "html.parser")
                    product_data = None
                    breadcrumb_data = None
                    for script in soup.find_all('script', type='application/ld+json'):
                        try:
                            data = json.loads(script.string)
                            if data.get('@type') == 'Product':
                                product_data = data
                            elif data.get('@type') == 'BreadcrumbList':
                                breadcrumb_data = data
                        except Exception:
                            continue
                    if product_data:
                        # Tenta preencher campos faltantes a partir do JSON-LD
                        for campo in seletores.keys():
                            if resultado.get(campo) is None:
                                if campo == "titulo":
                                    resultado[campo] = product_data.get("name")
                                elif campo == "descricao":
                                    resultado[campo] = product_data.get("description")
                                elif campo == "imagem":
                                    img = product_data.get("image")
                                    resultado[campo] = img[0] if isinstance(img, list) else img
                                elif campo == "preco":
                                    resultado[campo] = product_data.get("offers", {}).get("price")
                                elif campo == "categorias":
                                    if product_data.get("category"):
                                        resultado[campo] = [product_data.get("category")]
                    if breadcrumb_data and breadcrumb_data.get("itemListElement"):
                        resultado["categorias"] = [item["name"] for item in breadcrumb_data["itemListElement"] if "name" in item]

                resultados.append(resultado)
        return resultados


if __name__ == '__main__':
    ean = input("Digite o EAN: ")
    scraper = EANScraper(ean)
    resultados = scraper.scrape()
    if resultados:
        for r in resultados:
            print("URL:", r["url"])
            for campo, valor in r.items():
                if campo != "url":
                    print(f"{campo.capitalize()}: {valor}")
            print("-"*40)
    else:
        print("Nenhum resultado encontrado nas páginas da Americanas.")
