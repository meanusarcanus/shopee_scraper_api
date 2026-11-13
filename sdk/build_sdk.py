import os
import io
import tarfile
from pathlib import Path

sdk_dir = Path(__file__).parent
dist_dir = sdk_dir / "dist"
dist_dir.mkdir(exist_ok=True)

pkg_info_content = """Metadata-Version: 2.1
Name: shopee-scraper-api
Version: 1.0.0
Summary: Official Python SDK for Shopee Product & Review Intelligence Scraper Pro.
Home-page: https://github.com/meanusarcanus/shopee_scraper_api
Author: Meanus Arcanus
Author-email: meanusarcanus@gmail.com
License: MIT
Description-Content-Type: text/markdown

# 🛍️ Shopee Product & Review Intelligence Scraper Pro Python SDK

Official Python SDK for `shopee-scraper-api`. Extract Shopee product details, price variants, customer reviews, seller shop info, and rating stars in 1 line of Python code.
"""

tar_path = dist_dir / "shopee_scraper_api-1.0.0.tar.gz"

with tarfile.open(tar_path, "w:gz") as tar:
    # 1. Add PKG-INFO
    info = tarfile.TarInfo(name="shopee_scraper_api-1.0.0/PKG-INFO")
    data = pkg_info_content.encode("utf-8")
    info.size = len(data)
    tar.addfile(info, fileobj=io.BytesIO(data))

    # 2. Add setup.py
    setup_file = sdk_dir / "setup.py"
    if setup_file.exists():
        tar.add(setup_file, arcname="shopee_scraper_api-1.0.0/setup.py")

    # 3. Add pyproject.toml
    pyproject_file = sdk_dir / "pyproject.toml"
    if pyproject_file.exists():
        tar.add(pyproject_file, arcname="shopee_scraper_api-1.0.0/pyproject.toml")

    # 4. Add README.md
    readme_file = sdk_dir / "README.md"
    if readme_file.exists():
        tar.add(readme_file, arcname="shopee_scraper_api-1.0.0/README.md")

    # 5. Add shopee_scraper package
    pkg_dir = sdk_dir / "shopee_scraper"
    for f in pkg_dir.glob("*.py"):
        tar.add(f, arcname=f"shopee_scraper_api-1.0.0/shopee_scraper/{f.name}")

print(f"✓ Rebuilt valid PyPI sdist with PKG-INFO: {tar_path}")
