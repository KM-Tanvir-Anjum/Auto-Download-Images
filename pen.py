from icrawler.builtin import BingImageCrawler

# Define a more specific keyword to avoid irrelevant results (like Apple logo, products, etc.)
search_term = "apple fruit"

# Create a safe folder name
safe_search_term = search_term.replace(" ", "_")

# Set up the crawler
bing_crawler = BingImageCrawler(storage={'root_dir': f'images/{safe_search_term}'})
bing_crawler.crawl(keyword=search_term, max_num=30)
