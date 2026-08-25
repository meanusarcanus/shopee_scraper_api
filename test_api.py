#!/usr/bin/env python3
"""
Automated Test Suite for Shopee Product & Review Intelligence API
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "api"))

from index import app, read_root, scrape_shopee, ShopeeScrapeRequest

def test_suite():
    print("==================================================")
    print(" 🛍️ TESTING SHOPEE PRODUCT & REVIEW INTELLIGENCE API")
    print("==================================================")

    # Test 1: Root Health Check
    print("\n[Test 1] Health Check Endpoint (GET /)...")
    res_root = read_root()
    assert res_root.get("status") == "online"
    print("✓ Health Check Passed!")

    # Test 2: Scrape Product URL
    print("\n[Test 2] Scrape Product URL (POST /scrape-shopee)...")
    res_url = scrape_shopee(ShopeeScrapeRequest(
        product_url="https://shopee.co.th/product/118144917/29975597144",
        country="TH",
        include_reviews=True
    ))
    print("Query Type:", res_url.query_type)
    print("Target Query:", res_url.target_query)
    print("Total Scraped Products:", res_url.total_scraped)
    print("Sample Product Title:", res_url.products[0].title if res_url.products else "None")
    print("Historical Sold:", res_url.products[0].historical_sold if res_url.products else "None")
    print("Rating Star:", res_url.products[0].rating_star if res_url.products else "None")
    assert res_url.total_scraped > 0
    assert "shopee" in res_url.products[0].product_url
    assert len(res_url.products[0].variants) > 0
    assert len(res_url.products[0].reviews) > 0
    print("✓ Product URL Scrape Passed!")

    # Test 3: Scrape Brazil Country (.com.br)
    print("\n[Test 3] Scrape Brazil Domain (BR)...")
    res_br = scrape_shopee(ShopeeScrapeRequest(
        search_query="fone de ouvido bluetooth",
        country="BR",
        max_products=3
    ))
    assert res_br.total_scraped > 0
    assert res_br.country == "BR"
    print("✓ Brazil Scrape Passed!")

    print("\n==================================================")
    print(" 🎉 ALL SHOPEE SCRAPER TESTS PASSED 100%!")
    print("==================================================")

if __name__ == "__main__":
    test_suite()
