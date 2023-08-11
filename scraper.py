###
# Scrape domain looking for all internal links
import time
import requests
from bs4 import BeautifulSoup

url = "https://terem.tech/"

linkstoParse = set()
parsedLinks = set()


def processLinks(link):
    if "<a href" not in str(link):
        return
    aa = str(link).partition(">")[0].rstrip("\"")  #
    aa = aa.lstrip("<a href=")                     # extract the html part
    aa = aa.lstrip("\"")                           #
    if (url in aa or aa.startswith("/")):  # we need to ignore external links
                                           # and keep internal links like /contact
        if aa.startswith("/"):
            aa = url + aa  # expand to full url
        aa = aa.partition("\" ")[0]
        if aa not in linkstoParse and aa.startswith("http") and (not aa.endswith("webm")):
            # haven't added it before
            linkstoParse.add(aa)
            print(aa)


def crawlsite(link):
    print(f"Site to crawl: {link}")
    linkstoParse.add(link)
    while (len(parsedLinks) < len(linkstoParse) and len(linkstoParse) < 5):  # look until we've parsed all links in queue
        copy = linkstoParse.copy()
        print("Parsed: " + str(len(parsedLinks)))
        print("Links: " + str(len(linkstoParse)))
        print("Copy: " + str(len(copy)))
        for a in copy:  # use copy to avoid modifying parsedLinks while iterating through it
            time.sleep(1)  # make longer to avoid hammering a site
            if str(a) not in parsedLinks:
                parsedLinks.add(str(a))   # track that we've looked at it
                r = requests.get(a, timeout=30)

                soup = BeautifulSoup(r.content, 'lxml')
                newlinks = soup.find_all('a')  # find all new links on this page, process
                for b in newlinks:
                    processLinks(b)
        print("Len of parsedLinks: " + str(len(parsedLinks)))
        print("Len of linkstoParse: " + str(len(linkstoParse)))
    return list(linkstoParse)
