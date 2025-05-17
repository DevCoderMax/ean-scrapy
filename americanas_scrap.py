import requests
from lxml import html


def scrape_americanas(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tree = html.fromstring(response.content)

    # Exemplo de extração: título, preço e descrição
    title = tree.cssselect('.ProductInfoCenter_title__hdTX_')
    return {
        'title': title,
    }


def main():
    url = 'https://www.americanas.com.br/produto/107665952/bebida-energetica-fusion-garrafa-1-l'
    data = scrape_americanas(url)
    print("\nDados extraídos:")
    for k, v in data.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()