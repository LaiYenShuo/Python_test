# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:30:21 2018

@author: ms022
"""
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    url='https://www.google.com.tw'
    print('Links in',url)
    for num, link in enumerate(get_links(url),start=1):
        print(num, link)
    print()    
