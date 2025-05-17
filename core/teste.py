from bs4 import BeautifulSoup
import json

with open('core/last_americanas.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Extract JSON-LD
product_data = None
for script in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(script.string)
        if data.get('@type') == 'Product':
            product_data = data
            break
    except Exception:
        continue

if product_data:
    name = product_data.get('name')
    description = product_data.get('description')
    brand = product_data.get('brand', {}).get('name')
    sku = product_data.get('sku')
    gtin = product_data.get('gtin')
    image = product_data.get('image')[0] if isinstance(product_data.get('image'), list) else product_data.get('image')
    price = product_data.get('offers', {}).get('price')
    currency = product_data.get('offers', {}).get('priceCurrency')
    availability = product_data.get('offers', {}).get('availability')
    url = product_data.get('offers', {}).get('url')
    print({
        'name': name,
        'description': description,
        'brand': brand,
        'sku': sku,
        'gtin': gtin,
        'image': image,
        'price': price,
        'currency': currency,
        'availability': availability,
        'url': url
    })