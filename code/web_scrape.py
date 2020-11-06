# Import depdendencies

import re
import pickle

import requests
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML

# Check to see if we our websites allow web-scraping

def status_codes(urls):
    """
    Takes a list of urls as an argument and returns response code in a disctionary. 
    This is a quick check to see if we are able to scrape some potential websites
    """
    response_dict = {}
    for url in urls:
        response_dict[url] = requests.get(url).status_code
    return response_dict

# Web-scraping Trump Speech

def get_transcript(url):
    """
    Takes a Trump speech URL and extracts the transcript
    """
    transcript = []
    
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "lxml")
    
    for element in soup.find_all('p'):
        transcript.append(element.text)
    
    return transcript