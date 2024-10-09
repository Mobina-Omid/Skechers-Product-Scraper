
# Skechers Product Scraper

This Python project scrapes product information from the Skechers Germany website, including the titles, colors, and prices of women's shoes. The data is extracted and saved into a CSV file for further analysis.

## Features

- Scrapes product titles, colors, and prices from the Skechers website.
- Cleans and structures the data into a pandas DataFrame.
- Saves the data into a CSV file (`SKECHERS.csv`).
- Includes the following fields: 
  - **Index**: Product index
  - **Title**: Name of the product
  - **Price**: Price in euros (€)
  - **Color**: Number of available color options

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` from the `bs4` package
- `pandas` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mobina-Omid/skechers-product-scraper.git
   ```

2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

Run the Python script to scrape the data:
```bash
python skechers_scraper.py
```

The script will:
1. Scrape product data from the [Skechers Germany website](https://www.skechers.de/damen/schuhe/?start=0&sz=576).
2. Create a CSV file (`SKECHERS.csv`) containing the product titles, colors, and prices.

## Output Example

The CSV file (`SKECHERS.csv`) will contain columns like this:

| Index | Title                         | Price | Color           |
|-------|-------------------------------|-------|-----------------|
| 1     | Skechers Ultra Flex 3.0       | 69.99 | 4               |
| 2     | Skechers Go Walk Joy          | 49.99 | 3               |


