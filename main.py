import requests
import lxml.html as html

HOME_URL = 'https://www.lagaceta.com.ar/'

LINK_TO_ARTICLE = '//div[@class="card"]/div[@class="text"]/h2/a[@href]/@href'
ARTICLE_TITLE = '//h1[@id="spktitle"]/text()'
ARTICLE_SUMMARY = '//div[@class="articleHead "]/h2[@id="spksumary"]/text()'
ARTICLE_CONTENT = '//div[@class="articleBody"]/p/text()'

def parse_titles():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200 :
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            cualquiervariable = parsed.xpath(LINK_TO_ARTICLE)
            for nota in cualquiervariable:
                print (nota[39::])
            
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)
        

def run():
    parse_titles()

if __name__=="__main__":
    run()