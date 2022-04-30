from urllib.parse import urlparse
from lxml import html
import requests


def crawl_page(base_url, current_url, pages):
    normalized_url = normalize_url(current_url)

    # This is a new page, create an entry first
    if normalized_url not in pages:
        pages[normalized_url] = 0

    # If this URL is offsite, then just skip it
    if urlparse(base_url).netloc != urlparse(current_url).netloc:
        pages[normalized_url] = None
        return pages

    # If this is a page that has been already checked and is not valid skip it
    if pages[normalized_url] is None:
        return pages

    # If the is already validated then increase count and skip it
    if pages[normalized_url] > 0:
        pages[normalized_url] += 1
        return pages

    # Make a request to the URL
    resp = requests.get(base_url)

    # If the response is not valid page then log and skip it
    try:
        validate_response(resp, current_url)
    except Exception as e:
        print(e)
        pages[normalized_url] = None
        return pages

    # Increment the count for this page
    pages[normalized_url] += 1

    # Scan the page and crawl
    urls = get_urls_from_string(resp.content, base_url)
    for url in urls:
        crawl_page(base_url, url, pages)
    return pages


def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception("{} response status not OK {}".format(url, resp.status_code))

    # if content is not HTML skip it
    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception("{} could not find HTML response".format(url))


# get_urls_from_string scans through a string,
# finds all the links, and returns the urls in a list
def get_urls_from_string(page_content, base_url):
    urls = []
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url=base_url)
    for elem in tree.iter():
        if elem.tag == "a":
            url = elem.get("href")
            urls.append(url)
    return urls


# normalize_url returns a "normalized" URL that can be used to
# deduplicate URLs which resolve to the same web page
def normalize_url(url):
    parsed_url = urlparse(url)
    netloc_path = "{}{}".format(parsed_url.netloc, parsed_url.path)
    loweredcased = netloc_path.lower()
    if len(loweredcased) < 1:
        return loweredcased
    last_slash_removed = loweredcased if loweredcased[-1] != "/" else loweredcased[:-1]
    return last_slash_removed
