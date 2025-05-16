from icrawler.builtin import BingImageCrawler  # instead of GoogleImageCrawler

search_term = input("Enter the object you want to download images of: ")
bing_crawler = BingImageCrawler(storage={'root_dir': f'images/shahioal'})
bing_crawler.crawl(keyword=search_term, max_num=30)
