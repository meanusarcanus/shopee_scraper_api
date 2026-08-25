# 🛍️ Shopee Product & Review Intelligence Scraper Pro Python SDK

Official Python SDK for `shopee-scraper-api`. Extract Shopee product details, price variants, customer reviews, seller shop info, and rating stars in 1 line of Python code.

## 🚀 Installation
```bash
pip install shopee-scraper-api
```

## 💻 Quick Usage
```python
from shopee_scraper import ShopeeScraperClient

client = ShopeeScraperClient(api_key="YOUR_RAPIDAPI_KEY")
res = client.scrape_shopee(product_url="https://shopee.co.th/product/118144917/29975597144", country="TH")

for product in res["products"]:
    print(f"Title: {product['title']} | Rating: {product['rating_star']}★ | Price: {product['currency']} {product['price']}")
```
