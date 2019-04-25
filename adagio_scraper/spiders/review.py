# -*- coding: utf-8 -*-
from lxml.etree import fromstring
import requests
from ast import literal_eval
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString
  
class ReviewScraper:

    def __init__(self, sku, review_count):
        self.sku = sku
        self.review_count = review_count
        self.API_url = 'https://www.adagio.com/ajax/load_reviews_2017.html'

    def between(self, cur, end):
        while cur and cur != end:
            if isinstance(cur, NavigableString):
                text = cur.strip()
                if len(text):
                    yield text
            cur = cur.next_element

    def get_reviews(self):
        reviews = []
     
        data = {
        'reviewCounter': '0',
        'teaId': self.sku,
        'reviewLoad': self.review_count//100,
        }

        response = requests.post(self.API_url, data=data)
        soup = BeautifulSoup(response.text)
        review_blocks = soup.find_all('div', {'class':'reviewBlock'})
        
        for review in review_blocks:
            item = {}

            copy_block = review.find('div', {'class':'copy'})
            item['review'] = ' '.join(text for text in self.between(
                copy_block.find('span', {'class':'quoteMarks'}).next_sibling, copy_block.find_all('span', {'class':'quoteMarks'})[1])
                )

            try: 
                item['steeping_info'] = copy_block.b.string
            except:
                item['steeping_info'] = None

            raw_date = review.find('div', {'class':'date'}).string.split(' ')
            raw_date[1] = raw_date[1][:-2].rjust(2,'0')
            raw_date[2] = raw_date[2].replace("'",'')
            item['date'] = datetime.strptime(' '.join(raw_date), "%b %d %y").date()

            score_block = review.find('div', {'class':'review'})
            item['score'] = int(score_block.select('div[class*="score_"]')[0]['class'][0].replace('score_',''))

            reviewer_block = review.find('div', {'class':'reviewer'})
            item['userid'] = literal_eval(reviewer_block.find('a')['onclick'].split('viewProfile')[1].split(';')[0])[0]

            item['sku'] = self.sku
            reviews.append(item)

        return reviews

    
  

       
