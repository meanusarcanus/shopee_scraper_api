# 🛍️ Shopee Product & Review Intelligence Scraper Pro

Extract Shopee product details, prices, SKU variants, full image gallery, seller shop info, ratings & customer reviews across Brazil, Indonesia, Thailand, Malaysia, Singapore, Philippines, Vietnam, and Mexico. Just $4.99/1k items—75% cheaper than legacy scrapers!

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `product_url` | string | Shopee product URL | `https://shopee.co.th/product/118144917/29975597144` |
| `country` | string | Country code | `TH`, `BR`, `ID`, `MY`, `SG`, `PH`, `VN`, `MX` |
| `include_reviews` | boolean | Extract customer reviews | `true` |
| `max_reviews` | integer | Max reviews count | `30` |

## 📤 Output Format

```json
{
  "item_id": "29975597144",
  "shop_id": "118144917",
  "product_url": "https://shopee.co.th/product/118144917/29975597144",
  "title": "Portable Bluetooth 5.3 Speaker Waterproof Heavy Bass",
  "price": 450.0,
  "currency": "THB",
  "rating_star": 4.9,
  "historical_sold": 14200,
  "stock": 850,
  "shop_name": "AudioTech Official Store",
  "shop_location": "Bangkok, Thailand",
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
      "comment": "Excellent bass sound!"
    }
  ],
  "ai_product_sentiment": "Highly Positive (4.9/5 Rating)."
}
```
