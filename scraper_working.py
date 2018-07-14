import argparse
import json
import itertools
import re

from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'html.parser')

def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query

def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    # print(link_type_records)
    return link_type_records

def extract_images(query, num_images):
    url = get_query_url(query)
    print("Extracting Soup")
    soup = get_soup(url, REQUEST_HEADER)
    print("Extracting image urls")
    link_type_records = extract_images_from_soup(soup)
    # print(link_type_records)
    return itertools.islice(link_type_records, num_images)

image_links = []

def save_img_links(images, num_images):
    for i, (url, image_type) in enumerate(images):
        
        try:
            print("Making request","(",i+1,"/",num_images,")")
            print('LINK:',url)
            image_links.append(url)

        except Exception as e:
            print("Exception:",e)

def run(query, num_images=100):
    query = '+'.join(query.split())
    print("Extracting image links")
    images = extract_images(query, num_images)
    print("Saving Links")
    save_img_links(images, num_images)
    print("Finished")

def main():
    query = input('Search:')
    num_images=int(input('Number of Images[Max 100]:'))
    run(query,num_images)
    print('Image Links List:',image_links)
    print('Converting to JSON:')
    image_links_json = json.dumps(image_links)
    print(image_links_json)
if __name__ == "__main__":
    main()
