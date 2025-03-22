# Python Web Scraper

A simple Python web scraper that extracts book titles, prices, and ratings from [Books to Scrape](http://books.toscrape.com/) and saves the data to a CSV file.

## Features
- Extracts book titles, prices, and ratings.
- Saves the data to a CSV file (`books.csv`).
- Easy to customize for other websites.

## How to Run
1. **Install Dependencies**:
   Make sure you have Python installed. Then, run:
   ```bash
   pip install requests beautifulsoup4 pandas
   
## Ethical Considerations
- This scraper is for educational purposes only.
- It respects the `robots.txt` file of the target website.
- Avoid overloading the server by adding delays between requests (e.g., `time.sleep(2)`).

![CSV Output](screenshots/csv_output.png)