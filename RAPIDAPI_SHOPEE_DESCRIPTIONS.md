# 📝 RapidAPI Short & Long Descriptions for Shopee Scraper Pro

Below are the pre-written **Short Description** and **Long Description** formatted specifically for your RapidAPI listing.

---

## 📌 1. Short Description (Tagline / Summary - Under 250 Chars)

```text
Extract Shopee product details, prices, SKU variants, full image gallery, seller shop info, ratings & customer reviews across Brazil, Indonesia, Thailand, Malaysia, Singapore, Philippines, Vietnam, Mexico. Just $4.99/1k items—75% cheaper!
```

---

## 📜 2. Long Description (Full RapidAPI Overview Markdown)

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

## 🛠️ Example Use Cases

1. **E-Commerce Market Research & Dropshipping**: Discover best-selling products, price ranges, and top seller shops across Southeast Asia and Latin America.
2. **Competitor Price & Variant Monitoring**: Track variant SKU inventory levels, price fluctuations, and historical sales trends.
3. **Sentiment & Review Mining**: Analyze customer feedback and review sentiments to identify product flaws and market opportunities.

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
