# 🛍️ Shopee Product & Review Intelligence Scraper Pro API

High-performance API engine and Apify Actor designed to scrape Shopee product details, pricing, SKU variants, full image gallery, seller shop info, rating stars, and buyer reviews across all 8 global Shopee regional marketplaces (Brazil, Indonesia, Thailand, Malaysia, Singapore, Philippines, Vietnam, Mexico).

---

## 🚀 Quick Start

### 1. Run Locally
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```

### 2. Run Tests
```bash
python3 test_api.py
```

### 3. API Endpoint (`POST /scrape-shopee`)
```json
{
  "product_url": "https://shopee.co.th/product/118144917/29975597144",
  "country": "TH",
  "include_reviews": true
}
```
