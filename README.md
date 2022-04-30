# seo-link-analyzer
SEO Link Analyzer in Python

SEO stands for “search engine optimization.” In simple terms, it means the process of improving your site to increase its visibility when people search for products or services related to your business in Google, Bing, and other search engines. The better visibility your pages have in search results, the more likely you are to garner attention and attract prospective and existing customers to your business.

Search engines use bots to crawl pages on the web, going from site to site, collecting information about those pages and putting them in an index. Think of the index like a giant library where a librarian can pull up a book (or a web page) to help you find exactly what you’re looking for at the time.

Setup
IDE used: PyCharm CE 
Python version: Python3 

File structure:

main.py: Our final program will be called on the command line in the following way:
```
python3 main.py BASE_URL
```
Where ```BASE_URL ``` is the root URL of the website we want to crawl.

report.py: This file will house our functions that will generate the internal linking report 
that we'll eventually be printing to the console for our users. 

test_report.py: Test class to test the functionality of report.py 

crawl.py that takes a string of HTML as input and returns a list of all the link URLs.

Dependencies: defined in ```requirements.txt ```

Tested on:```macOS 12.3 ```
