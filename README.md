# Web Scraper README

This is a Python script for scraping HTML content and links from a website. The script uses the `requests`, `BeautifulSoup`, `os`, `re`, `dotenv`, and `random` libraries. The `requests` library is used to fetch the HTML content of a website, `BeautifulSoup` is used to parse the HTML content and extract links, `os` and `re` are used to handle file operations, `dotenv` is used to load environment variables, and `random` is used to randomly select links from the extracted links.

## Installation

1.  Clone the repository to your local machine using `git clone <repository-url>`
2.  Install the required libraries using `pip install -r requirements.txt`
3.  Create a `.env` file in the project directory and set the following environment variables:

    - `URL`: The URL to start scraping from
    - `MAX_LINKS`: The maximum number of links to extract per page
    - `DEPTH`: The depth factor, which determines how many levels of links to follow from the initial URL
    - `UNIQUE`: Set to `True` or `False` to indicate whether or not to remove duplicates from the extracted links
    - `LIMIT_URLS`: Set a number to Limit the number of extracted URLs to avoid performance issues.

    For example

```console
	URL=https://www.ynetnews.com/
	MAX_LINKS=5
	DEPTH=2
	UNIQUE=True
	LIMIT_URLS=1000
```

## Usage

To run the script, execute `python scraper.py` in the project directory. The script will fetch the HTML content of the URL, save it to a file, extract links from it, and save them to files. It will then randomly select links from the extracted links and repeat the process for each selected link, up to the specified depth level. The maximum number of links to extract per page and the uniqueness flag can be configured through the environment variables. The script will print a warning if the number of extracted links is less than the maximum number of links to extract, and if the number of extracted URLs is too large, it will stop the loop and print a warning.

## Edge Cases

1. **Invalid or unreachable URL:** log the error message and skip the URL.

2. **Empty HTML content**: log a warning message and skip the URL.

3. **Maximum links lower than number of extracted links**: log a warning message and extract only the maximum number of links.

4. **Depth factor of zero**: save only the source URL content.

5. **Large number of extracted URLs**: limit the number of extracted URLs to avoid performance issues or crashes. For example, you can set a maximum number of URLs to extract per depth level and handle it appropriately. (default :1000 links)
