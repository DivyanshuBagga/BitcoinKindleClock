import requests
from bs4 import BeautifulSoup
from . import config


try:
    page = requests.get(config.blockurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    blockcount = soup.select_one(config.blockselector)
    blockcount = blockcount.text.split()[0]
except Exception:
    blockcount = 0

try:
    resp = requests.get(config.baserateurl)
    baserate = float(resp.json()['result'][f'XXBTZ{config.baseCurrency}']['o'])
except Exception:
    baserate = 0.0

try:
    resp = requests.get(config.rateurl)
    rate = resp.json()['rates'][config.currency] * baserate
except Exception:
    rate = 0.0

try:
    resp = requests.get(config.quoteurl)
    quote = resp.json()['body']
    author = resp.json()['author']['name']
except Exception:
    quote = ''
    author = ''

pageData = ('<!DOCTYPE html>'
'<html>'
    '<head>'
        '<title>Display</title>'
        '<link rel="stylesheet" href="./style.css">'
        '<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@1,400;1,500;1,900&amp;display=swap" rel="stylesheet">'
            '<meta charset="utf-8"/>'
            '<meta name="viewport" content="width=600">'
         '<meta name="apple-mobile-web-app-capable" content="yes">'
         '<meta name="apple-mobile-web-app-status-bar-style" content="white">'
     '</head>'
     '<body>'
         '<div class="bg"></div>'
         '<div class="info">'
             '<h3 class="price price--rate1">'
                 '<span class="curr">$</span>'
                 f'<span class="rate">{baserate:,.2f}</span>'
             '</h3>'
             f'<h1> {blockcount} </h1>'
             '<h3 class="price price--rate2">'
                 '<span class="curr">₹</span>'
                 f'<span class="rate">{rate:,.2f}</span>'
             '</h3>'
         '</div>'
         '<blockquote>'
             f'<p>{quote}</p>'
             f'<p class="author">— {author}</p>'
         '</blockquote>'
     '</body>'
'</html>')
with open("display.html", "w") as htmlfile:
    htmlfile.write(pageData)


