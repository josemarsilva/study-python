#
# filename   : lab-127-requests-beautifullsoap4-webscrapping.py
# Description:
# Docs       :
#

import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
resp = requests.get(url)
html = BeautifulSoup(resp.text, 'html.parser')

for question in html.select('.question-summary'):
    question_title = question.select_one('.question-hyperlink')
    question_views = question.select_one('.views')
    print(f'* {question_title.text}')
    print(f'  - {question_views.text.strip()}')
