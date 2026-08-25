"""
Official Python SDK Client for Shopee Product & Review Intelligence Scraper Pro
"""

import requests
from typing import Optional, Dict, Any

class ShopeeScraperClient:
    """
    Python SDK Client for Shopee Scraper API.
    """
    def __init__(self, api_key: str, base_url: str = "https://microsaas-agent-api.vercel.app"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def scrape_shopee(self, product_url: Optional[str] = None, search_query: Optional[str] = None, country: str = "TH", include_reviews: bool = True, max_reviews: int = 30, max_products: int = 10) -> dict:
        """
        Scrape Shopee product details, pricing, variants, ratings, customer reviews, and seller shop info.
        """
        url = f"{self.base_url}/scrape-shopee"
        payload = {
            "product_url": product_url,
            "search_query": search_query,
            "country": country,
            "include_reviews": include_reviews,
            "max_reviews": max_reviews,
            "max_products": max_products
        }
        response = requests.post(url, json=payload, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()
