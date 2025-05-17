import os
import requests
import googlesearch

from bs4 import BeautifulSoup

def salvar_html_sites(ean, pasta_destino="html_sites"):
    """
    Pesquisa o EAN no Google, retorna a lista de sites encontrados e salva o HTML de cada site em uma pasta.
    """
    # Cria a pasta se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Pesquisa no Google
    urls = list(googlesearch.search(ean, num_results=40))
    print(f"[LOG] {len(urls)} URLs encontradas para o EAN {ean}.")

    session = requests.Session()
    salvos = []
    for idx, url in enumerate(urls, 1):
        try:
            print(f"[LOG] Baixando {url}")
            response = session.get(url, timeout=15)
            if response.status_code == 200:
                # Nome do arquivo: idx_nome_site.html
                nome_site = url.split("//")[-1].split("/")[0].replace('.', '_')
                nome_arquivo = f"{idx:02d}_{nome_site}.html"
                caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    f.write(response.text)
                salvos.append(caminho_arquivo)
                print(f"[LOG] HTML salvo em: {caminho_arquivo}")
            else:
                print(f"[LOG] Falha ao baixar {url} (status {response.status_code})")
        except Exception as e:
            print(f"[LOG] Erro ao baixar {url}: {e}")

    print(f"\nTotal de arquivos salvos: {len(salvos)}")
    return salvos

if __name__ == "__main__":
    ean = input("Digite o EAN para pesquisar e salvar os HTMLs: ")
    salvar_html_sites(ean)