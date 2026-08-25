# 🛍️ RapidAPI Master Listing & Documentation Kit: Shopee Scraper Pro

Complete, standalone documentation kit for publishing **Shopee Product & Review Intelligence Scraper Pro (`POST /scrape-shopee`)** on **RapidAPI Studio** ([provider.rapidapi.com](https://provider.rapidapi.com)).

---

## 📌 1. RapidAPI Listing Metadata

- **API Name**: `Shopee Product & Review Intelligence Scraper Pro`
- **Category**: `E-Commerce` / `Data` / `Shopping`
- **Base URL**: `https://microsaas-agent-api.vercel.app`
- **Endpoint**: `POST /scrape-shopee`

---

## 📝 2. Short Description (Tagline / Summary - Under 250 Chars)

```text
Extract Shopee product details, prices, SKU variants, full image gallery, seller shop info, ratings & customer reviews across Brazil, Indonesia, Thailand, Malaysia, Singapore, Philippines, Vietnam, Mexico. Just $4.99/1k items—75% cheaper!
```

---

## 📜 3. Long Description (RapidAPI Overview Tab)

```markdown
# 🛍️ Shopee Product & Review Intelligence Scraper Pro

Extract Shopee product details, price min/max ranges, SKU variants, full image gallery URLs, seller shop information, historical sold metrics, star ratings, and buyer review comments across all 8 global Shopee regional marketplaces in real-time.

---

## 🚀 Key Features & Extracted Data Fields

* **🛍️ Product Details & Historical Sales**: Item ID, Shop ID, Product Title, Direct URL, Price Min/Max, Currency, Stock Count, and Historical Sold metric.
* **🏷️ SKU Variant Extraction**: Complete list of product options, color/size variants, SKU pricing, and variant image links.
* **⭐ Buyer Ratings & Review Analytics**: Overall Star Rating (out of 5.0) and full customer review comments with buyer usernames and timestamps.
* **🏬 Seller Shop Information**: Shop Name, Shop Location, and Seller Reputation indicators.
* **🌍 Multi-Country Store Support**: Works across Thailand (`TH`), Indonesia (`ID`), Brazil (`BR`), Malaysia (`MY`), Singapore (`SG`), Philippines (`PH`), Vietnam (`VN`), and Mexico (`MX`).

---

## 📥 Sample Request JSON

```json
{
  "product_url": "https://shopee.co.th/product/118144917/29975597144",
  "country": "TH",
  "include_reviews": true
}
```

## 📤 Sample Response JSON

```json
{
  "status": "success",
  "query_type": "url",
  "target_query": "https://shopee.co.th/product/118144917/29975597144",
  "country": "TH",
  "total_scraped": 1,
  "products": [
    {
      "item_id": "29975597144",
      "shop_id": "118144917",
      "product_url": "https://shopee.co.th/product/118144917/29975597144",
      "title": "Portable Bluetooth 5.3 Speaker Waterproof Heavy Bass Wireless Soundbar",
      "price": 450.0,
      "price_min": 390.0,
      "price_max": 490.0,
      "currency": "THB",
      "rating_star": 4.9,
      "historical_sold": 14200,
      "stock": 850,
      "shop_name": "AudioTech Official Store",
      "shop_location": "Bangkok, Thailand",
      "images": [
        "https://down-th.img.susercontent.com/file/sg-11134201-22120-7f2868848123.jpg"
      ],
      "variants": [
        {
          "variant_id": "v1",
          "name": "Navy Blue / 20W Pro",
          "price": 490.0,
          "stock": 430
        }
      ],
      "reviews": [
        {
          "review_id": "r101",
          "author_username": "somchai_t",
          "rating_star": 5,
          "comment": "Excellent bass sound! Fast delivery in 2 days."
        }
      ],
      "ai_product_sentiment": "Highly Positive Buyer Reviews (4.9/5 Star Rating). High historical sales velocity (14.2k+ sold)."
    }
  ]
}
```
```

---

## 💰 4. Recommended RapidAPI Pricing Tiers

| Plan Tier | Monthly Price | Included Requests | Overage Fee / Request |
| :--- | :--- | :--- | :--- |
| **BASIC (Free)** | `$0.00 / mo` | 20 requests | Hard Cap (No Overages) |
| **PRO** | **`$29.00 / mo`** | 2,500 requests | `$0.015 / request` |
| **ULTRA** | **`$79.00 / mo`** | 10,000 requests | `$0.010 / request` |
| **MEGA** | **`$199.00 / mo`** | 30,000 requests | `$0.008 / request` |
