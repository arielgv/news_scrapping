import lxml.html as html
import requests
import os
import datetime

HOME_URL = 'https://www.lagaceta.com.ar/'
LINK_TO_ARTICLE = '//div[@class="card"]/div[@class="text"]/h2/a[@href]/@href'
ARTICLE_TITLE = '//h1[@id="spktitle"]/text()'
ARTICLE_SUMMARY = '//div[@class="articleHead "]/h2[@id="spksumary"]/text()'
ARTICLE_CONTENT = '//div[@class="articleBody"]/p/text()'


def news(link, today):
    # This function scraps the entire News article each one and saves in a new folder after the date
    response = requests.get(link)
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    
    title = response.xpath(ARTICLE_TITLE)[0]
    title.replace('\"','')
    try:
        summary = response.xpath(ARTICLE_SUMMARY)[0]
    except IndexError:
        return
    content = response.xpath(ARTICLE_CONTENT) 
    with open(f'{today}/{title}.txt','w', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(summary)
        f.write('\n\n')

        for p in content:
            f.write(p)
        

def parse_links():
    #this function retrieves a list of each Link to any article on the newspaper
    response = requests.get(HOME_URL)
    response = response.content.decode("utf-8")
    parsed_response = html.fromstring(response)
    parsed = parsed_response.xpath(LINK_TO_ARTICLE)
    today = datetime.datetime.today().strftime('%d - %m - %Y')
    if not os.path.isdir(today):
        os.mkdir(today)
    
    for link in parsed:
        news(link,today)


    

def run():
    parse_links()

if __name__=="__main__":
    run()